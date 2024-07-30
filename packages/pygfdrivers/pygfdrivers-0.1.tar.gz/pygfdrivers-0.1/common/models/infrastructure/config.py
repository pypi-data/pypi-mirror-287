from pydantic import BaseModel, Field, AliasChoices

class BaseConfigModel(BaseModel):
    config_id: str = Field(
        default=None,
        validation_alias=AliasChoices('config_id', 'config_name','configuration_name')
    )

    config_type: str = Field(
        default= None,
        validation_alias=AliasChoices('config_type', 'configuration_type')
    )