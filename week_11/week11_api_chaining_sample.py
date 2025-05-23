# API chaining is the process of using the output of one API call as the input to the next. 
# Often done in Python, Postman, or CI/CD tools.

token = get_auth_token()
device_list = get_devices(token)
for device in device_list:
    update_config(device['id'], token)
