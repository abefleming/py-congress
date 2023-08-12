from requests import Session
from urllib3.util import Retry
from urllib.parse import urljoin
from requests.adapters import HTTPAdapter
from requests.models import Response


class HTTPClient:
    """Base HTTP client with custom Session configuration."""

    def __init__(self, base_url: str = None):
        # TODO: Expose additional retry configuration to the user.
        self.base_url = base_url
        self.session = Session()
        retries = Retry(
            total=3,
            backoff_factor=0.5,
        )
        self.session.mount(base_url, HTTPAdapter(max_retries=retries))

    def get(self, endpoint: str = None, *args, **kwargs) -> Response:
        """Basic GET wrapper to use custom Session configuration

        Args:
            endpoint (str, optional): Endpoint to add onto the base url for API request. Defaults to None.

        Raises:
            ValueError: Raises when no value for endpoint is provided. Expecting

        Returns:
            Response: Response object that contains the server's response to the HTTP request
        """
        if not endpoint:
            raise ValueError(
                "No endpoint provided for GET request. Example: /bill, /ammendment"
            )
        if not endpoint.startswith("/"):
            endpoint = f"/{endpoint}"
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url=url, *args, **kwargs)
