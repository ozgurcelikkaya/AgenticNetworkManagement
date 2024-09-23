import json
import os
from typing import Literal,Annotated
import random
import autogen
import network_groupchat

@user_proxy.register_for_execution()
@controller.register_for_llm(description="Checks if the specified port is authorized for use.")
def is_port_authorized(system_name: Annotated[str, "Name of the system to check"],
                       port_number: Annotated[int, "Port number to check"]) -> str:
    # Simulated port authorization check
    port_authorized = random.choice([True, False])
    return f"Port {port_number} on {system_name} authorized: {port_authorized}"