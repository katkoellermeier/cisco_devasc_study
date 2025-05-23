# When polling dozens or hundreds of devices, serial code is too slow.
# Use threading or concurrent.futures.ThreadPoolExecutor to run commands in parallel.

from concurrent.futures import ThreadPoolExecutor
from netmiko import ConnectHandler

devices = [ {...}, {...}, {...} ]  # List of Cisco devices

def get_version(device):
    try:
        conn = ConnectHandler(**device)
        output = conn.send_command("show version")
        print(f"{device['host']} → SUCCESS")
        conn.disconnect()
    except Exception as e:
        print(f"{device['host']} → ERROR: {e}")

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(get_version, devices)
