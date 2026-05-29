import os
import yaml
from dotenv import load_dotenv

load_dotenv()
YAML_PATH = "./config.yaml"


def load_config() -> dict[str:any]:
    # for github actions
    config_str = os.getenv("CONFIG_YAML")
    if config_str:
        return yaml.load(config_str, Loader=yaml.FullLoader)

    # for local use
    if os.path.exists(YAML_PATH):
        with open(YAML_PATH, "r", encoding="utf-8") as f:
            return yaml.load(f, Loader=yaml.FullLoader)
    raise Exception("未找到配置信息")


config: dict[str, any] = load_config()
