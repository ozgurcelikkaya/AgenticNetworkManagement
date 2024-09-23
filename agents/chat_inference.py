import autogen
import network_groupchat

chat_result = user_proxy.initiate_chat(
    manager,
    message=initial_message,
    summary_method="reflection_with_llm",
    max_turns=5,
)

initial_message="""What is memory usage of Device-123?"""