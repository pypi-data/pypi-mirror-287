import bson
import json
import yaml
from typing import Any

from common.util.logger_manager import LOGGING_MODE, LoggerManager
import pandas as pd



class SaveUtil:

    def __init__(self, *args: Any, **kwds: Any) -> Any:
        self.log = LoggerManager("SaveUtil", LOGGING_MODE.DEBUG).log
        self.FILE_OPTIONS = {
            'bson': SaveUtil.save_bson,
            'json': SaveUtil.save_json,
            'csv': SaveUtil.save_csv,
            'yaml': SaveUtil.save_yaml
        }


    def save_file(self, data: dict, file_path: str, file_option: str = 'bson') -> None:
        """
        Save the data to a file.
        """
        #To allow for the saving of a dictionary or a data object
        try:
            if type(data) != dict:
                data = data.model_dump(by_alias=True, exclude_none=True)
            assert(type(file_option) == str)
            file_option = file_option.lower()
            if not file_option in self.FILE_OPTIONS:
                raise ValueError(f"File Option was {file_option}, but must be: {self.FILE_OPTIONS.keys()}")
            self.FILE_OPTIONS[file_option](data, file_path)
            self.log.info(f"File saved to {file_path}.{file_option}")
        except (FileNotFoundError, FileExistsError) as e:
            self.log.error(f"Error with file Location: {e}")
        except Exception as e:
            self.log.error(f"Error saving file: {e}")
        

    def save_bson(data: dict, file_path: str) -> None:
        """
        Save the data to a bson file.
        """
        file_path += '.bson'
        with open(file_path, 'wb') as file:
            file.write(bson.encode(data))
    

    def save_json(data: dict, file_path: str) -> None:
        """
        Save the data to a json file.
        """
        file_path += '.json'
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def save_csv(data: dict, file_path: str) -> None:
        """
        Save the data to a csv file.
        """
        file_path += '.csv'
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)

    def save_yaml(data: dict, file_path: str) -> None:
        """
        Save the data to a yaml file.
        """
        file_path += '.yaml'
        with open(file_path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
