import json
import os
from typing import Literal,Annotated
import random
import autogen

config_list = [
    {"api_type": "groq", "model": "llama3-70b-8192", "api_key": "A P I K E Y", "cache_seed": None,"use_docker": False}
]

initial_message="""Why I can not connect internet with device Device-123?"""

user_proxy = autogen.ConversableAgent(
    name="User",
    system_message="""
    For NETWORK STATUS and NETWORK TROUBLESHOOTING tasks:
    - Before executing any function, explain your reasoning and specify which function you will use.
    - Only use the functions you have been provided with.
    - Observe Planner Agent's plan and Summarize it as a plan.
    - Output 'TERMINATE' when an answer has been provided.
    """,
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
    llm_config={"config_list": config_list},
    code_execution_config={"use_docker": False},  # Disable Docker for code execution
)
planner = autogen.ConversableAgent(
    name="Planner",
    system_message="""You are a planner responsible for creating a detailed plan to solve tasks.
    Available Functions:
        check_internet_connectivity(device_name: str) -> str
        get_memory_usage(system_name: str) -> str
        is_cable_connected(system_name: str) -> str
        is_port_authorized(system_name: str, port_number: int) -> str
        is_firewall_pass_allowed(system_name: str) -> str
    Before executing any function, outline your reasoning and specify which functions to use.
    Ensure all arguments, especially device names like "Device-123", are correctly referenced and not altered.
    Only use the functions provided above.
    Output the plan as a list of function calls in the following format:
        check_internet_connectivity("Device-123")
        get_memory_usage("Device-123")
        is_cable_connected("Device-123")
        is_port_authorized("Device-123", 8080)
        is_firewall_pass_allowed("Device-123")
Output once the plan is ready.
""",
    llm_config={"config_list": config_list},
)
controller = autogen.ConversableAgent(
    name="Controller",
    system_message="""You are a controller responsible for controlling the plan and its execution. 
    Write everything from User Proxy as a plan.""",
    llm_config={"config_list": config_list},
)


groupchat = autogen.GroupChat(agents=[user_proxy, planner, controller], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list})
