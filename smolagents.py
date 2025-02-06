# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "smolagents",
# ]
# ///
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel


def main():
  print("[+] Running SmolAgents")
  agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

  # agent = CodeAgent()
  # agent.add_tool(DuckDuckGoSearchTool())
  # agent.add_tool(HfApiModel())
  # agent.run()

  agent.run("Tell me joke about Git")


if __name__ == "__main__":
  main()
