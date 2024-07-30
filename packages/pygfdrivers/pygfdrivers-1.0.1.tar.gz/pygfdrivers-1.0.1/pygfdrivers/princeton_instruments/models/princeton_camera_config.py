from pydantic import AliasChoices, Field

from common.models.infrastructure.config import BaseConfigDeviceModel
from common.models.device.device import BaseDeviceModel
from princeton_instruments.models.capture import PrincetonCaptureConfig
from princeton_instruments.models.sensor import PrincetonSensorConfig
from common.models.device.trigger import BaseTriggerModel


class PrincetonTriggerConfig(BaseTriggerModel):
    pass

class PrincetonCameraInfo(BaseDeviceModel):
    pass


class PrincetonCameraConfigModel(BaseConfigDeviceModel):
    camera: PrincetonCameraInfo = Field(
        default_factory=lambda: PrincetonCameraInfo(),
        validation_alias=AliasChoices('camera', 'device', 'camera_info', 'camera_settings')
    )
    capture: PrincetonCaptureConfig = Field(
        default_factory=lambda: PrincetonCaptureConfig(),
        validation_alias=AliasChoices('capture', 'capture_settings')
    )
    trigger: PrincetonTriggerConfig = Field(
        default_factory=lambda: PrincetonTriggerConfig(),
        validation_alias=AliasChoices('trigger', 'trigger_settings')
    )
    sensor: PrincetonSensorConfig = Field(
        default_factory=lambda: PrincetonSensorConfig(),
        validation_alias=AliasChoices('sensor', 'sensor_settings')
    )