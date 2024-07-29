# Model load module. 

from tensorflow.python.client import device_lib


def get_device_type():
    device_info = device_lib.list_local_devices()[0]

    # If device type is CPU, return False
    if device_info == "CPU":
        return False
    else:
        return True
    
