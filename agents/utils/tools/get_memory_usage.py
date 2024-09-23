import json
import os
from typing import Literal,Annotated
import random
import autogen
import network_groupchat

@user_proxy.register_for_execution()
@controller.register_for_llm(description="Retrieves the current memory usage of the system as a percentage.")
def get_memory_usage(system_name: Annotated[str, "Name of the system to check"]) -> str:
    # Simulated memory usage percentage
    memory_usage = random.uniform(0, 100)
    return f"{system_name} memory usage: {memory_usage:.2f}%"