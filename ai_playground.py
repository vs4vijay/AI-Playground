import os

import streamlit as st
from streamlit import runtime
from streamlit.web import cli as stcli

from .config import config


def init_chat():
  if "messages" not in st.session_state:
    st.session_state.messages = []


def render_chat():
  with st.chat_message("user"):
    st.write("Hello 👋")

  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  if prompt := st.chat_input("Write here..."):
    with st.chat_message("user"):
      st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # TODO: Call the LLM API to get a response
    response = f"Echo: {prompt}"
    with st.chat_message("assistant"):
      st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})


def app():
  st.set_page_config(
    page_title="AI Playground",
    page_icon="🧠",
  )

  init_chat()

  st.title("Welcome to the AI Playground!")
  st.write("This is a sample Streamlit app.")

  render_chat()


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
      "browser.gatherUsageStats": False,
      "theme.base": "light",
      # "theme.primaryColor": "#000000",
      # "theme.backgroundColor": "#000000",
      # "theme.secondaryBackgroundColor": "#333333",
      # "theme.textColor": "#00FF00",
    }
    stcli.bootstrap.load_config_options(conf)
    stcli.bootstrap.run(app_file, False, args=[], flag_options=[])


if __name__ == "__main__":
  main()
