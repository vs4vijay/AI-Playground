import os

class Config:
    AZURE_OPENAI_DEPLOYMENT_NAME = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "vs4vijay-gpt-35")
    AZURE_OPENAI_API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_API_BASE = os.environ.get("AZURE_OPENAI_API_BASE")

config = Config()