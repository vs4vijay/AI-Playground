# AI-Playground

---

AI Playground for trying out LLM Models, Embeddings, Vector Stores, Semantic Search, RAG, MCP, Agents, Skills, Azure OpenAI, LLaMa, Mistral, DeepSeek, Qwen, Kimi, Z.ai GLM


## Installation

```bash
pip install -U ai-playground
```

### Installation for development

Pre-requisites:

- Python 3.10+ and pip

```bash
# Start virtual environment
source ./activate

# Install requirements
pip install -r requirements.txt
```


### Running the full playground

- Copy `.env.example` to `.env` and fill in the values

- Run the following command to start the server

```bash
python ai_playground.py
```

---


## Models

Q4_K_M

https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF/resolve/main/Qwen3.6-35B-A3B-UD-Q4_K_M.gguf?download=true

https://huggingface.co/unsloth/gemma-4-26B-A4B-it-GGUF/resolve/main/gemma-4-26B-A4B-it-UD-Q4_K_M.gguf?download=true

https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2/resolve/main/supergemma4-26b-uncensored-fast-v2-Q4_K_M.gguf?download=true

https://huggingface.co/HauhauCS/Gemma-4-E4B-Uncensored-HauhauCS-Aggressive/resolve/main/Gemma-4-E4B-Uncensored-HauhauCS-Aggressive-Q4_K_M.gguf?download=true

Llama 2 - https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF

Llama 3 Instruct - https://huggingface.co/lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF/tree/main


wget -c https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q8_0.gguf
wget -c https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q8_0.gguf
wget -c https://huggingface.co/TheBloke/Mistral-7B-OpenOrca-GGUF/resolve/main/mistral-7b-openorca.Q8_0.gguf

wget -c https://huggingface.co/TheBloke/Wizard-Vicuna-7B-Uncensored-GGUF/resolve/main/Wizard-Vicuna-7B-Uncensored.Q8_0.gguf

wget -c https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF/resolve/main/codellama-7b-instruct.Q8_0.gguf

---

# Inference Local LLM



## Try with LLaMA.cpp

- Extract LLaMA.cpp zip to bin/ directory 

```bash
./bin/main.exe -m models/llama-2-7b-chat.Q8_0.gguf
```

## Try with ollama

```bash
echo "FROM ./models/llama-2-13b-chat.Q5_K_M.gguf" > llama-2-13b-chat.Modelfile

ollama create llama2-13b-chat -f ./llama-2-13b-chat.Modelfile

ollama run llama2-13b-chat
# OR
ollama run llama3.1:7b
ollama serve llama3.1:7b

ollama ps

curl -X POST http://localhost:11434/api/generate -d '{
    "model": "wizardlm-uncensored",
    "prompt":"Who made Rose promise that she would never let go?"
}'

ollama run starcoder2:3b
ollama pull nomic-embed-text

```

## Try with vLLM

```bash
pip install -U vllm

python -u -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --model mistralai/Mistral-7B-v0.1
```

## Try with SGLang

TBD

## Try with Llamafile

## Try with FastChat

```bash
pip install -U fastchat

python -m fastchat.serve.openai_api_server --host localhost --port 8000
```

## Try with LeptonAI

```bash
pip install -U leptonai

```


## Others

https://github.com/sgl-project/sglang

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

---

## Specs

RAM Required:

| Model Size | RAM Required |
|------------|--------------|
| 3B         | 8 GB         |
| 7B         | 16 GB        |
| 13B        | 32 GB        |


---

## Chat UIs

- OpenWebUI - https://github.com/open-webui/open-webui
- kotaemon - https://github.com/Cinnamon/kotaemon
- ChatBotUI - https://github.com/mckaywrigley/chatbot-ui
- OpenUI
- AnythingLLM
- LobeChat
- LibreChat - https://github.com/danny-avila/LibreChat
- oterm - `uvx install oterm`
- https://github.com/billmei/every-chatgpt-gui
- https://github.com/Bin-Huang/chatbox
- https://bettergpt.chat/
- https://github.com/bionic-gpt/bionic-gpt
- aichat - https://github.com/sigoden/aichat

---

## Agents

- AutoGen
- aider-chat - `pipx install aider-chat`
- metagpt - `pipx install metagpt`
- CrewAI - https://github.com/joaomdmoura/crewAI
- AgentScript
- https://github.com/browser-use/web-ui
- https://github.com/browser-use/browser-use
- https://github.com/steel-dev/steel-browser
- https://github.com/phidatahq/phidata
- LangGraph
- https://github.com/elizaOS/eliza
- SmolAgents
- https://github.com/steel-dev/steel-browser
- https://github.com/lightpanda-io/browser

---

## Coding Models

- https://github.com/QwenLM/Qwen3-Coder


---

## Code Assistants / Copilots

- opencode-ai
- Github Copilot
- Qwen Code - https://github.com/QwenLM/qwen-code
- Pi Coding Agent
- Continue.dev - https://github.com/continuedev/continue
- Cursor
- LlamaCoder
- Zed AI
- ClaudeDev
- BlackBox AI
- Tabnine AI
- OpenHands - https://github.com/All-Hands-AI/OpenHands
- https://github.com/TabbyML/tabby
- crush - https://github.com/charmbracelet/crush


bun install -g opencode-ai

bun install -g @Qwen-Code/Qwen-code

uv tool install --python 3.13 kimi-cli

uvx aider-install

uvx oterm

---

## AI Search Engine

- Perplexica - https://github.com/ItzCrazyKns/Perplexica
- https://github.com/InternLM/MindSearch
- SearchGPT
- MemFree

----

## Deep Research

- https://github.com/zilliztech/deep-searcher
- https://github.com/LearningCircuit/local-deep-research


---

## Other Tools

- https://github.com/outlines-dev/outlines
- guidance
- https://leetgpu.com/
- MindsDB
- https://github.com/SWE-agent/SWE-ReX

FireCrawl
Crawl4AI

---

### Development Notes

```bash

GLM-4.7-Flash 

OpenCode

Qwen3-TTS

pip install uv
uvx


uv tool install autogenstudio

pip install ag2

uvx autogenstudio

autogenstudio ui --port 8080 --appdir ./my-app

uvx markitdown

uvx --from langroid-examples chat --model ollama/qwen2.5-coder:32b

uvx --from flask python

dspy

pip install openplayground
openplayground run

uvx --python 3.13 open-webui serve

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



poetry export -f requirements.txt --output requirements.txt
poetry publish --build


lazypredict

mito

pip install langchain-serve

LangServe

pip install -U "langserve[all]"
pip install -U langchain-cli


langflow run


flowise

promptflow
pip install promptflow promptflow-tools


PyGWalker

# DSPy
pip install dspy-ai





https://github.com/ShreyaR/guardrails
https://github.com/guardrails-ai/guardrails



guidance
https://guidancelab.ai/
https://github.com/1rgs/jsonformer

LangChain
https://github.com/jina-ai/langchain-serve

LangFlow / Flowise / LangSmith
ChainLit

promptflow


LMQI
https://github.com/eth-sri/lmql

https://github.com/zilliztech/GPTCache

https://github.com/argilla-io/argilla

https://github.com/vllm-project/vllm

https://github.com/TransformerOptimus/SuperAGI

accelerate
  - accelerate config
  - accelerate env
bitsandbytes
wand
https://github.com/huggingface/text-generation-inference


ctransformers

spacy
spacy-llm
gorilla-cli
https://github.com/langgenius/dify
gptcache

https://github.com/wandb/openui


https://github.com/deepseek-ai/DeepSeek-Coder


https://github.com/jgravelle/AutoGroq


https://github.com/infiniflow/ragflow

Autogen Studio

https://docs.openlit.io/latest/introduction


https://github.com/FujiwaraChoki/MoneyPrinterV2
https://voidface.fly.dev/


uv run ruff check

uv python pin 3.13
uv venv --python 3.11.6
uv python install 3.12

uv add --script smolagents.py smolagents
uv run smolagents.py

uv venv

uvx posting
```
 
