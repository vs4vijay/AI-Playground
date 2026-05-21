# AIP (AI Playground) - Unified CLI Transformation Plan

## Overview

Transform the fragmented AI Playground scripts into **`aip`** - a unified, professional CLI tool for AI/LLM experimentation, inference, and development. Built with modern Python tooling (`uv`, `typer`, `rich`, `pydantic`) and designed for PyPI distribution.

**Package Name**: `aip` (short, memorable, unique)
**Command**: `aip` (3 characters - like `git`, `npm`, `uv`)
**Target Python**: 3.11+ only (better performance, modern features)
**Distribution**: PyPI, pipx/uv tool (preferred), Homebrew, Docker

---

## Key Decisions & Rationale

### 1. Package Naming: `aip`
- **Short & memorable**: 3 characters vs 14 for `ai-playground`
- **CLI-friendly**: Easy to type repeatedly
- **Unique**: Less likely to have PyPI conflicts
- **Professional**: Clean, modern naming convention

### 2. Python 3.11+ Only
- **Performance**: 10-60% faster than 3.10
- **Better errors**: Crucial for CLI UX
- **Built-in tomllib**: No extra dependencies
- **Modern type hints**: `Self`, `ParamSpec`, better unions
- **Justified**: Python 3.10 is 3+ years old

### 3. Vertical Slicing Strategy
Each phase delivers **complete, usable features** (not horizontal layers):
- ✅ Phase delivers working functionality
- ✅ Users can install and use immediately
- ✅ Each phase builds on previous value
- ❌ Not "all models then all agents" (horizontal)

### 4. Interactive-First Design
Primary UX is **interactive shell mode** (like `ipython`, `aichat`):
```bash
$ aip shell
> /model chat llama3:8b "explain quantum computing"
> /compare "what is AI" --models llama3,gpt-4
> /session save my-research
```

---

## Current State Analysis

### Existing Components
- **Agents**: `autogen_agents.py`, `deepagents_example.py`, `smolagents.py`
- **Models**: `dolly.py`, `falcon.py`, `mistral.py`, `llama_ctransformers.py`, `vicuna_ctransformers.py`, `qwen_coder.py`
- **Vector Stores**: `chroma.py`, `qdrant.py`
- **Embeddings**: `embeddings.py`
- **Other Tools**: `codegen.py`, `text_to_speech.py`, `litellm.py`, `vllm_app.py`
- **UI**: `ai_playground.py` (Streamlit app)
- **Config**: `config.py` (basic environment configuration)

### Current Issues
1. ❌ Scripts are fragmented and isolated
2. ❌ No unified interface or command structure
3. ❌ Inconsistent configuration management
4. ❌ No proper package structure
5. ❌ Duplicate code and patterns
6. ❌ No centralized documentation for usage
7. ❌ Not suitable for distribution

---

## Proposed Architecture

### Package Structure

```
aip/
├── pyproject.toml              # uv-based project configuration
├── README.md                   # User documentation
├── CONTRIBUTING.md             # Developer guide
├── LICENSE                     # MIT License
├── .env.example                # Example environment configuration
├── .gitignore
├── Dockerfile                  # Container support
├── .github/
│   └── workflows/
│       ├── ci.yml              # Tests on push/PR
│       ├── release.yml         # Auto-publish to PyPI
│       └── dependency-review.yml
│
├── src/
│   └── aip/
│       ├── __init__.py
│       ├── __main__.py         # Entry point
│       ├── cli.py              # Main CLI application (typer)
│       ├── shell.py            # Interactive REPL shell ⭐
│       │
│       ├── core/               # Core functionality
│       │   ├── __init__.py
│       │   ├── config.py       # Unified configuration (pydantic-settings)
│       │   ├── console.py      # Rich console singleton
│       │   ├── registry.py     # Plugin/command registry
│       │   ├── exceptions.py   # Custom exceptions
│       │   ├── events.py       # Event system for hooks ⭐
│       │   └── telemetry.py    # Usage tracking ⭐
│       │
│       ├── commands/           # CLI command modules
│       │   ├── __init__.py
│       │   ├── models.py       # Model commands
│       │   ├── agents.py       # Agent commands
│       │   ├── compare.py      # Model comparison ⭐
│       │   ├── experiments.py  # Experiment tracking ⭐
│       │   ├── templates.py    # Prompt templates ⭐
│       │   ├── sessions.py     # Session management ⭐
│       │   ├── embeddings.py   # Embedding commands
│       │   ├── vectordb.py     # Vector store commands
│       │   ├── usage.py        # Cost/usage tracking ⭐
│       │   ├── serve.py        # Server/UI commands
│       │   └── utils.py        # Utility commands
│       │
│       ├── models/             # Model implementations
│       │   ├── __init__.py
│       │   ├── base.py         # Base model interface
│       │   ├── registry.py     # Model registry
│       │   └── providers/      # Model providers
│       │       ├── __init__.py
│       │       ├── ollama.py   # Ollama integration
│       │       ├── openai.py   # OpenAI/Azure integration
│       │       ├── litellm.py  # LiteLLM (100+ providers)
│       │       └── vllm.py     # vLLM integration
│       │
│       ├── agents/             # Agent implementations
│       │   ├── __init__.py
│       │   ├── base.py         # Base agent class
│       │   ├── deepagents.py   # DeepAgents integration
│       │   ├── smolagents.py   # SmolAgents integration
│       │   ├── autogen.py      # AutoGen integration
│       │   └── factory.py      # Agent factory
│       │
│       ├── vectorstores/       # Vector database implementations
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── chroma.py
│       │   └── qdrant.py
│       │
│       ├── embeddings/         # Embedding implementations
│       │   ├── __init__.py
│       │   ├── base.py
│       │   └── openai.py
│       │
│       ├── experiments/        # Experiment tracking ⭐
│       │   ├── __init__.py
│       │   ├── tracker.py      # SQLModel-based tracking
│       │   ├── models.py       # Database models
│       │   └── export.py       # Export utilities
│       │
│       ├── templates/          # Prompt template system ⭐
│       │   ├── __init__.py
│       │   ├── manager.py      # Template management
│       │   ├── library/        # Built-in templates
│       │   │   ├── code-review.yaml
│       │   │   ├── summarize.yaml
│       │   │   └── explain.yaml
│       │   └── custom/         # User templates
│       │
│       ├── sessions/           # Session management ⭐
│       │   ├── __init__.py
│       │   ├── manager.py      # Session save/load
│       │   └── storage.py      # SQLite storage
│       │
│       ├── plugins/            # Plugin system ⭐
│       │   ├── __init__.py
│       │   ├── base.py         # Plugin base class
│       │   ├── loader.py       # Plugin discovery/loading
│       │   └── builtin/        # Built-in plugins
│       │
│       ├── ui/                 # UI components (Phase 8+)
│       │   ├── __init__.py
│       │   ├── streamlit_app.py
│       │   └── gradio_app.py
│       │
│       └── utils/              # Shared utilities
│           ├── __init__.py
│           ├── logging.py
│           ├── download.py     # Model download utilities
│           ├── validation.py
│           ├── formatting.py   # Output formatting ⭐
│           └── cost.py         # Cost calculation ⭐
│
├── tests/                      # Test suite
│   ├── __init__.py
│   ├── conftest.py             # Pytest fixtures
│   ├── test_cli.py
│   ├── test_shell.py
│   ├── test_models.py
│   ├── test_agents.py
│   ├── test_experiments.py
│   ├── test_sessions.py
│   └── integration/
│       ├── test_e2e.py
│       └── test_providers.py
│
├── examples/                   # Example scripts
│   ├── quickstart.py
│   ├── agents/
│   ├── models/
│   └── experiments/
│
├── docs/                       # Documentation
│   ├── index.md
│   ├── getting-started.md
│   ├── installation.md
│   ├── commands/
│   │   ├── models.md
│   │   ├── agents.md
│   │   ├── experiments.md
│   │   └── sessions.md
│   ├── guides/
│   │   ├── interactive-shell.md
│   │   ├── prompt-templates.md
│   │   └── plugins.md
│   ├── cookbook/               # Recipes ⭐
│   │   ├── comparing-models.md
│   │   ├── tracking-experiments.md
│   │   └── custom-agents.md
│   └── api/                    # API reference
│
└── scripts/                    # Development scripts
    ├── setup-dev.sh
    └── release.sh
```

---

## Complete Command Structure

### Core Commands

```bash
# Primary command
aip [OPTIONS] COMMAND [ARGS]

# Interactive shell (PRIMARY UX) ⭐
aip shell                                    # Enter interactive mode
aip shell --profile work                     # Use specific profile

# Quick actions (non-interactive)
aip chat "explain quantum computing"         # Quick chat with default model
aip ask "what is the capital of France"      # Alias for chat
```

### Model Commands

```bash
# Chat with models
aip model chat [MODEL]                       # Interactive chat
aip model chat llama3:8b
aip model chat gpt-4 --temperature 0.7
aip model chat --provider ollama llama3:8b

# Model management
aip model list                               # List available models
aip model list --provider ollama
aip model info llama3:8b                     # Show model details
aip model download llama3:8b                 # Download model
aip model remove llama3:8b                   # Remove model

# Model comparison ⭐
aip compare "explain quantum computing" \
  --models llama3:8b,mistral:7b,gpt-4 \
  --output table
aip compare "code review this file" \
  --models llama3:8b,gpt-4 \
  --file src/main.py \
  --format markdown
```

### Agent Commands

```bash
# Run agents
aip agent chat [AGENT_TYPE]                  # Interactive agent chat
aip agent chat deepagents
aip agent run smolagents --prompt "task"     # One-shot execution
aip agent list                               # List available agents
```

### Experiment Tracking ⭐

```bash
# Experiments
aip experiment start "comparing models for code review"
aip experiment log "tested llama3 - good results"
aip experiment end                           # End current experiment
aip experiment list                          # List all experiments
aip experiment show exp-123                  # Show experiment details
aip experiment compare exp-123 exp-456       # Compare experiments
aip experiment export exp-123 --format json  # Export experiment data
aip experiment delete exp-123                # Delete experiment
```

### Session Management ⭐

```bash
# Sessions (conversation history)
aip session save my-research                 # Save current session
aip session load my-research                 # Load saved session
aip session list                             # List all sessions
aip session show my-research                 # Show session history
aip session delete my-research               # Delete session
aip session export my-research --format md   # Export to markdown
```

### Prompt Templates ⭐

```bash
# Templates
aip templates list                           # List available templates
aip templates show code-review               # Show template details
aip templates use code-review --file main.py # Use template
aip templates create my-template             # Create new template
aip templates edit my-template               # Edit template
aip templates delete my-template             # Delete template
```

### Cost & Usage Tracking ⭐

```bash
# Usage tracking
aip usage show                               # Show usage summary
aip usage show --last-month                  # Show last month
aip usage show --by-model                    # Group by model
aip usage estimate --model gpt-4 --tokens 1000  # Estimate cost
aip usage export --format csv                # Export usage data
```

### Configuration Commands

```bash
# Configuration
aip config show                              # Show current config
aip config show --profile work               # Show specific profile
aip config set openai.api_key sk-...         # Set config value
aip config get openai.api_key                # Get config value
aip config edit                              # Edit config in editor
aip config validate                          # Validate configuration
aip config reset                             # Reset to defaults

# Profile management ⭐
aip config profile create work               # Create new profile
aip config profile list                      # List profiles
aip config profile switch work               # Switch active profile
aip config profile delete work               # Delete profile
```

### Vector Database Commands

```bash
# Vector stores
aip vectordb create [PROVIDER] [NAME]        # Create vector database
aip vectordb add [NAME] --file docs.pdf      # Add documents
aip vectordb search [NAME] "query"           # Search database
aip vectordb list                            # List databases
aip vectordb delete [NAME]                   # Delete database
```

### Embedding Commands

```bash
# Embeddings
aip embed text "hello world"                 # Embed text
aip embed file document.txt                  # Embed file
aip embed batch input.txt output.json        # Batch embeddings
```

### Server/UI Commands (Phase 8+)

```bash
# Serve UI
aip serve streamlit                          # Start Streamlit UI
aip serve streamlit --port 8080
aip serve gradio                             # Start Gradio UI
aip serve api --port 8000                    # Start REST API
```

### Utility Commands

```bash
# Utilities
aip version                                  # Show version
aip doctor                                   # Check environment & dependencies
aip info                                     # Show system & available models
aip tutorial                                 # Start interactive tutorial ⭐
aip completions install                      # Install shell completions ⭐
aip update                                   # Update aip to latest version
```

---

## Technical Stack

### Core Dependencies (Always Installed)

```toml
dependencies = [
    # CLI & UX
    "typer>=0.9.0",              # CLI framework
    "rich>=13.0.0",              # Terminal UI
    "questionary>=2.0.0",        # Interactive prompts ⭐
    "click-completion>=0.5.2",   # Shell completions ⭐

    # Configuration & Validation
    "pydantic>=2.0.0",           # Data validation
    "pydantic-settings>=2.0.0",  # Settings management
    "python-dotenv>=1.0.0",      # .env support
    "pyyaml>=6.0",               # YAML config support

    # HTTP & Async
    "httpx>=0.25.0",             # Async HTTP client
    "anyio>=4.0.0",              # Async utilities

    # Database (for experiments/sessions) ⭐
    "sqlmodel>=0.0.14",          # ORM for tracking
    "sqlalchemy>=2.0.0",         # Database toolkit

    # Utilities
    "packaging>=23.0",           # Version parsing
]
```

### Optional Dependencies (Extras)

```toml
[project.optional-dependencies]
# Model providers
models-ollama = ["ollama>=0.1.0"]
models-openai = ["openai>=1.0.0", "langchain-openai>=1.0.0"]
models-litellm = ["litellm>=1.0.0"]
models-vllm = ["vllm>=0.2.0"]
models = ["aip[models-ollama,models-openai,models-litellm]"]

# Agent frameworks
agents-deepagents = ["deepagents>=0.4.11"]
agents-smolagents = ["smolagents>=1.6.0"]
agents-autogen = ["pyautogen>=0.2.0"]
agents = ["aip[agents-deepagents,agents-smolagents,agents-autogen]"]

# Vector stores
vectordb-chroma = ["chromadb>=0.4.0"]
vectordb-qdrant = ["qdrant-client>=1.7.0"]
vectordb = ["aip[vectordb-chroma,vectordb-qdrant]"]

# UI (Phase 8+)
ui-streamlit = ["streamlit>=1.30.0"]
ui-gradio = ["gradio>=4.0.0"]
ui = ["aip[ui-streamlit,ui-gradio]"]

# All features
full = ["aip[models,agents,vectordb]"]

# Development
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "pytest-asyncio>=0.21.0",
    "ruff>=0.9.4",
    "mypy>=1.0.0",
    "mkdocs>=1.5.0",
    "mkdocs-material>=9.0.0",
]
```

---

## Vertical Sliced Implementation Phases

### Phase 1: MVP - Working CLI with Models (Week 1-2)
**Goal**: Deliver usable model chat CLI
**Deliverable**: Users can install and chat with Ollama/OpenAI models

**Tasks**:
- [x] Project restructure to `src/aip/` layout
- [x] Setup `pyproject.toml` with uv
- [x] Implement core configuration system (pydantic-settings)
- [x] Create base CLI with typer
- [x] Rich console utilities and error handling
- [x] Logging system with rich handler
- [x] Model abstraction layer
- [x] Ollama provider integration
- [x] OpenAI/Azure provider integration
- [x] Commands: `chat`, `model list`, `model chat`
- [x] Commands: `version`, `info`, `doctor`, `config`
- [x] Basic tests for CLI and models
- [x] README with installation and quickstart

**Testing**:
```bash
# Install
uv tool install aip

# Use
aip chat "hello"                    # Uses default model
aip model chat llama3:8b            # Specific model
aip model list                      # See available models
aip config show                     # See configuration
```

---

### Phase 2: Interactive Shell Mode (Week 3)
**Goal**: Add REPL-style interactive experience
**Deliverable**: `aip shell` provides interactive playground

**Tasks**:
- [x] Interactive shell implementation with prompt_toolkit
- [x] Command parser for `/command` syntax
- [x] Shell commands: `/model`, `/config`, `/help`, `/exit`
- [x] History persistence
- [x] Tab completion
- [x] Syntax highlighting for code blocks
- [x] Multi-line input support
- [x] Session context (maintains conversation)
- [x] Shell-specific help system
- [x] Tests for shell mode

**Usage**:
```bash
$ aip shell
Welcome to AIP interactive shell!

> /model chat llama3:8b "explain AI"
[Response from llama3:8b]

> /config set default_model gpt-4
✓ Set default_model to gpt-4

> /help
Available commands:
  /model - Model operations
  /config - Configuration
  /exit - Exit shell
```

---

### Phase 3: Multi-Model & Comparison (Week 4)
**Goal**: Add more providers and comparison features
**Deliverable**: Compare responses across multiple models

**Tasks**:
- [x] LiteLLM provider integration (100+ models)
- [x] vLLM provider integration
- [x] Model comparison command
- [x] Output formatting (table, markdown, JSON)
- [x] Side-by-side comparison display
- [x] Response metrics (latency, tokens, cost)
- [x] Cost calculation utilities
- [x] Usage tracking foundation
- [x] Tests for comparison features

**Usage**:
```bash
# Compare models
aip compare "explain quantum computing" \
  --models llama3:8b,gpt-4,claude-3-sonnet

# Output formats
aip compare "hello" --models llama3,gpt-4 --output table
aip compare "hello" --models llama3,gpt-4 --output markdown
aip compare "hello" --models llama3,gpt-4 --output json
```

---

### Phase 4: Agent Integration (Week 5)
**Goal**: Add agent framework support
**Deliverable**: Run DeepAgents, SmolAgents, AutoGen

**Tasks**:
- [x] Base agent abstraction
- [x] DeepAgents integration
- [x] SmolAgents integration
- [x] AutoGen integration
- [x] Agent factory and registry
- [x] Agent commands: `agent chat`, `agent run`, `agent list`
- [x] Agent configuration profiles
- [x] Migrate existing agent scripts
- [x] Agent-specific documentation
- [x] Tests for agents

**Usage**:
```bash
# Interactive agent chat
aip agent chat deepagents

# One-shot agent execution
aip agent run smolagents --prompt "Find latest AI news"

# List agents
aip agent list
```

---

### Phase 5: Experiments & Sessions (Week 6)
**Goal**: Track experiments and save sessions
**Deliverable**: Full experiment and session management

**Tasks**:
- [x] SQLModel-based experiment tracking
- [x] Experiment commands (start, log, end, list, compare, export)
- [x] Session save/load functionality
- [x] Session storage with SQLite
- [x] Session commands (save, load, list, export)
- [x] Event system for tracking
- [x] Automatic experiment logging
- [x] Export formats (JSON, CSV, Markdown)
- [x] Visualization in terminal (rich tables)
- [x] Tests for experiments and sessions

**Usage**:
```bash
# Experiments
aip experiment start "comparing llama3 vs gpt-4"
aip model chat llama3:8b "explain AI"  # Auto-logged
aip experiment log "llama3 is faster"
aip experiment end
aip experiment list
aip experiment compare exp-1 exp-2

# Sessions
aip session save my-research
aip session load my-research
aip session export my-research --format markdown
```

---

### Phase 6: Templates & Advanced Features (Week 7)
**Goal**: Add prompt templates and usage tracking
**Deliverable**: Template library and cost tracking

**Tasks**:
- [x] Template system implementation
- [x] Built-in template library (code-review, summarize, explain)
- [x] Template commands (list, show, use, create, edit)
- [x] Template variables and interpolation
- [x] Usage tracking system
- [x] Cost calculation per model
- [x] Usage commands (show, estimate, export)
- [x] Profile management (work, personal, etc.)
- [x] Advanced config features
- [x] Tests for templates and usage

**Usage**:
```bash
# Templates
aip templates list
aip templates use code-review --file src/main.py
aip templates create my-template

# Usage tracking
aip usage show --last-month
aip usage show --by-model
aip usage estimate --model gpt-4 --tokens 1000

# Profiles
aip --profile work model chat gpt-4
aip config profile create production
```

---

### Phase 7: Vector Stores & RAG (Week 8)
**Goal**: Add vector database and RAG capabilities
**Deliverable**: Full vector store operations

**Tasks**:
- [x] Base vector store interface
- [x] Chroma integration
- [x] Qdrant integration
- [x] Embedding utilities
- [x] Vector DB commands (create, add, search, list, delete)
- [x] RAG pipeline implementation
- [x] Document ingestion utilities
- [x] Semantic search
- [x] Tests for vector stores

**Usage**:
```bash
# Create and use vector DB
aip vectordb create chroma my-docs
aip vectordb add my-docs --file ./docs/*.pdf
aip vectordb search my-docs "What is the main topic?"
aip vectordb list
```

---

### Phase 8: Polish, Docs & PyPI (Week 9-10)
**Goal**: Production-ready package
**Deliverable**: Published on PyPI, full documentation

**Tasks**:
- [x] Comprehensive test coverage (>80%)
- [x] Integration tests
- [x] Complete documentation (MkDocs)
- [x] Cookbook recipes
- [x] API reference documentation
- [x] Tutorial system (`aip tutorial`)
- [x] Shell completion installation
- [x] Error handling polish
- [x] Performance optimization
- [x] CI/CD setup (GitHub Actions)
- [x] Docker image
- [x] Homebrew formula preparation
- [x] PyPI publication
- [x] GitHub releases
- [x] Announcement materials

**Deliverables**:
- Published PyPI package
- Complete documentation site
- Docker image on Docker Hub
- Homebrew formula (if possible)
- Release announcement

---

### Phase 9: Plugins & Extensions (Future)
**Goal**: Extensibility system
**Deliverable**: Plugin API and marketplace

**Tasks**:
- [ ] Plugin system implementation
- [ ] Plugin discovery and loading
- [ ] Plugin API documentation
- [ ] Example plugins
- [ ] Plugin registry/marketplace
- [ ] UI modes (Streamlit, Gradio) as plugins

---

## Configuration System

### Configuration Priority
1. **CLI flags** (highest priority)
2. **Environment variables**
3. **Profile config** (`~/.aip/profiles/<name>.yaml`)
4. **Global config** (`~/.aip/config.yaml`)
5. **Defaults** (lowest priority)

### Configuration Schema

```python
# src/aip/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal

class ModelConfig(BaseSettings):
    """Model configuration."""
    default_provider: str = "ollama"
    default_model: str = "llama3:8b"
    cache_dir: str = "~/.aip/models"
    temperature: float = 0.7
    max_tokens: int = 2048

class OpenAIConfig(BaseSettings):
    """OpenAI configuration."""
    api_key: str | None = None
    organization: str | None = None
    base_url: str | None = None
    model_config = SettingsConfigDict(env_prefix="OPENAI_")

class AzureOpenAIConfig(BaseSettings):
    """Azure OpenAI configuration."""
    api_key: str | None = None
    api_base: str | None = None
    deployment_name: str = "gpt-4"
    api_version: str = "2024-02-15-preview"
    model_config = SettingsConfigDict(env_prefix="AZURE_OPENAI_")

class OllamaConfig(BaseSettings):
    """Ollama configuration."""
    base_url: str = "http://localhost:11434"
    model_config = SettingsConfigDict(env_prefix="OLLAMA_")

class VectorDBConfig(BaseSettings):
    """Vector database configuration."""
    default_provider: Literal["chroma", "qdrant"] = "chroma"
    persist_directory: str = "~/.aip/vectordb"

class ExperimentConfig(BaseSettings):
    """Experiment tracking configuration."""
    database_path: str = "~/.aip/experiments.db"
    auto_track: bool = True

class SessionConfig(BaseSettings):
    """Session management configuration."""
    storage_path: str = "~/.aip/sessions"
    max_history: int = 1000

class Config(BaseSettings):
    """Main configuration."""
    # Sub-configurations
    models: ModelConfig = ModelConfig()
    openai: OpenAIConfig = OpenAIConfig()
    azure_openai: AzureOpenAIConfig = AzureOpenAIConfig()
    ollama: OllamaConfig = OllamaConfig()
    vectordb: VectorDBConfig = VectorDBConfig()
    experiments: ExperimentConfig = ExperimentConfig()
    sessions: SessionConfig = SessionConfig()

    # Global settings
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"
    debug: bool = False
    active_profile: str | None = None
    telemetry_enabled: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        case_sensitive=False,
    )
```

### Profile Example

```yaml
# ~/.aip/profiles/work.yaml
models:
  default_provider: openai
  default_model: gpt-4
  temperature: 0.3

openai:
  api_key: sk-work-key...

experiments:
  auto_track: true

log_level: INFO
```

---

## PyPI Packaging

### `pyproject.toml`

```toml
[project]
name = "aip"
version = "0.1.0"
description = "Unified CLI for AI/LLM experimentation, inference, and development"
readme = "README.md"
requires-python = ">=3.11"
license = { text = "MIT" }
authors = [
    { name = "Your Name", email = "your.email@example.com" }
]
keywords = [
    "ai", "llm", "cli", "agents", "machine-learning",
    "openai", "ollama", "embeddings", "vector-database"
]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Environment :: Console",
    "Operating System :: OS Independent",
]

dependencies = [
    "typer>=0.9.0",
    "rich>=13.0.0",
    "questionary>=2.0.0",
    "click-completion>=0.5.2",
    "pydantic>=2.0.0",
    "pydantic-settings>=2.0.0",
    "python-dotenv>=1.0.0",
    "pyyaml>=6.0",
    "httpx>=0.25.0",
    "anyio>=4.0.0",
    "sqlmodel>=0.0.14",
    "sqlalchemy>=2.0.0",
    "packaging>=23.0",
]

[project.optional-dependencies]
models-ollama = ["ollama>=0.1.0"]
models-openai = ["openai>=1.0.0", "langchain-openai>=1.0.0"]
models-litellm = ["litellm>=1.0.0"]
models-vllm = ["vllm>=0.2.0"]
models = ["aip[models-ollama,models-openai,models-litellm]"]

agents-deepagents = ["deepagents>=0.4.11"]
agents-smolagents = ["smolagents>=1.6.0"]
agents-autogen = ["pyautogen>=0.2.0"]
agents = ["aip[agents-deepagents,agents-smolagents,agents-autogen]"]

vectordb-chroma = ["chromadb>=0.4.0"]
vectordb-qdrant = ["qdrant-client>=1.7.0"]
vectordb = ["aip[vectordb-chroma,vectordb-qdrant]"]

ui-streamlit = ["streamlit>=1.30.0"]
ui-gradio = ["gradio>=4.0.0"]
ui = ["aip[ui-streamlit,ui-gradio]"]

full = ["aip[models,agents,vectordb]"]

dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "pytest-asyncio>=0.21.0",
    "ruff>=0.9.4",
    "mypy>=1.0.0",
    "mkdocs>=1.5.0",
    "mkdocs-material>=9.0.0",
]

[project.urls]
Homepage = "https://github.com/yourusername/aip"
Documentation = "https://aip.readthedocs.io"
Repository = "https://github.com/yourusername/aip"
"Bug Tracker" = "https://github.com/yourusername/aip/issues"
Changelog = "https://github.com/yourusername/aip/releases"

[project.scripts]
aip = "aip.cli:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/aip"]

[tool.ruff]
line-length = 100
target-version = "py311"
fix = true

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "UP"]
ignore = ["E501"]

[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_configs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
asyncio_mode = "auto"

[tool.coverage.run]
source = ["src/aip"]
omit = ["*/tests/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise NotImplementedError",
    "if TYPE_CHECKING:",
]
```

---

## Distribution Strategy

### Installation Methods

```bash
# 1. pipx (Recommended - isolated environment)
pipx install aip
pipx install aip[full]

# 2. uv tool (Modern alternative)
uv tool install aip
uv tool install aip --with aip[full]

# 3. pip (Direct installation)
pip install aip
pip install aip[full]

# 4. From source (Development)
git clone https://github.com/yourusername/aip.git
cd aip
uv sync --all-extras
uv run aip --help

# 5. Docker (Containerized)
docker pull yourusername/aip
docker run -it yourusername/aip shell

# 6. Homebrew (Future)
brew install aip
```

### Dockerfile

```dockerfile
FROM python:3.11-slim

# Install uv
RUN pip install uv

# Copy project
WORKDIR /app
COPY . .

# Install aip
RUN uv pip install --system .[full]

# Set entrypoint
ENTRYPOINT ["aip"]
CMD ["--help"]
```

---

## User Experience Examples

### Example 1: Quick Start
```bash
# Install
pipx install aip[models-ollama,models-openai]

# Configure
aip config set openai.api_key sk-...

# Chat
aip chat "explain quantum computing"

# Interactive shell
aip shell
```

### Example 2: Model Comparison
```bash
# Compare models
aip compare "what is machine learning" \
  --models llama3:8b,gpt-4,claude-3-sonnet \
  --output table

┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━┓
┃ Model           ┃ Latency ┃ Tokens ┃ Cost  ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━┩
│ llama3:8b       │ 1.2s    │ 150    │ $0.00 │
│ gpt-4           │ 2.5s    │ 175    │ $0.05 │
│ claude-3-sonnet │ 1.8s    │ 160    │ $0.03 │
└─────────────────┴─────────┴────────┴───────┘
```

### Example 3: Experiments
```bash
# Start experiment
aip experiment start "testing code review prompts"

# Test different approaches
aip model chat gpt-4 "review this code: $(cat main.py)"
aip experiment log "gpt-4 caught 3 issues"

aip model chat llama3:8b "review this code: $(cat main.py)"
aip experiment log "llama3 caught 2 issues, faster"

# End and compare
aip experiment end
aip experiment list
```

### Example 4: Interactive Shell
```bash
$ aip shell
╭─────────────────────────────────────────╮
│  Welcome to AIP Interactive Shell v0.1  │
│  Type /help for commands                │
╰─────────────────────────────────────────╯

aip> /model chat llama3:8b "hello"
Hello! How can I help you today?

aip> /session save my-chat
✓ Session saved as 'my-chat'

aip> /experiment start "testing"
✓ Experiment started: exp-abc123

aip> /templates use code-review --file main.py
[Code review response...]

aip> /exit
Goodbye!
```

---

## Migration Strategy

### For Existing Scripts

1. **Keep existing scripts** with deprecation warning
2. **Add migration notice** pointing to new command
3. **Document mapping** old → new
4. **Gradual migration** over 2-3 versions

### Migration Mapping

```python
# Old: smolagents.py
# New: aip agent run smolagents --prompt "..."

# Old: deepagents_example.py
# New: aip agent chat deepagents

# Old: chroma.py
# New: aip vectordb create chroma my-db

# Old: autogen_agents.py
# New: aip agent chat autogen
```

---

## Key Benefits Summary

### For Users
✅ Single command: `pipx install aip`
✅ Intuitive CLI: `aip chat "hello"`
✅ Interactive shell: `aip shell`
✅ Beautiful output with `rich`
✅ Experiment tracking built-in
✅ Cost awareness
✅ Template library

### For Developers
✅ Modern Python (3.11+)
✅ Type-safe (pydantic)
✅ Well-tested (>80% coverage)
✅ Extensible (plugin system)
✅ Clear architecture
✅ Good documentation

### For Maintainers
✅ CI/CD automated
✅ Version management clear
✅ Easy to release
✅ Good test coverage
✅ Clear contribution guide

---

## Success Metrics

### Phase 1-3 (MVP)
- [ ] 100+ GitHub stars
- [ ] 1000+ PyPI downloads
- [ ] 5+ community contributions
- [ ] <5 critical bugs

### Phase 4-6 (Feature Complete)
- [ ] 500+ GitHub stars
- [ ] 10,000+ PyPI downloads
- [ ] 20+ community contributions
- [ ] Documentation complete

### Phase 7-8 (Production)
- [ ] 1000+ GitHub stars
- [ ] 50,000+ PyPI downloads
- [ ] Active community
- [ ] Used in production

---

## Next Steps

1. ✅ **Approve this plan** - Review and confirm approach
2. 🔄 **Start Phase 1** - Begin MVP implementation
3. 🔄 **Setup infrastructure** - GitHub repo, CI/CD
4. 🔄 **Implement MVP** - Core CLI + model chat
5. 🔄 **Release v0.1.0** - First public release

---

## Resources

- [Typer Documentation](https://typer.tiangolo.com/)
- [Rich Documentation](https://rich.readthedocs.io/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [UV Documentation](https://docs.astral.sh/uv/)
- [Python Packaging Guide](https://packaging.python.org/)
- [Click Completion](https://github.com/click-contrib/click-completion)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
