# AI-Playground

---

## Use StarCoder

pip install transformers
pip install torch torchvision
pip install accelerate bitsandbytes
pip install accelerate[torch]

Edit:
- `load_in_8bit=True`

python starcoder.py
- will download ~60 GB of model

## Models

- LLaMa 2 - https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF


wget -c https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q8_0.gguf
wget -c https://huggingface.co/TheBloke/Wizard-Vicuna-7B-Uncensored-GGUF/resolve/main/Wizard-Vicuna-7B-Uncensored.Q8_0.gguf

---


## Try with LLaMa.cpp

- Extract zip to bin/ directory 


```bash

./bin/main.exe -m models/llama-2-7b-chat.Q8_0.gguf


```

## Try with vLLM

```bash
pip install vllm

python -u -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --model mistralai/Mistral-7B-v0.1
```

---

## Specs

RAM Required:

| Model Size | RAM Required |
|------------|--------------|
| 3B         | 8 GB         |
| 7B         | 16 GB        |
| 13B        | 32 GB        |


---

### Development Notes

```bash

pip install pyautogen

pip install openplayground

ollama run mistral


https://github.com/FlowiseAI/Flowise


wget https://gpt4all.io/models/ggml-gpt4all-j.bin -O models/ggml-gpt4all-j

https://github.com/go-skynet/LocalAI
docker pull quay.io/go-skynet/local-ai:latest

nlpcloud

curl "https://api.nlpcloud.io/v1/<model_name>/entities" \
  -H "Authorization: Token <token>" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{"text":"John Doe has been working for Microsoft in Seattle since 1999."}'


https://github.com/microsoft/semantic-kernel
https://github.com/microsoft/guidance


https://skypilot.readthedocs.io/

```
