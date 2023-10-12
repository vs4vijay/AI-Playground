#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ctransformers import AutoModelForCausalLM


def main():
    # model = "../../llama-2-7b-chat.ggmlv3.q8_0.bin"
    model = "models/llama-2-7b-chat.Q8_0.gguf"
    llm = AutoModelForCausalLM.from_pretrained(model, model_type="llama")

    user_input = input("Ask: ")
    response = llm(user_input or "AI is going to")
    print(f"Response: {response=}")
    return response


if __name__ == "__main__":
    main()
