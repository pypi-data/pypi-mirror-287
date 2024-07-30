from typing import List, Dict
from collections import defaultdict
from pydantic import AliasChoices, Field

# custom models
from pygfdrivers.common.models.infrastructure.config import BaseConfigDeviceModel
from pygfdrivers.common.models.device.visa import BaseVisaDeviceModel
from pygfdrivers.lecroy.models.trigger import LecroyTriggerModel
from pygfdrivers.lecroy.models.capture import LecroyCaptureModel
from pygfdrivers.lecroy.models.channel import LecroyChannelModel


# This model is used for configuring the devices from a yaml file, hence the different aliases for the fields
class LecroyScopeConfigModel(BaseConfigDeviceModel):
    scope: BaseVisaDeviceModel = Field(
        default_factory=lambda: BaseVisaDeviceModel(),
        validation_alias=AliasChoices('scope', 'scope_settings', 'scope_info')
    )
    capture: LecroyCaptureModel = Field(
        default_factory=lambda: LecroyCaptureModel(),
        validation_alias=AliasChoices('capture', 'capture_settings')
    )
    trigger: LecroyTriggerModel = Field(
        default_factory=lambda: LecroyTriggerModel(),
        validation_alias=AliasChoices('trigger', 'trigger_settings')
    )
    active_channels: List[int] = Field(
        default_factory=lambda: list(),
        validation_alias=AliasChoices('active_channels', 'active_sources')
    )
    channels: Dict[int, LecroyChannelModel] = Field(
        default_factory=lambda: defaultdict(LecroyChannelModel),
        validation_alias=AliasChoices('channels', 'channel_settings')
    )
