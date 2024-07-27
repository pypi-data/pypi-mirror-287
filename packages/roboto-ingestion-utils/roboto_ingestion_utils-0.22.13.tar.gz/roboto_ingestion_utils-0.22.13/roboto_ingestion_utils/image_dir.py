from PIL import Image
from pathlib import Path
import time
from typing import List, Literal, Optional, Union
import numpy as np
from io import BytesIO
import re

# protobuf serialization utils
from mcap_protobuf.writer import Writer as ProtobufWriter
from foxglove_schemas_protobuf.CompressedImage_pb2 import CompressedImage as CompressedImage_Protobuf

# ros2 serialization utils
from rosbags.typesys.stores.latest import sensor_msgs__msg__CompressedImage as CompressedImage_ROS2
from rosbags.typesys.stores.latest import std_msgs__msg__Header as Header_ROS2
from rosbags.typesys.stores.latest import builtin_interfaces__msg__Time as Timestamp_ROS2
from rosbags.typesys import Stores, get_typestore

typestore = get_typestore(Stores.LATEST)

from mcap_ros2.writer import Writer as ROS2Writer



from roboto.domain import topics
from roboto_ingestion_utils import ingestion_utils


ALLOWED_IMG_FORMATS = ["png", "jpg", "jpeg"]

def create_image_message_path_request(message_path_name: str):
    message_path = topics.AddMessagePathRequest(
            message_path=message_path_name,
            data_type="image",
            canonical_data_type=topics.CanonicalDataType.Image,
            )
    return [message_path]

def image_to_message(fname: Union[str, Path], 
                     timestamp: int, 
                     timestamp_format: str,
                     encoding: Literal['protobuf', 'cdr'],
                     frame_id: Optional[int]=None):
    if isinstance(fname, str):
        fname = Path(fname)

    ext = fname.suffix.lower()[1:] # remove period from extension
    assert ext in ALLOWED_IMG_FORMATS, f"Error: expected an image format from {ALLOWED_IMG_FORMATS}, received {ext}"

    raw_img = Image.open(fname)

    if encoding == 'protobuf':
        msg = CompressedImage_Protobuf()
        if timestamp_format == "seconds":
            msg.timestamp.FromSeconds(timestamp)
        elif timestamp_format == "milliseconds":
            msg.timestamp.FromMilliseconds(timestamp)
        elif timestamp_format == "microseconds":
            msg.timestamp.FromMicroseconds(timestamp)
        elif timestamp_format == "nanoseconds":
            msg.timestamp.FromNanoseconds(timestamp)
        else:
            raise ValueError(f"Error: timestamp must be in format seconds, milliseconds, microseconds, or nanoseconds, received {timestamp_format}")
        buffer = BytesIO()
        # convert jpg to jpeg
        raw_img.save(buffer, format='jpeg')
        msg.data = buffer.getvalue()
        msg.format = 'JPEG' 
    elif encoding ==  'cdr':
        # ROS2 messages require passing a frame_id
        assert frame_id is not None, "Error: ROS2 messages require a frame id"

        # report time as a ROS2 Timestamp in seconds + addl nanoseconds
        # we simply pass nanoseconds, and large values are wrapped automatically
        if timestamp_format == "seconds":
            timestamp = int(timestamp * 1e9)
        elif timestamp_format == "milliseconds":
            timestamp = int(timestamp * 1e6)
        elif timestamp_format == "microseconds":
            timestamp = int(timestamp * 1e3)
        elif timestamp_format == "nanoseconds":
            pass # timestamp automatically in NS
        stamp = Timestamp_ROS2(sec=0,
                               nanosec=timestamp)

        msg_header = Header_ROS2(stamp=stamp,
                                 frame_id=str(frame_id))
        buffer = BytesIO()
        raw_img.save(buffer, format="jpeg")

        msg = CompressedImage_ROS2(header=msg_header,
                                   format="jpeg",
                                   #data=np.asarray(raw_img))
                                   #data=im_buff_arr)
                                   data=buffer.getvalue())

    return msg

def image_dir_to_mcap(input_dir: Path,
                      output_dir: Optional[Union[str, Path]]=None,
                      timestamp_format: str="nanoseconds",
                      img_format: Optional[str]=None,
                      start_timestamp: Optional[int]=None,
                      frame_rate: Optional[int]=None,
                      timestamps: Optional[List]=None,
                      encoding: Literal['protobuf', 'cdr']='protobuf'):
    """
    Ingest a directory of images to an mcap file
    using encoding:
        1. foxglove's CompressedImage protobuf format
        2. CDR ROS2 format
    """
    assert encoding in ["protobuf", "cdr"]
    if img_format:
        assert img_format.lower() in ALLOWED_IMG_FORMATS, f"Error: expected one of {ALLOWED_IMG_FORMATS}, received {img_format}"
    
    assert (frame_rate is not None and start_timestamp is not None) or timestamps is not None, "Error: must provide one of a timestamp list or a framerate at which to create timestamps"
    assert timestamp_format, "timestamp must be passed with a timestamp format string."

    # create a list of all image files of specified format in the input dir
    if img_format:
        image_files = [x for x in input_dir.glob(f"*{img_format}")]
    else:
        image_files = []
        for fmt in ALLOWED_IMG_FORMATS + [x.upper() for x in ALLOWED_IMG_FORMATS]:

            image_files.extend([x for x in input_dir.glob(f"*.{fmt}")])
    
    assert image_files, f"Error: no image files in {input_dir}"

    # Sort image files using custom logic
    sorted_img_files = sorted(image_files, key=custom_sort_key)


    rel_file_path = image_files[0] 
    
    if output_dir is None:
    # setup temp output directory
        output_dir, _ = ingestion_utils.setup_output_folder_structure(
                input_dir=str(input_dir),
                file_path=str(input_dir / rel_file_path)
                )
    if isinstance(output_dir, str):
        output_dir = Path(output_dir)

    if frame_rate is not None and start_timestamp is not None:
        timestamps = [start_timestamp + int(x/frame_rate * 1e9) for x in range(len(sorted_img_files))]

    assert len(timestamps) == len(image_files), "Error: each image must have one timestamp,\
                            received {len(image_files) images and len(timestamps) timestamps}"

    # Write out to MCAP
    topic_name = input_dir.name
    fname = str(output_dir / f"{topic_name}.mcap")

    if encoding == "protobuf":
        with open(fname, "wb") as f:
            writer = ProtobufWriter(f)
            for i, (timestamp, image) in enumerate(zip(timestamps, sorted_img_files)):
                image_msg = image_to_message(image,
                                             timestamp=timestamp,
                                             timestamp_format=timestamp_format,
                                             encoding="protobuf",
                                             frame_id=i)
                writer.write_message(
                    topic=topic_name,
                    message=image_msg,
                        )
            writer.finish()
    elif encoding == "cdr":
        #writer = StandardWriter(output=fname)
        # returns msgdef, md5_checksum
        msgdef, _ = typestore.generate_msgdef(typename="sensor_msgs/msg/CompressedImage",
                                           ros_version=2)
        writer = ROS2Writer(output=fname)
        schema = writer.register_msgdef(
                datatype="sensor_msgs/msg/CompressedImage",
                msgdef_text=msgdef
                )

        for i, (timestamp, image) in enumerate(zip(timestamps, sorted_img_files)):
            image_msg = image_to_message(image,
                                         timestamp=timestamp,
                                         timestamp_format=timestamp_format,
                                         encoding="cdr",
                                         frame_id=i)
            #ROS2Writer automatically registers a channel and topic
            writer.write_message(
                    topic=topic_name,
                    schema=schema,
                    message=image_msg
                    )

    topic_entry = {}

    topic_entry["first_timestamp"] = timestamps[0] 
    topic_entry["last_timestamp"] = timestamps[-1]
    topic_entry["nr_msgs"] = len(sorted_img_files)
    topic_entry["mcap_path"] = fname
    topic_info_dict = {topic_name: topic_entry}

    return topic_info_dict, None, {}, {}

# custom sorting logic: extract number from file_name
# and use as sorting key, irrespective of zero-padding
def extract_number(file_path):
    file_name = file_path.name
    match = re.search(r'(\d+)', file_name)
    return int(match.group(0)) if match else None

def custom_sort_key(file_name):
    number_part = extract_number(file_name)
    if number_part is not None:
        return (0, number_part)
    else:
        return (1, file_name)
        
