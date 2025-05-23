# Use try/except blocks to avoid script crashes when a device times out or an API fails.

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as err:
    print(f"HTTP error: {err}")