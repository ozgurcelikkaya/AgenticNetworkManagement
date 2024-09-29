from typing import Literal,Annotated
import random

def get_memory_usage_impl(device_name) -> str:
    # Simulated memory usage percentage
    memory_usage = random.uniform(0, 100)
    return f"{device_name} memory usage: {memory_usage:.2f}%"