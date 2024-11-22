import requests
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context
import hashlib
import time


class TLSAdapter(HTTPAdapter):
    def __init__(self, ssl_version=None, **kwargs):
        self.ssl_context = create_urllib3_context(ssl_version=ssl_version)
        super().__init__(**kwargs)

    def init_poolmanager(self, *args, **kwargs):
        kwargs["ssl_context"] = self.ssl_context
        return super().init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        kwargs["ssl_context"] = self.ssl_context
        return super().proxy_manager_for(*args, **kwargs)

# Your Marvel API keys
public_key = "02a7bfa50de411fd1df66a52f3664a03"
private_key = "your private key"

# Marvel API base URL
base_url = "https://gateway.marvel.com/v1/public/characters"

# Generate a timestamp and hash for signing the request
timestamp = str(int(time.time()))  # Use current time as timestamp
hash_input = timestamp + private_key + public_key
hash_value = hashlib.md5(hash_input.encode()).hexdigest()
params = {
    "apikey": public_key,
    "ts": timestamp,
    "hash": hash_value,
    "nameStartsWith": "Spider",  # Example query: characters starting with "Spider"
    "limit": 10  # Number of results to return
}
import certifi



# Enforce TLS 1.2
session = requests.Session()
adapter = TLSAdapter()
session.mount("https://", adapter)
try:
    # Use certifi's CA bundle
    response = session.get(base_url, params=params, verify=certifi.where())
    response.raise_for_status()  # Raises an HTTPError if the status code is 4xx/5xx

    # Process the response
    data = response.json()
    if "data" in data and "results" in data["data"]:
        results = data["data"]["results"]
        print("Characters found:")
        for character in results:
            print(f"- {character['name']}")
    else:
        print("No results found.")

except requests.exceptions.RequestException as e:
    print(f"HTTP Request failed: {e}")
except KeyError as e:
    print(f"KeyError: {e}")
