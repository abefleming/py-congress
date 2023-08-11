from py_congress.client import HTTPClient
from py_congress.config import *
from py_congress.models.bill import *

class Bill:
    def __init__(self, 
                 config: PyCongressConfig
                 ):
        self.config = config
        self.http_client = HTTPClient(base_url=full_endpoint(self.config))
        self.allowed_billtypes = ["hr", "s", "hjres", "sjres", "hcones", "sconres", "hres", "sres"]

    def get_bills(self, 
                  congress: int=None, 
                  billtype: str=None, 
                  limit: int=None, 
                  fromDateTime: str=None,
                  toDateTime: str=None,
                  sort: str=None,
                  offset: int=0, 
                  ):
        """Returns a list of bills sorted by date of latest action.

        Args:
            congress (int, optional): The congress number. For example, the value can be 117. Defaults to None.
            billtype (str, optional): The type of bill. Value can be hr, s, hjres, sjres, hconres, sconres, hres, or sres. Defaults to None.
            limit (int, optional): The number of records returned. The maximum limit is 250. Defaults to None.
            fromDateTime (str, optional): The starting timestamp to filter by update date. Use format: YYYY-MM-DDT00:00:00Z. Defaults to None.
            toDateTime (str, optional): The ending timestamp to filter by update date. Use format: YYYY-MM-DDT00:00:00Z. Defaults to None.
            sort (str, optional): Sort by update date in Congress.gov. Value can be updateDate+asc or updateDate+desc. Defaults to None.
            offset (int, optional): The starting record returned. 0 is the first record. Defaults to 0.

        Returns:
            _type_: _description_
        """
        params = {
            "format": self.config.response_format,
            "limit": limit, 
            "fromDateTime": fromDateTime,
            "toDateTime": toDateTime,
            "sort": sort,
            "offset": offset,
        }
        headers = {
            "x-api-key": self.config.api_key
        }
        if congress:
            endpoint = f"/bill/{congress}"
        if congress and billtype:
            endpoint = f"/bill/{congress}/{billtype}"
        else:
            endpoint = "/bill"
        response = self.http_client.get(endpoint, params=params, headers=headers)
        if response.ok:
            return BillListResponse(**response.json())
        else:
            response.text
