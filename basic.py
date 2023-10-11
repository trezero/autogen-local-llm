from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Import the openapi key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# Create assistat agent
assistant = AssistantAgent(name="assistant",llm_config={"config_list": config_list})

# Create a user proxy agent
user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config={"work_dir": "coding"})

# Start the conversation
user_proxy.initiate_chat(
    assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")