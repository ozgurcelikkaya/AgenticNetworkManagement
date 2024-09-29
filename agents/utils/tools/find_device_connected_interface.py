

def find_device_connected_interface_impl(device_name) -> str:
    switch_name = "switch1:123"
    interface = "Ethernet01"
    return "{device_name} known to connected {interface} of {switch_name}"