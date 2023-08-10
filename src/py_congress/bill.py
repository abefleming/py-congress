from client import HTTPClient
from py_congress.models.config import PyCongressConfig

class Bill:
    def __init__(self, 
                 config: PyCongressConfig
                 ):
        self.config = config
        self.http_client = HTTPClient(self.config.base_url)
        
