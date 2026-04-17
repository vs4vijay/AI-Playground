"""
DeepAgents Example - Batteries-included agent harness built with LangChain and LangGraph.

This example demonstrates:
1. Basic agent creation and invocation
2. Custom model configuration (Azure OpenAI / OpenAI)
3. Adding custom tools
4. Streaming output
5. Sub-agent delegation patterns

Setup:
    pip install deepagents
    # Set OPENAI_API_KEY or AZURE_OPENAI_API_KEY environment variable

Usage:
    python deepagents_example.py
"""

from __future__ import annotations

import asyncio
import os
from typing import Annotated

from deepagents import create_deep_agent
from langchain_core.tools import tool
from langchain_openai import AzureChatOpenAI, ChatOpenAI


def example_1_basic_agent() -> None:
    """Example 1: Basic agent with default settings.
    
    The agent comes with built-in tools:
    - write_todos: Planning and task breakdown
    - read_file, write_file, edit_file: Filesystem operations
    - ls, glob, grep: File discovery
    - execute: Shell commands (sandboxed)
    - task: Sub-agent delegation
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 1: Basic Agent")
    print("=" * 60)
    
    agent = create_deep_agent()
    
    result = agent.invoke({
        "messages": [{
            "role": "user", 
            "content": "Create a simple Python hello world script and save it to hello_deepagents.py"
        }]
    })
    
    # Extract the final response
    final_message = result["messages"][-1]
    print(f"\nAgent response:\n{final_message.content}")


def example_2_custom_model() -> None:
    """Example 2: Using a custom model (Azure OpenAI or OpenAI)."""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Custom Model Configuration")
    print("=" * 60)
    
    # Try Azure OpenAI first, fall back to OpenAI
    if os.environ.get("AZURE_OPENAI_API_KEY"):
        print("Using Azure OpenAI...")
        model = AzureChatOpenAI(
            azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o"),
            api_version="2024-02-15-preview",
            temperature=0,
        )
    elif os.environ.get("OPENAI_API_KEY"):
        print("Using OpenAI...")
        model = ChatOpenAI(model="gpt-4o", temperature=0)
    else:
        print("No API key found, using default model configuration...")
        model = None
    
    agent = create_deep_agent(
        model=model,
        system_prompt="You are a helpful research assistant. Be concise and thorough.",
    )
    
    result = agent.invoke({
        "messages": [{
            "role": "user", 
            "content": "What are the main features of LangGraph? List 3-5 key features."
        }]
    })
    
    final_message = result["messages"][-1]
    print(f"\nAgent response:\n{final_message.content}")


def example_3_custom_tools() -> None:
    """Example 3: Adding custom tools to the agent."""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Custom Tools")
    print("=" * 60)
    
    @tool
    def get_weather(
        location: Annotated[str, "City name, e.g., 'San Francisco'"]
    ) -> str:
        """Get the current weather for a location (simulated)."""
        # Simulated weather data
        weather_data = {
            "san francisco": "68°F, Partly Cloudy",
            "new york": "55°F, Clear",
            "london": "52°F, Rainy",
            "tokyo": "72°F, Sunny",
        }
        return weather_data.get(
            location.lower(), 
            f"Weather data not available for {location}. Try: San Francisco, New York, London, or Tokyo."
        )
    
    @tool
    def calculate(
        expression: Annotated[str, "Mathematical expression to evaluate, e.g., '2 + 2'"]
    ) -> str:
        """Evaluate a mathematical expression."""
        try:
            # Safe evaluation of simple math expressions
            result = eval(expression, {"__builtins__": {}}, {})
            return f"Result: {result}"
        except Exception as e:
            return f"Error evaluating expression: {e}"
    
    agent = create_deep_agent(
        tools=[get_weather, calculate],
        system_prompt="You are a helpful assistant with access to weather and calculator tools.",
    )
    
    result = agent.invoke({
        "messages": [{
            "role": "user", 
            "content": "What's the weather in Tokyo? Also, what is 15 * 7 + 3?"
        }]
    })
    
    final_message = result["messages"][-1]
    print(f"\nAgent response:\n{final_message.content}")


def example_4_planning_and_files() -> None:
    """Example 4: Planning and file operations.
    
    DeepAgents includes a planning tool (write_todos) that helps break down
    complex tasks into manageable steps.
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Planning and File Operations")
    print("=" * 60)
    
    agent = create_deep_agent()
    
    # The agent can plan, read/write files, and track progress
    result = agent.invoke({
        "messages": [{
            "role": "user", 
            "content": """
            Create a simple project structure for a Python CLI tool:
            1. Create a project directory called 'my_cli_tool'
            2. Create a main.py with a basic click CLI
            3. Create a README.md with usage instructions
            4. Create a requirements.txt with click dependency
            """
        }]
    })
    
    final_message = result["messages"][-1]
    print(f"\nAgent response:\n{final_message.content}")


def example_5_streaming() -> None:
    """Example 5: Streaming output for real-time responses."""
    print("\n" + "=" * 60)
    print("EXAMPLE 5: Streaming Output")
    print("=" * 60)
    
    agent = create_deep_agent()
    
    print("\nStreaming response:\n")
    
    # Stream the response token by token
    for chunk in agent.stream({
        "messages": [{
            "role": "user", 
            "content": "Write a haiku about artificial intelligence."
        }]
    }):
        # Extract and print text content from chunks
        if hasattr(chunk, "content"):
            print(chunk.content, end="", flush=True)
        elif isinstance(chunk, dict):
            # Handle dict-formatted chunks
            if "agent" in chunk:
                messages = chunk["agent"].get("messages", [])
                for msg in messages:
                    if hasattr(msg, "content") and msg.content:
                        print(msg.content, end="", flush=True)
    
    print("\n")


async def example_6_async_streaming() -> None:
    """Example 6: Async streaming for better performance."""
    print("\n" + "=" * 60)
    print("EXAMPLE 6: Async Streaming")
    print("=" * 60)
    
    agent = create_deep_agent()
    
    print("\nAsync streaming response:\n")
    
    # Async streaming
    async for chunk in agent.astream({
        "messages": [{
            "role": "user", 
            "content": "Explain what LangGraph is in 2-3 sentences."
        }]
    }):
        if isinstance(chunk, dict) and "agent" in chunk:
            messages = chunk["agent"].get("messages", [])
            for msg in messages:
                if hasattr(msg, "content") and msg.content:
                    print(msg.content, end="", flush=True)
    
    print("\n")


def example_7_research_agent() -> None:
    """Example 7: A research-focused agent configuration."""
    print("\n" + "=" * 60)
    print("EXAMPLE 7: Research Agent Configuration")
    print("=" * 60)
    
    agent = create_deep_agent(
        system_prompt="""You are a thorough research assistant with access to filesystem tools.

Your workflow:
1. Break down research tasks using write_todos
2. Create organized notes and summaries in files
3. Use sub-agents (task tool) for parallel research when appropriate
4. Always cite sources and provide structured outputs

Be methodical and comprehensive in your research.""",
    )
    
    result = agent.invoke({
        "messages": [{
            "role": "user", 
            "content": """
            Research and summarize the key differences between:
            - LangChain
            - LangGraph
            - LangSmith
            
            Create a comparison file called 'langchain_ecosystem_comparison.md'
            """
        }]
    })
    
    final_message = result["messages"][-1]
    print(f"\nAgent response:\n{final_message.content}")


def example_8_code_assistant() -> None:
    """Example 8: Code assistant with custom system prompt."""
    print("\n" + "=" * 60)
    print("EXAMPLE 8: Code Assistant")
    print("=" * 60)
    
    agent = create_deep_agent(
        system_prompt="""You are an expert Python developer assistant.

Guidelines:
- Write clean, well-documented code
- Follow PEP 8 style guidelines
- Include type hints for function signatures
- Add docstrings to all functions and classes
- Use meaningful variable names
- Consider edge cases and error handling

When writing code, always create the files directly using the file tools.""",
    )
    
    result = agent.invoke({
        "messages": [{
            "role": "user", 
            "content": """
            Create a Python module called 'data_processor.py' with:
            1. A DataProcessor class that can read JSON and CSV files
            2. Methods for filtering, sorting, and aggregating data
            3. Export functionality to JSON, CSV, and Excel formats
            4. Proper error handling and logging
            """
        }]
    })
    
    final_message = result["messages"][-1]
    print(f"\nAgent response:\n{final_message.content}")


def run_all_examples() -> None:
    """Run all examples in sequence."""
    examples = [
        ("Basic Agent", example_1_basic_agent),
        ("Custom Model", example_2_custom_model),
        ("Custom Tools", example_3_custom_tools),
        ("Planning & Files", example_4_planning_and_files),
        ("Streaming", example_5_streaming),
        ("Research Agent", example_7_research_agent),
        ("Code Assistant", example_8_code_assistant),
    ]
    
    print("\n" + "=" * 60)
    print("DEEPAGENTS EXAMPLES")
    print("=" * 60)
    print("\nSelect an example to run:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"  {i}. {name}")
    print(f"  {len(examples) + 1}. Run all examples")
    print(f"  {len(examples) + 2}. Run async streaming example")
    print("  0. Exit")
    
    choice = input("\nEnter your choice (0-{}): ".format(len(examples) + 2))
    
    try:
        choice_num = int(choice)
        if choice_num == 0:
            print("Goodbye!")
            return
        elif 1 <= choice_num <= len(examples):
            name, func = examples[choice_num - 1]
            print(f"\nRunning: {name}")
            func()
        elif choice_num == len(examples) + 1:
            print("\nRunning all examples...")
            for name, func in examples:
                func()
        elif choice_num == len(examples) + 2:
            asyncio.run(example_6_async_streaming())
        else:
            print("Invalid choice. Running basic example...")
            example_1_basic_agent()
    except ValueError:
        print("Invalid input. Running basic example...")
        example_1_basic_agent()


if __name__ == "__main__":
    # Check for API keys
    if not os.environ.get("OPENAI_API_KEY") and not os.environ.get("AZURE_OPENAI_API_KEY"):
        print("Warning: No OpenAI API key found.")
        print("Set OPENAI_API_KEY or AZURE_OPENAI_API_KEY environment variable.")
        print("Some examples may not work without an API key.\n")
    
    run_all_examples()
