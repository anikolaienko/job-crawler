import os
import json
from enum import Enum
from typing import Dict, List

from dotenv import load_dotenv

class CrawlerType(Enum):
    JSON = "json"

class CrawlerConfig:
    name: str
    type: CrawlerType
    url: str
    base_path_parts: List[str]
    params: Dict[str, str]
    result: List[str]

    def __init__(self, config: Dict[str, any]):
        self.name = config['name']
        self.type = CrawlerType[config['type'].upper()]
        self.url = config["url"]
        self.base_path_parts = config["base_path"].split("/")
        self.params = config["params"]
        self.result = config["result"]

load_dotenv() # load from .env file if present

config_file = "config.json"
telegram_token = os.getenv("TELEGRAM_TOKEN")
db_connection = os.getenv("DB_CONNECTION")

__config = json.load(open(config_file, "r"))
crawlers_config: List[CrawlerConfig] = list(map(CrawlerConfig, __config["crawlers"]))
