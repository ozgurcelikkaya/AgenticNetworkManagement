from typing import Literal,Annotated
import random

def get_memory_usage_impl(system_name: Annotated[str, "Name of the system to check"]) -> str:
    # Simulated memory usage percentage
    memory_usage = random.uniform(0, 100)
    return f"{system_name} memory usage: {memory_usage:.2f}%"