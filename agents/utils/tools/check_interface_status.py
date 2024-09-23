import json
import os
from typing import Literal,Annotated
import random
import autogen
import network_groupchat

@user_proxy.register_for_execution()
@controller.register_for_llm(description="Checks whether the network interface is active or down.")
def check_interface_status(interface: Annotated[str, "Name of the interface to check"]) -> str:
    status = random.choice(["down", "active"])
    return f"Interface {interface} is {status}"