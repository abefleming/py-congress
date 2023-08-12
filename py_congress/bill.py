from urllib.parse import urlparse
from py_congress.client import HTTPClient
from py_congress.config import *
from py_congress.models.bill import *
from py_congress.models.common import *

class Bill:
    def __init__(self, config: PyCongressConfig):
        self.config = config
        self.http_client = HTTPClient(base_url=full_endpoint(self.config))
        self.headers = {"x-api-key": self.config.api_key}
        self.allowed_billtypes = [
            "hr",
            "s",
            "hjres",
            "sjres",
            "hcones",
            "sconres",
            "hres",
            "sres",
        ]
        self.enabled_endpoints = [
            "actions",
            "amendments",
            "committees",
            "cosponsors",
            "relatedbills",
            "subjects",
            "summaries",
            "text",
            "titles",
        ]
        self.section_to_model = {
            "actions": BillActions,
            "amendments": BillAmendments,
            "committees": BillCommittees,
            "cosponsors": BillCosponsors,
            "relatedbills": BillRelatedBills,
            "subjects": BillSubjects,
            "summaries": BillSummaries,
            "text": BillText,
            "titles": BillTitles,
        }
    def get_bills(
        self,
        congress: int = None,
        billtype: str = None,
        limit: int = None,
        fromDateTime: str = None,
        toDateTime: str = None,
        sort: str = None,
        offset: int = 0,
    ) -> Union[BaseBillResponse, CongressApiError]:
        """Returns a list of bills sorted by date of latest action. Supports filtering by a specified congress and bill type.
           Use this if you're accessing any of these endpoints:
           - /bill
           - /bill/:congress
           - /bill/:congress/:billType
        Args:
            congress (int, optional): The congress number. For example, the value can be 117. Defaults to None.
            billtype (str, optional): The type of bill. Value can be hr, s, hjres, sjres, hconres, sconres, hres, or sres. Defaults to None.
            limit (int, optional): The number of records returned. The maximum limit is 250. Defaults to None.
            fromDateTime (str, optional): The starting timestamp to filter by update date. Use format: YYYY-MM-DDT00:00:00Z. Defaults to None.
            toDateTime (str, optional): The ending timestamp to filter by update date. Use format: YYYY-MM-DDT00:00:00Z. Defaults to None.
            sort (str, optional): Sort by update date in Congress.gov. Value can be updateDate+asc or updateDate+desc. Defaults to None.
            offset (int, optional): The starting record returned. 0 is the first record. Defaults to 0.

        Returns:
            Union[BaseBillResponse, CongressApiError]: Formatted response or error message
        """
        params = {
            "format": self.config.response_format,
            "limit": limit,
            "fromDateTime": fromDateTime,
            "toDateTime": toDateTime,
            "sort": sort,
            "offset": offset,
        }
        headers = self.headers

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
            return CongressApiError(**response.json())

    def get_bill(
        self,
        url: HttpUrl = None,
        congress: int = None,
        billType: str = None,
        billNumber: int = None,
        section: str = None,
    ) -> Union[BaseBillResponse, CongressApiError]:
        """_summary_

        Args:
            url (HttpUrl, optional): _description_. Defaults to None.
            congress (int, optional): _description_. Defaults to None.
            billType (str, optional): _description_. Defaults to None.
            billNumber (int, optional): _description_. Defaults to None.

        Returns:
            Union[BaseBillResponse, CongressApiError]: _description_
        """
        response_model = BillNumber
        if url:
            try:
                _path = urlparse(url).path[1:]
                _path_parts = _path.split('/')
                _version = _path_parts[0]
                _base_resource = _path_parts[1]
                _congress = _path_parts[2]
                _billType = _path_parts[3]
                _billNumber = _path_parts[4]
                _section = _path_parts[5]
                print(_path_parts)
            except Exception:
                raise ValueError("URL provided is not from /bill/:congress/:billType/:billNumber")
            if _version != self.config.api_version:
                raise ValueError("API version does not match configuration")
            if _base_resource != 'bill':
                raise ValueError("Only endpoints from /bill/:congress/:billType/:billNumber are supported")
            if _section and _section not in self.enabled_endpoints:
                raise UnsupportedActionError(f"{_section} is not available to use through this client.")
            endpoint = _path.split("v3/")[1]
            response_model = self.section_to_model[_section]
        elif section and congress and billType and billNumber:
            endpoint = f"/bill/{congress}/{billType}/{billNumber}/{section}"
            response_model = self.section_to_model[section]
        elif congress and billType and billNumber:
            endpoint = f"/bill/{congress}/{billType}/{billNumber}"
        else:
            raise MissingArgumentsError("One or more arguments are missing.")

        params = {
            "format": self.config.response_format,
        }
        headers = self.headers
        response = self.http_client.get(endpoint, params=params, headers=headers)
        if response.ok:
            return response_model(**response.json())
        else:
            return CongressApiError(**response.json())