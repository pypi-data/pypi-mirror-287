from pydantic import BaseModel
from abc import ABC, abstractmethod
from common.save_utility import SaveUtil
import os

# custom package
from common.util.logger_manager import LOGGING_MODE, LoggerManager


#TODO Get rid of the client_config
class BaseDevice(ABC):
    def __init__(self, device_config: BaseModel, device_type: str = 'scope') -> None:
        self.device_type = device_type

        self.config = device_config
        self.name = getattr(device_config, self.device_type).device_name

        self.log = LoggerManager(self.name, LOGGING_MODE.DEBUG).log
        self.saveUtil = SaveUtil()

        self.handler_type = getattr(device_config, self.device_type).device_handler
        self.save_path = getattr(device_config, self.device_type).file_save_path
        self.file_type = getattr(device_config, self.device_type).file_format
        self.prev_config = None

        self.is_enabled = getattr(device_config, self.device_type).device_enabled
        self.is_downloaded = False
        self.is_triggered = False
        self.is_connected = False
        self.is_armed = False
        self.is_aborted = False
        self.data = None

    def init(self) -> None:
        raise NotImplementedError("Child classes must implement 'init' method.")

    # ------------------------------------------------------------------------------------
    #  Base Device Control Methods - Must be overridden by the child class
    # ------------------------------------------------------------------------------------

    @abstractmethod
    def connect(self) -> None:
        raise NotImplementedError("Child classes must implement 'connect' method.")

    @abstractmethod
    def disconnect(self) -> None:
        raise NotImplementedError("Child classes must implement 'disconnect' method.")

    @abstractmethod
    def check_connection(self) -> bool:
        raise NotImplementedError("Child classes must implement 'check_connection' method.")

    # ------------------------------------------------------------------------------------
    #  Base Device Control Methods - Must be overridden by the child class
    # ------------------------------------------------------------------------------------

    @abstractmethod
    def apply_configurations(self) -> None:
        raise NotImplementedError("Child classes must implement 'apply_configurations' method.")

    @abstractmethod
    def arm(self) -> None:
        raise NotImplementedError("Child classes must implement 'arm' method.")

    @abstractmethod
    def abort(self) -> None:
        raise NotImplementedError("Child classes must implement 'abort' method.")

    @abstractmethod
    def prep_shot(self) -> None:
        raise NotImplementedError("Child classes must implement 'prep_shot' method.")

    # ------------------------------------------------------------------------------------
    #  Base Data Methods - Must be overridden by the child class
    # ------------------------------------------------------------------------------------

    @abstractmethod
    def fetch_data(self, *args, **kwargs) -> None:
        raise NotImplementedError("Child classes must implement 'fetch_data' method.")

    @abstractmethod
    def fetch_metadata(self, *args, **kwargs) -> None:
        raise NotImplementedError("Child classes must implement 'fetch_metadata' method.")
    
    # ------------------------------------------------------------------------------------
    #  File Util Method - Call to run fetch_data then save data to file
    # ------------------------------------------------------------------------------------

    def save_data(self):
        # data = getattr(self, data_method)()
        if self.data is not None:
            file_path = os.path.join(self.save_path, self.name)
            self.saveUtil.save_file(self.data, file_path, self.file_type)

    def reconnect(self) -> None:
        self.disconnect()
        self.connect()

    def __del__(self) -> None:
        self.disconnect()
