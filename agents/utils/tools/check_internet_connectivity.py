import json
import os
from typing import Literal,Annotated
import random
import autogen
import network_groupchat

@user_proxy.register_for_execution()
@controller.register_for_llm(description="Verifies that the device can connect to the internet.")
def check_internet_connectivity(device_name: Annotated[str, "Name of the device to check"]) -> str:
    # Default simulated result: device is connected
    connected_devices = ["Device-123", "Device-456", "Device-789"]
    
    if device_name in connected_devices:
        return f"{device_name} is connected to the internet."
    else:
        return f"{device_name} is not connected to the internet."