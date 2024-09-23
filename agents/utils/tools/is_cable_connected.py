import json
import os
from typing import Literal,Annotated
import random
import autogen
import network_groupchat

@user_proxy.register_for_execution()
@controller.register_for_llm(description="Checks if the cable is connected to the system.")
def is_cable_connected(system_name: Annotated[str, "Name of the system to check"]) -> str:
    # Simulated cable connection check
    cable_connected = random.choice([True, False])
    return f"Cable connected to {system_name}: {cable_connected}"