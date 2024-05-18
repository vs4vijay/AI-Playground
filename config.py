import os

class Config:
    # Server config
    SERVER_PORT = os.environ.get("SERVER_PORT", 4100)

    # OpenAI config
    AZURE_OPENAI_DEPLOYMENT_NAME = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "vs4vijay-gpt-35")
    AZURE_OPENAI_API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_API_BASE = os.environ.get("AZURE_OPENAI_API_BASE")

config = Config()