import json
import os
from typing import Literal,Annotated
import random
import autogen
import network_groupchat

@user_proxy.register_for_execution()
@controller.register_for_llm(description="Checks if there is permission to pass through the firewall.")
def is_firewall_pass_allowed(system_name: Annotated[str, "Name of the system to check"]) -> str:
    # Simulated firewall permission check
    firewall_pass_allowed = random.choice([True, False])
    return f"Firewall pass permission for {system_name}: {firewall_pass_allowed}"
