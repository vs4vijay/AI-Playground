import sys
import os

import streamlit as st
from streamlit import runtime

from streamlit import config
from streamlit.web import cli as stcli

from .config import config


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
    # config.set_option("server.headless", config.SERVER_HEADLESS)
    
    # conf = {
    #     "server.fileWatcherType": "none",
    #     "server.headless": True,
    #     "theme.base": "light",
    #     'browser.gatherUsageStats': False,
    # }
    # streamlit.bootstrap.load_config_options(flag_options=conf)
    # streamlit.bootstrap.run(fname, "", args=[], flag_options={})
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'ai_playground.py')

    sys.argv = [
      "streamlit", "run", filename, 
      "--server.port", str(config.SERVER_PORT),
      "--server.headless", str(config.SERVER_HEADLESS),
      "--browser.gatherUsageStats=False"]
    sys.exit(stcli.main())


if __name__ == "__main__":
  main()
