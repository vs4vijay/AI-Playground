#!/usr/bin/env python
# -*- coding: utf-8 -*-

from litellm import completion
import json

# set ENV variables
os.environ["OPENAI_API_KEY"] = "openai key"
os.environ["COHERE_API_KEY"] = "cohere key"

messages = [{"content": "Hello, how are you?", "role": "user"}]

# openai call
response = completion(model="gpt-3.5-turbo", messages=messages)

# cohere call
response = completion("command-nightly", messages)

print(f"{response=}")
