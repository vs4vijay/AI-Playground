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
wget -c https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q8_0.gguf
wget -c https://huggingface.co/TheBloke/Mistral-7B-OpenOrca-GGUF/resolve/main/mistral-7b-openorca.Q8_0.gguf

wget -c https://huggingface.co/TheBloke/Wizard-Vicuna-7B-Uncensored-GGUF/resolve/main/Wizard-Vicuna-7B-Uncensored.Q8_0.gguf

wget -c https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF/resolve/main/codellama-7b-instruct.Q8_0.gguf

---


## Try with LLaMA.cpp

- Extract LLaMA.cpp zip to bin/ directory 

```bash

./bin/main.exe -m models/llama-2-7b-chat.Q8_0.gguf
```

## Try with vLLM

```bash
pip install -U vllm

python -u -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --model mistralai/Mistral-7B-v0.1
```

## Try with FastChat

```bash
pip install -U fastchat

python -m fastchat.serve.openai_api_server --host localhost --port 8000
```

## Try with LeptonAI

```bash
pip install -U leptonai


```

## Try with ollama

```bash

echo "FROM ./models/llama-2-13b-chat.Q5_K_M.gguf" > llama-2-13b-chat.Modelfile

ollama create llama2-13b-chat -f ./llama-2-13b-chat.Modelfile

ollama run llama2-13b-chat


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
openplayground run

ollama run mistral

pip install -U jina

Ray Serve
pip install "ray[serve]"
https://github.com/ray-project/ray-llm

txtai

MLC AI - https://mlc.ai/package/
pip install --pre --force-reinstall mlc-ai-nightly mlc-chat-nightly -f https://mlc.ai/wheels
python -m mlc_chat.rest 

OpenLLM


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

Later:
https://github.com/Arize-ai/phoenix
https://github.com/explodinggradients/ragas
https://github.com/trypromptly/LLMStack


Q5_K_M


```
 
