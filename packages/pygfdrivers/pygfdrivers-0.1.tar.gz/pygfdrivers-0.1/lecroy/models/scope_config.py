from typing import List, Dict
from collections import defaultdict
from pydantic import AliasChoices, Field

# custom models
from common.models.infrastructure.config import BaseConfigModel
from common.models.device.visa import BaseVisaDeviceModel
from lecroy.models.trigger import LecroyTriggerModel
from lecroy.models.capture import LecroyCaptureModel
from lecroy.models.channel import LecroyChannelModel


# This model is used for configuring the devices from a yaml file, hence the different aliases for the fields
class LecroyScopeConfigModel(BaseConfigModel):
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
