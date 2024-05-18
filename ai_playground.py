import sys

import streamlit as st
from streamlit import runtime
from streamlit.web import cli as stcli

from config import config


def app():
  st.set_page_config(
    page_title="AI Playground",
    page_icon="🧠",
  )
  st.title("Welcome to the AI Playground!")
  st.write("This is a sample Streamlit app.")


def main():
  if runtime.exists():
    app()
  else:
    sys.argv = ["streamlit", "run", "ai_playground.py", "--server.port", str(config.SERVER_PORT)]
    sys.exit(stcli.main())


if __name__ == "__main__":
  main()
