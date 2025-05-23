import requests # type: ignore

url = "https://api.github.com/"
response = requests.get(url)

if response.status_code == 200:
    devices = response.json()
    print(devices)
else:
    print("Failed to get devices")