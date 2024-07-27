import yaml
from lime.config import Config

def load_config(path: str) -> Config:
    with open(path, 'r') as file:
        config_dict = yaml.safe_load(file)
    return Config(**config_dict)