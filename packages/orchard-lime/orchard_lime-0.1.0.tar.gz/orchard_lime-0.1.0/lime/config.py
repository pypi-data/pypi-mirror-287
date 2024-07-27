from pydantic import BaseModel

class MaasConfig(BaseModel):
    base_url: str
    api_key: str
    default_model: str
    models: list[str]

class Config(BaseModel):
    maas: MaasConfig