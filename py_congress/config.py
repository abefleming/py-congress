from typing import Literal, Union
from pydantic import BaseModel, StrictStr, HttpUrl
import os
from dotenv import load_dotenv


class PyCongressConfig(BaseModel):
    api_key: StrictStr
    api_version: StrictStr = "v3"
    base_url: HttpUrl = "https://api.congress.gov/"
    response_format: Literal["json", "xml"] = "json"


def full_endpoint(config: PyCongressConfig) -> str:
    return f"{config.base_url}{config.api_version}"


def generate_config() -> PyCongressConfig:
    load_dotenv()
    try:
        config = PyCongressConfig(api_key=os.environ["API_KEY"])
        return config
    except KeyError:
        raise Exception("API_KEY not found in environment variables.")
