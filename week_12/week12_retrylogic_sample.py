#Sometimes network devices or APIs fail temporarily. Retry a few times before giving up.

from tenacity import retry, stop_after_attempt, wait_fixed

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_device_data():
    response = requests.get("https://device/api")
    response.raise_for_status()
    return response.json()
