#!/usr/bin/env python

# pip install pyautogen

import os

from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample


load_dotenv()

config_list = [
    {
        "api_type": "azure",
        # "model": "gpt-3.5-turbo",
        "model": os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "vs4vijay-gpt-35"),
        "api_key": os.environ.get("AZURE_OPENAI_API_KEY"),
        "api_base": os.environ.get("AZURE_OPENAI_API_BASE"),
        "api_version": "2023-07-01-preview",
    },
]


def main():
    print("[+] Starting Autogen")
    print(f"{config_list=}")

    assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
    user_proxy = UserProxyAgent(
        "user_proxy", code_execution_config={"work_dir": "code"}
    )

    user_instructions = (
        input("Enter your instructions: ")
        or "Plot a chart of NVDA and TESLA stock price change YTD."
    )
    user_proxy.initiate_chat(assistant, message=user_instructions)
    # This initiates an automated chat between the two agents to solve the task


if __name__ == "__main__":
    main()
