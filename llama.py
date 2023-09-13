#!/usr/bin/env python
# -*- coding: utf-8 -*-


from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained("../../llama-2-7b-chat.ggmlv3.q8_0.bin", model_type="llama")


user_input = input("Ask: ")

response = llm(user_input or "AI is going to")

print(f'Response: {response=}')
