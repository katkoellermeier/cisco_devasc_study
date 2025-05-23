# Week 2 Lab: Python Functions + SDLC
# Author: [Kat Koellermeier]
# Purpose: Learn how to write and use Python functions for modular, reusable code. Understand how modern software development workflows (like Agile, DevOps, CI/CD) relate to network automation projects.
#Lab: Write a Python function that: Accepts a hostname and IP, Returns a formatted string with device status, Create another function that takes a list of devices and calls the status function for each

# Device Info
device_name = "R1"
ip_address = "192.168.0.1"
is_active = True

# Print basic info
print("Device Name:", device_name)
print("IP Address:", ip_address)

# Check device status
if is_active:
    print(f"{device_name} is currently UP.")
else:
    print(f"{device_name} is currently DOWN.")

# List of devices
devices = ["R1", "R2", "SW1", "SW2"]

# Iterate through devices and simulate pinging each
print("\nPinging all devices in the list:")
for device in devices:
    print(f"Pinging {device}... Success!")

# Example dictionary of devices and their statuses
device_status = {
    "R1": True,
    "R2": False,
    "SW1": True,
    "SW2": False
}

# Report the status of each device
print("\nDevice Status Report:")
for name, status in device_status.items():
    state = "UP" if status else "DOWN"
    print(f"{name} is {state}")