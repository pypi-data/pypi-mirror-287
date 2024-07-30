from pydantic import AliasChoices, Field
from typing import Dict, List
from collections import defaultdict

from common.models.infrastructure.config import BaseConfigDeviceModel
from common.models.device.visa import BaseVisaDeviceModel
from common.models.device.trigger import BaseTriggerModel
from common.models.device.capture import BaseCaptureModel
from common.models.device.channel import BaseChannelModel


class GFTriggerModel(BaseTriggerModel):
    pass

class GFDigitizerInfo(BaseVisaDeviceModel):
    pass

class GFCaptureModel(BaseCaptureModel):
    volt_range: float = Field(
        default=None,
        alias='volt_range',
        validation_alias=AliasChoices('volt_range', 'voltage_range')
    )

    acq_start_sample: int = Field(
        default= None,
        alias= 'start_sample',
        validation_alias=AliasChoices('acq_start_sample', 'start_sample')
    )

class GFChannelModel(BaseChannelModel):
    ch_scale_m: float = Field(
        default=1.0,
        alias='scale_m',
        validation_alias=AliasChoices('ch_scale_m', 'scale_m')
    )

    ch_scale_b: float = Field(
        default=50.0,
        alias='scale_b',
        validation_alias=AliasChoices('ch_scale_b', 'scale_b')
    )


class GFDigitizerConfigModel(BaseConfigDeviceModel):
    scope: GFDigitizerInfo = Field(
        default_factory=lambda: GFDigitizerInfo(),
        validation_alias=AliasChoices('scope', 'scope_settings', 'scope_info')
    )
    capture: GFCaptureModel = Field(
        default_factory=lambda: GFCaptureModel(),
        validation_alias=AliasChoices('capture', 'capture_settings')
    )
    trigger: GFTriggerModel = Field(
        default_factory=lambda: GFTriggerModel(),
        validation_alias=AliasChoices('trigger', 'trigger_settings')
    )
    active_channels: List[int] = Field(
        default_factory=lambda: list(),
        validation_alias=AliasChoices('active_channels', 'active_sources')
    )
    channels: Dict[int, GFChannelModel] = Field(
        default_factory=lambda: defaultdict(GFChannelModel),
        validation_alias=AliasChoices('channels', 'channel_settings')
    )