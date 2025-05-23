# Many modern platforms expose monitoring via REST APIs:
# Meraki: /devices/{serial}/lossAndLatencyHistory
# DNA Center: /dna/intent/api/v1/client-health
# Webex: /metrics

import requests
headers = {"X-Cisco-Meraki-API-Key": "YOUR_API_KEY"}
url = "https://api.meraki.com/api/v1/networks/123/devices"
response = requests.get(url, headers=headers)
print(response.json())
