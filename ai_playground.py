import os

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
    dirname = os.path.dirname(__file__)
    app_file = os.path.join(dirname, "ai_playground.py")

    conf = {
      # "server.fileWatcherType": "none",
      "server.port": config.SERVER_PORT,
      "server.headless": config.SERVER_HEADLESS,
      "theme.base": "light",
      "browser.gatherUsageStats": False,
    }
    stcli.bootstrap.load_config_options(conf)
    stcli.bootstrap.run(app_file, False, args=[], flag_options=[])


if __name__ == "__main__":
  main()
