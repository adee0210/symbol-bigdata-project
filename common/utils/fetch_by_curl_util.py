from curl_cffi import requests


class FetchByCurlError(Exception):
    pass


class FetchByCurlUtil:
    @staticmethod
    def fetch_by_curl(url, params=None, headers=None):
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise FetchByCurlError(
                f"Request failed with status code {response.status_code}"
            )
