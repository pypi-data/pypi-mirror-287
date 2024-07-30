from typing import List, Dict
from collections import defaultdict
from pydantic import Field, AliasChoices

# custom models
from common.models.infrastructure.config import BaseConfigDeviceModel
from common.models.device.device import BaseDeviceModel
from common.models.device.channel import BaseChannelModel
from common.models.device.trigger import BaseTriggerModel 
from common.models.device.capture import BaseCaptureModel

from dtacq.models.acq425 import Acq425ChannelModel, Acq425SiteModel
from dtacq.models.acq480 import Acq480ChannelModel, Acq480SiteModel


class DtacqChannelModel(BaseChannelModel, Acq425ChannelModel, Acq480ChannelModel):
    ch_gain: int = Field(
        default=None,
        alias='gain',
        validation_alias=AliasChoices('ch_probe', 'probe', 'gain', 'attenuation', 'attn')
    )


class DtacqSiteModel(Acq425SiteModel, Acq480SiteModel):
    channels: Dict[int, DtacqChannelModel] = Field(
        default_factory=lambda: defaultdict(DtacqChannelModel),
        validation_alias=AliasChoices('channels', 'channel_settings')
    )


class DtacqScopeConfigModel(BaseConfigDeviceModel):
    scope: BaseDeviceModel = Field(
        default_factory=lambda: BaseDeviceModel(),
        validation_alias=AliasChoices('scope', 'scope_settings', 'scope_info')
    )
    capture: BaseCaptureModel = Field(
        default_factory=lambda: BaseCaptureModel(),
        validation_alias=AliasChoices('capture', 'capture_settings')
    )
    trigger: BaseTriggerModel = Field(
        default_factory=lambda: BaseTriggerModel(),
        validation_alias=AliasChoices('trigger', 'trigger_settings')
    )
    active_sites: Dict[str, List[int]] = Field(
        default_factory=lambda: defaultdict(list),
        validation_alias=AliasChoices('active_sites', 'active_channels', 'active_modules')
    )
    sites: Dict[str, DtacqSiteModel] = Field(
        default_factory=lambda: defaultdict(DtacqSiteModel),
        validation_alias=AliasChoices('sites', 'site_settings')
    )
