from collections import defaultdict
from typing import List, Dict, Union
from pydantic import BaseModel, Field

# custom models
from common.models.device.device import BaseDeviceModel
from common.models.device.trigger import BaseTriggerModel
from common.models.device.capture import BaseCaptureModel
from common.models.device.source import BaseSourceDataModel

from dtacq.models.acq425 import Acq425SiteModel
from dtacq.models.acq480 import Acq480SiteModel
from dtacq.models.scope_config import DtacqChannelModel


class DtacqChannelDataModel(BaseSourceDataModel, DtacqChannelModel):
    raw_data: List[Union[int, List[int]]] = Field(default_factory=lambda: list())


class DtacqSiteDataModel(Acq425SiteModel, Acq480SiteModel):
    channels: Dict[str, DtacqChannelDataModel] = Field(default_factory=lambda: defaultdict(DtacqChannelDataModel))


class DtacqScopeDataModel(BaseModel):
    scope: BaseDeviceModel = Field(default_factory=lambda: BaseDeviceModel())
    capture: BaseCaptureModel = Field(default_factory=lambda: BaseCaptureModel())
    trigger: BaseTriggerModel = Field(default_factory=lambda: BaseTriggerModel())
    active_sites: Dict[str, List[int]] = Field(default_factory=lambda: defaultdict(list))
    sites: Dict[str, DtacqSiteDataModel] = Field(default_factory=lambda: defaultdict(DtacqSiteDataModel))
