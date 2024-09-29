from typing import Literal,Annotated
import random

def check_interface_status_impl(switch, interface) -> str:
    status = random.choice(["down", "active"])
    return f"Status of interface {interface} of switch {switch} is {status}"