#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ctransformers import AutoModelForCausalLM


def main():
    model = "models/Wizard-Vicuna-7B-Uncensored.Q8_0.gguf"

    print(f"[+] Loading model: {model}")

    llm = AutoModelForCausalLM.from_pretrained(
        model,
        model_type="llama",
        # config={
        #     'n_gqa': 8,
        #     'max_new_tokens': 512,
        #     # 'temperature': 0.01
        # }
    )

    user_input = input("Ask: ")

    response = llm(user_input or "AI is going to")
    print(f"Response: {response=}")

    return response


if __name__ == "__main__":
    main()
