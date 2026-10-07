from curl_cffi import requests

from common.exception.exception_extraction import ExtractionException


class FetchByCurlUtil:
    def __init__(self):
        self.fetch_by_curl_error = ExtractionException("Fetch by curl error")

    def fetch_by_curl(self, url, params=None, headers=None):
        """Fetch data from the given URL using curl with optional parameters and headers."""
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise self.fetch_by_curl_error.extraction_error(
                f"Request failed with status code: {response.status_code}"
            )
