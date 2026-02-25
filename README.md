# draw-rich-local

Local, end-to-end replica architecture for an **Eraser.io-style** AI diagram workflow.

This project uses:
- **D2** as the local rendering engine.
- A **local LLM** (default: Ollama-compatible API) to translate natural language into D2 syntax.
- A lightweight **style enhancer** that injects richer colors and auto-icons to mimic Eraser's visual polish.

## Architecture

```text
User Prompt
   │
   ▼
Prompt Builder ──► Local LLM Client ──► Raw D2
   │                                 │
   └──────────── style hints ◄───────┘
                    │
                    ▼
             Style Enhancer (colors/icons)
                    │
                    ▼
                D2 Renderer
                    │
                    ▼
              SVG / PNG output
```

## Requirements

- Python 3.10+
- [D2 CLI](https://d2lang.com/tour/install/) installed and available on `PATH`
- Local LLM endpoint (default expects Ollama at `http://localhost:11434`)

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Generate a diagram:

```bash
draw-rich-local \
  --prompt "Design a RAG architecture with ingestion, vector DB, API, and monitoring" \
  --model llama3.1 \
  --out outputs/rag.svg
```

This command will:
1. Ask the local model for D2 source.
2. Post-process nodes with color + icon hints.
3. Render using `d2` into the requested output format.

## Notes

- If D2 is not installed, generation still produces `.d2` source for manual rendering later.
- The enhancer is intentionally deterministic, so outputs are stable even when model output varies.

