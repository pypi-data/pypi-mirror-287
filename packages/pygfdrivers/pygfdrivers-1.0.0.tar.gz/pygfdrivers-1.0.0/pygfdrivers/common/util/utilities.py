import yaml
import bson
import logging
import numpy as np
from typing import Dict, Any, Union, Optional

log = logging.getLogger(__name__)


def open_bson(bson_file: str) -> Optional[Dict]:
    if not bson_file.endswith('.bin'):
        raise ValueError("Not a .bin file type.")

    try:
        with open(bson_file, 'rb') as file:
            bson_data = bson.decode_all(file.read())
            if not bson_data:
                raise ValueError("BSON file is empty.")
            return bson_data[0]
    except Exception as e:
        raise ValueError(f"Failed to open '{bson_file}' with error: {e}")


def open_yaml(yaml_file: str) -> Optional[Dict]:
    if not yaml_file.endswith(('.yml', '.yaml')):
        raise ValueError("Not a .yml or .yaml file type.")

    try:
        with open(yaml_file, "r") as file:
            yaml_dict = yaml.safe_load(file)
            if yaml_dict is None:
                raise ValueError("YAML file is empty or improperly formatted.")
            return yaml_dict
    except Exception as e:
        raise ValueError(f"Failed to open '{yaml_file}' with error: {e}") 

def load_yaml(yaml_file: str) -> Optional[Dict]:
    try:
        yaml_dict = yaml.safe_load(yaml_file)
        if yaml_dict is None:
            raise ValueError("YAML file is empty or improperly formatted.")
        return yaml_dict
    except Exception as e:
        raise ValueError(f"Failed to open '{yaml_file}' with error: {e}")    


def save_bson(file_dict: Dict, file_path: str) -> None:
    try:
        with open(file_path, 'wb') as file:
            file.write(bson.encode(file_dict))
    except Exception as e:
        log.error(f"Writing as a BSON file encountered error: {e}")


def convert_value(value) -> Union[int, float, str]:
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value.lower()
    return value


def convert_si_suffix(value: str) -> Optional[float]:
    suffix_map = {
        'p': 1e-12,  # pico
        'n': 1e-9,   # nano
        'u': 1e-6,   # micro
        'm': 1e-3,   # milli
        'k': 1e3,    # kilo
        'K': 1e3,    # kilo
        'M': 1e6,    # mega
        'G': 1e9,    # giga
        'T': 1e12,   # tera
    }

    if value[-1].isdigit():
        return float(value)  # No suffix, plain float

    suffix = value[-1]
    if suffix in suffix_map:
        return float(value[:-1]) * suffix_map[suffix]
    else:
        raise ValueError(f"Unknown SI suffix: {suffix}")


def has_prop(obj: Any, getter: str) -> bool:
    return isinstance(getattr(type(obj), getter, None), property)


def has_setter(obj: Any, setter: str) -> bool:
    prop = getattr(type(obj), setter, None)
    return isinstance(prop, property) and prop.fset is not None


def get_number_of_points(self):
    try:
        num_points  = self.query_scope("MEMORY_SIZE?")
        unit_scale = {'G': 1E9, 'M': 1E6, 'k': 1E3, 'K': 1E3}
        for unit in unit_scale.keys():
            if num_points.find(unit) != -1:
                num_points = num_points.split(unit)
                num_points = float(num_points[0]) * unit_scale[unit]
                break
        return float(num_points)
    except Exception as e:
        self.log.info(f"Error getting getting number of points: {e}")


def format_raw_bytes(channel_data: np.ndarray, v_div: float = None, v_offset: float = None):
    # Converts analog byte values to decimal
    volts = [byte * (v_div / 25) - v_offset for byte in channel_data]
    return volts



# import os
# import inspect
# import numpy as np
# from stat import ST_MODE
# from json import JSONEncoder
# from datetime import datetime
#
#
# def flatten_dict(data_dict):
#     """ Recursive function to return a dictionary representation of an object with nested objects """
#     try:
#         for key in data_dict:
#             if isinstance(data_dict[key], data_dict) or inspect.isclass(data_dict[key]):
#                 temp_dict = data_dict[key] if isinstance(data_dict[key], data_dict) else data_dict[key].__dict__
#                 data_dict[key] = flatten_dict(temp_dict)
#         return data_dict
#     except Exception as e:
#         log.error(f"Expanding nested objects into flattened dictionary encountered error: {e}")
#
#
# def save_bson(file_dict: Dict, file_path: str):
#     try:
#         with open(file_path, 'wb') as file:
#             file.write(bson.encode(file_dict))
#     except Exception as e:
#         log.error(f"Writing as a BSON file encountered error: {e}")
#         if "Permission denied" in str(e):
#             log.error(f"Permission denied, recording permissions to 'nfs/expdata/record_permissions.txt'.")
#             record_permissions('record_permissions.txt', '/nfs/expdata')
#
#
# def record_permissions(record_path, mount_path):
#     """ Excerpt from Todd Chisholm for troubleshooting file permission issues """
#     now = datetime.now()
#     date_str = now.strftime("%d/%m/%Y %H:%M:%S")
#     try:
#         with open(record_path, "a") as file:
#             top_permissions = oct(os.stat(mount_path)[ST_MODE])
#             pi3_dir_permissions = oct(os.stat(os.path.join(mount_path, "PI3"))[ST_MODE])
#             last_shot_permissions = oct(os.stat(os.path.join(mount_path, "PI3", "LastShot.txt"))[ST_MODE])
#             file.write(f"{date_str}: {top_permissions}, {pi3_dir_permissions}, {last_shot_permissions}\n")
#     except Exception as e:
#         log.error(f"Couldn't write to file when recording file permissions: {e}")
#
#
# # Numpy encoder for json serialization of numpy arrays
# # Taken from https://pynative.com/python-serialize-numpy-ndarray-into-json/
# class numpy_array_encoder(JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, np.ndarray):
#             return obj.tolist()
#         return JSONEncoder.default(self, obj)
