#Netmiko example that logs into a Cisco IOS device and runs a basic show command:

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "admin123"
}

connection = ConnectHandler(**device)
output = connection.send_command("show version")
print(output)
connection.disconnect()