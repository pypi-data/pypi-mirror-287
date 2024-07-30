from collections import defaultdict
from typing import List, Dict
from pydantic import AliasChoices, Field

# custom models
from common.models.infrastructure.config import BaseConfigDeviceModel
from common.models.device.visa import BaseVisaDeviceModel
from keysight.models.capture import KeysightCaptureModel
from keysight.models.trigger import KeysightTriggerModel
from keysight.models.channel import KeysightChannelModel


# This model is used for configuring the devices from a yaml file, hence the different aliases for the fields
class KeysightScopeConfigModel(BaseConfigDeviceModel):
    scope: BaseVisaDeviceModel = Field(
        default_factory=lambda: BaseVisaDeviceModel(),
        validation_alias=AliasChoices('scope', 'scope_settings', 'scope_info')
    )
    capture: KeysightCaptureModel = Field(
        default_factory=lambda: KeysightCaptureModel(),
        validation_alias=AliasChoices('capture', 'capture_settings')
    )
    trigger: KeysightTriggerModel = Field(
        default_factory=lambda: KeysightTriggerModel(),
        validation_alias=AliasChoices('trigger', 'trigger_settings')
    )
    active_channels: List[int] = Field(
        default_factory=lambda: list(),
        validation_alias=AliasChoices('active_channels', 'active_sources')
    )
    channels: Dict[int, KeysightChannelModel] = Field(
        default_factory=lambda: defaultdict(KeysightChannelModel),
        validation_alias=AliasChoices('channels', 'channel_settings')
    )
