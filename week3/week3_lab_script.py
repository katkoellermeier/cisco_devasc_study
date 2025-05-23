import json

data = '{"hostname": "R1", "ip": "192.168.1.1", "status": "up"}'
parsed = json.loads(data)
print(parsed["hostname"])  # Output: R1