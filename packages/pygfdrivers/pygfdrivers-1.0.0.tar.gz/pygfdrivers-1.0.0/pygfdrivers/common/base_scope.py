import os
import json
from abc import ABC
from typing import Dict
from pydantic import BaseModel
from collections import defaultdict

# custom module
from common.model_map import model_map
from common.base_device import BaseDevice
from common.util.utilities import save_bson

from dtacq.models.scope_data import DtacqSiteDataModel
from keysight.models.scope_data import KeysightChannelDataModel


class BaseScope(BaseDevice, ABC):
    def __init__(self, scope_config: BaseModel) -> None:
        super().__init__(scope_config, 'scope')
        self.scope_talk_delay = 0.1  # 0.1 not working for Lecroys

        self.file_name = self.name
        self.scope = None

        self.device_model = None
        self.scope_type = self.config.scope.device_type

        self.init_scope_info()

    def init_scope_info(self) -> None:
        # TODO: Need to make this dyanmic to the scope_info specific to the scope_type
        try:
            self.scope_info = model_map['scope_info'].get(self.scope_type)()
            if self.scope_info is None:
                raise ValueError(f"Scope type '{self.scope_type}' does not have mapped scope_info model.'")

            setattr(self.scope_info, 'scope', self.config.scope)
            if 'dtacq' in self.scope_type:
                setattr(self.scope_info, 'active_sites', self.config.active_sites)
            else:
                setattr(self.scope_info, 'active_channels', self.config.active_channels)
        except Exception as e:
            self.log.error(f"Initializing scope info encountered error: {e}")

    def clear_scope_info_data(self) -> None:
        if 'dtacq' in self.scope_type:
            setattr(self.scope_info, 'sites', defaultdict(DtacqSiteDataModel))
        elif 'keysight' in self.scope_type:
            setattr(self.scope_info, 'channels', defaultdict(KeysightChannelDataModel))

    # ------------------------------------------------------------------------------------
    #  Data Capture
    # ------------------------------------------------------------------------------------

    def collectDataFromScope(self) -> None:
        self.log.info("Downloading data...")

        self.is_triggered = getattr(self, 'trigger_status')
        self.log.info(f"Trigger Status: {self.is_triggered}")
        try:
            if not self.is_armed:
                raise ValueError("Scope did not arm.")

            if not self.is_connected:
                raise ValueError("Scope is not connected.")

            if not self.is_triggered:
                raise ValueError("Scope failed to trigger.")

            getattr(self, 'populateVoltValueForActiveChannels')()
            self.is_downloaded = True
        except Exception as e:
            self.log.error(f"Downloading data from scope encountered error: {e}")
            self.is_downloaded = False

        finally:
            self.log.info(f"{'Finished collecting data.' if self.is_downloaded else 'Failed to collect data.'}")
            self.scope_info.scope.flag_downloaded = self.is_downloaded
            self.scope_info.scope.flag_triggered = self.is_triggered
            self.scope_info.scope.flag_connected = self.is_connected
            self.prev_config = self.scope_info
            self.save_data_to_file()

    # ------------------------------------------------------------------------------------
    #  Save Methods
    #
    # TODO: Remove the save_utility functions out of here and into its own module
    #
    # ------------------------------------------------------------------------------------

    # TODO: Determine how the files should be saved in the file location
    def save_data_to_file(self) -> None:
        file_format = self.config.scope.file_format
        export_dict = self.scope_info.model_dump(by_alias=True, exclude_none=True)

        if file_format == 'bson':
            self.save_as_bson(export_dict)
        elif file_format == 'json':
            self.save_as_json(export_dict)
        else:
            self.save_as_csv(export_dict)

        self.is_downloading = True

    def save_as_bson(self, export_dict: Dict) -> None:
        self.log.info(f"Saving file as a BSON")
        try: 
            file_path = os.path.join(self.save_path, f"{self.file_name}.bin")
            save_bson(export_dict, file_path)
        except Exception as e:
            self.log.error(f"Saving as BSON file encountered error: {e}")

    def save_as_json(self, export_dict: Dict) -> None:
        self.log.info(f"Saving file as a JSON")
        try: 
            file_path = os.path.join(self.save_path, f"{self.file_name}.json")
            with open(file_path, 'w') as jsonFile:
                json.dump(export_dict, jsonFile, indent=2)
        except Exception as e:
            self.log.error(f"Saving as JSON file encountered error: {e}")

    def save_as_csv(self, export_dict: Dict) -> None:
        pass

    # TODO: Need to add functionality that creates folder if it doesn't yet exist
    # def create_folder_path(self) -> str:
    #     folder_path = os.path.join(self.save_path, self.file_name)
    #     self.log.info(f"Creating folder path at {folder_path}")
    #     if not os.path.exists(folder_path):
    #         try:
    #             os.makedirs(folder_path)
    #         except os.error as e:
    #             self.log.error(f"Creating folder path encountered os.error: {e}")
    #         except Exception as e:
    #             self.log.error(f"Creating folder path encountered general error: {e}")
    #     self.log.info(f"Global folder path created at {folder_path} for all file saving purposes.")
    #     return folder_path
