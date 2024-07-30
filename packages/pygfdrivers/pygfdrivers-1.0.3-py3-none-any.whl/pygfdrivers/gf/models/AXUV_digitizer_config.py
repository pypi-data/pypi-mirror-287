from pydantic import AliasChoices, Field

from pygfdrivers.common.models.infrastructure.config import BaseConfigDeviceModel 
from pygfdrivers.common.models.device.device import BaseDeviceModel

class AXUVDeviceInfo(BaseDeviceModel):
    hostname: str = Field(
        default=None,
        alias='hostname',
        validation_alias=AliasChoices("hostname", "host")
    )

    username: str = Field(
        default=None,
        alias='hostname',
        validation_alias=AliasChoices("username", "user")
    )

    password: str = Field(
        default=None,
        alias='password',
        validation_alias = AliasChoices("password", "pass")
    )

    remote_file: str = Field(
        default=None,
        alias='remote_file',
        validation_alias = AliasChoices("remote_file", "remote")
    )

class AXUVDigitizerConfig(BaseConfigDeviceModel):
    scope: AXUVDeviceInfo = Field(
        defauly_factory=lambda: AXUVDeviceInfo(),
        alias='scope',
        validation_alias=AliasChoices('scope', 'scope_settings')
    )