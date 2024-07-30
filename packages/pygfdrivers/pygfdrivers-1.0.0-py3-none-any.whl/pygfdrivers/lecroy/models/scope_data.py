from typing import List, Dict
from collections import defaultdict
from pydantic import BaseModel, Field

# custom models
from common.models.device.visa import BaseVisaDeviceModel
from lecroy.models.trigger import LecroyTriggerModel
from lecroy.models.capture import LecroyCaptureModel
from lecroy.models.channel import LecroyChannelDataModel


# This model represents what is ultimately saved into the server as containing the user set configurations, the
# actual configurations read from the scope, and also the data obtained from the scope.
class LecroyScopeDataModel(BaseModel):
    scope: BaseVisaDeviceModel = Field(
        default_factory=lambda: BaseVisaDeviceModel()
    )
    capture: LecroyCaptureModel = Field(
        default_factory=lambda: LecroyCaptureModel()
    )
    trigger: LecroyTriggerModel = Field(
        default_factory=lambda: LecroyTriggerModel()
    )
    active_channels: List[int] = Field(
        default_factory=lambda: list()
    )
    channels: Dict[str, LecroyChannelDataModel] = Field(
        default_factory=lambda: defaultdict(LecroyChannelDataModel)
    )
