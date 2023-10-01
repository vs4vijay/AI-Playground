#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from litellm import completion

os.environ["OPENAI_API_KEY"] = "<OPEN_AI_KEY>"
os.environ["COHERE_API_KEY"] = "<COHERE_KEY>"

messages = [{"content": "Hello, how are you?", "role": "user"}]

# openai call
response = completion(model="gpt-3.5-turbo", messages=messages)

# cohere call
response = completion("command-nightly", messages)

print(f"{response=}")
