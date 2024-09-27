import json
import os
from typing import Literal,Annotated
import random

def is_port_authorized_impl(system_name, port_number) -> str:
    # Simulated port authorization check
    port_authorized = random.choice([True, False])
    return f"Port {port_number} on {system_name} authorized: {port_authorized}"