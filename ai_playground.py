import sys

import streamlit as st
from streamlit import runtime
from streamlit.web import cli as stcli


def app():
  st.title("Welcome to the AI Playground!")
  st.write("This is a sample Streamlit app.")


def main():
  if runtime.exists():
    app()
  else:
    sys.argv = ["streamlit", "run", sys.argv[0]]
    sys.exit(stcli.main())


if __name__ == "__main__":
  main()
