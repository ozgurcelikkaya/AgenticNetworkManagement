import json
import os
from typing import Literal,Annotated
import random
import autogen
from dotenv import load_dotenv
from agents.utils.tools.check_interface_status import check_interface_status_impl
from agents.utils.tools.get_memory_usage import get_memory_usage_impl
from agents.utils.tools.get_most_cpu import get_most_cpu_impl
from agents.utils.tools.is_cable_connected import is_cable_connected_impl
from agents.utils.tools.is_firewall_pass_allowed import is_firewall_pass_allowed_impl
from agents.utils.tools.is_port_authorized import is_port_authorized_impl ;

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

config_list = [
    {"api_type": "groq", "model": "llama3-70b-8192", "api_key": GROQ_API_KEY, "cache_seed": None,"use_docker": False}
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
        get_memory_usage(system_name: str) -> str
        is_cable_connected(system_name: str) -> str
        is_port_authorized(system_name: str, port_number: int) -> str
        is_firewall_pass_allowed(system_name: str) -> str
    Before executing any function, outline your reasoning and specify which functions to use.
    Ensure all arguments, especially device names like "Device-123", are correctly referenced and not altered.
    Only use the functions provided above.
    Output the plan as a list of function calls in the following format:
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

@user_proxy.register_for_execution()
@controller.register_for_llm(description="Checks whether the network interface is active or down.")
def check_interface_status(interface: Annotated[str, "Name of the interface to check"]) -> str:
    return check_interface_status_impl(interface)

@user_proxy.register_for_execution()
@controller.register_for_llm(description="Retrieves the current memory usage of the system as a percentage.")
def get_memory_usage(system_name: Annotated[str, "Name of the system to check"]) -> str:
    return get_memory_usage_impl(system_name);

@user_proxy.register_for_execution()
@controller.register_for_llm(description="Returns the system that has used the most CPU today.")
def get_most_cpu() -> str:
    return get_most_cpu_impl();

@user_proxy.register_for_execution()
@controller.register_for_llm(description="Checks if the cable is connected to the system.")
def is_cable_connected(system_name: Annotated[str, "Name of the system to check"]) -> str:
    return is_cable_connected_impl(system_name)

@user_proxy.register_for_execution()
@controller.register_for_llm(description="Checks if there is permission to pass through the firewall.")
def is_firewall_pass_allowed(system_name: Annotated[str, "Name of the system to check"]) -> str:
    return is_firewall_pass_allowed_impl(system_name)

@user_proxy.register_for_execution()
@controller.register_for_llm(description="Checks if the specified port is authorized for use.")
def is_port_authorized(system_name: Annotated[str, "Name of the system to check"],
                       port_number: Annotated[int, "Port number to check"]) -> str:
    return is_port_authorized_impl(system_name, port_number);

chat_result = user_proxy.initiate_chat(
    manager,
    message=initial_message,
    summary_method="reflection_with_llm",
    max_turns=5,
)

initial_message="""What is memory usage of Device-123?"""