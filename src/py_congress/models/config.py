from typing import Literal, Union
from pydantic import BaseModel, StrictStr, HttpUrl

class PyCongressConfig(BaseModel):
    api_key: StrictStr
    api_version: StrictStr = 'v3'
    base_url: HttpUrl = "https://api.congress.gov/"
    response_format: Union[Literal('json'), Literal('xml')] = "json"