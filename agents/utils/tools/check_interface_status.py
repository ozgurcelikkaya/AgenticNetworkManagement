from typing import Literal,Annotated
import random

def check_interface_status_impl(interface) -> str:
    status = random.choice(["down", "active"])
    return f"Interface {interface} is {status}"