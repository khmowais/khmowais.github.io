---
title: 'Local-First AI Stack: Run Agents on Your Laptop, Own Your Data'
description: Cloud AI is convenient. But your data leaves your machine. Your agent's
  memory lives on someone else's server. You pay per token forever.
pubDate: '2025-01-28'
tags:
- AI Engineering
- Local-First
- Self-Hosting
- Tutorial
author: Khawaja M. Owais
audience: both
draft: false
---

Cloud AI is convenient. But your data leaves your machine. Your agent's memory lives on someone else's server. You pay per token forever.

**Local-first** changes the deal: Model runs on your GPU. Vector DB in your folder. Memory in your SQLite. Zero API calls. Zero monthly cost.

---

## The Stack (All Open Source)

| Layer | Cloud Default | Local-First Alternative |
|-------|---------------|------------------------|
| **LLM** | OpenAI API | **Ollama** (Llama 3, Qwen, Mistral, Phi) |
| **Embeddings** | text-embedding-3-small | **nomic-embed-text** (via Ollama) or **sentence-transformers** |
| **Vector DB** | Pinecone, Weaviate | **Chroma** (local), **Qdrant** (local), **sqlite-vec** |
| **Framework** | LangChain Cloud | **LangGraph** (local), **LangChain** (local) |
| **Memory** | Managed service | **SQLite** + **sqlite-vec** |
| **UI** | Web app | **Gradio**, **Streamlit**, or **Tauri** desktop app |

---

## 5-Minute Setup

```bash
# 1. Install Ollama (runs models locally)
curl -fsSL https://ollama.com/install.sh | sh

# 2. Pull a model (4-bit quantized, ~4GB RAM)
ollama pull llama3.1:8b
ollama pull nomic-embed-text

# 3. Python deps
pip install langgraph langchain-ollama chromadb sentence-transformers

# 4. Verify
ollama run llama3.1:8b "Hello from local AI"
```

---

## Minimal Agent (30 Lines)

```python
# agent.py
from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from typing import TypedDict, List

class State(TypedDict):
    messages: List[dict]
    context: str

llm = ChatOllama(model="llama3.1:8b", temperature=0)
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectordb = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

def retrieve(state):
    query = state["messages"][-1]["content"]
    docs = vectordb.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs])
    return {"context": context}

def generate(state):
    prompt = f"""Context: {state['context']}
    
    Answer the user's question using only the context above.
    If not in context, say "I don't know."
    
    User: {state['messages'][-1]['content']}"""
    response = llm.invoke(prompt)
    return {"messages": state["messages"] + [{"role": "assistant", "content": response.content}]}

graph = StateGraph(State)
graph.add_node("retrieve", retrieve)
graph.add_node("generate", generate)
graph.set_entry_point("retrieve")
graph.add_edge("retrieve", "generate")
graph.add_edge("generate", END)

app = graph.compile()

# Run
result = app.invoke({"messages": [{"role": "user", "content": "What's our refund policy?"}]})
print(result["messages"][-1]["content"])
```

---

## Add Documents Once

```python
# ingest.py
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = DirectoryLoader("./my_docs", glob="**/*.md")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

vectordb.add_documents(chunks)
print(f"Ingested {len(chunks)} chunks")
```

Run `python ingest.py` whenever you add docs. That's it.

---

## Memory That Persists

```python
# memory.py - SQLite + vectors
import sqlite3
import sqlite_vec

db = sqlite3.connect("memory.db")
db.enable_load_extension(True)
sqlite_vec.load(db)

db.execute("""
    CREATE VIRTUAL TABLE episodes USING vec0(
        embedding float[768],
        task text,
        outcome text,
        timestamp text
    )
""")

# Store episode
emb = embeddings.embed_query(f"Task: {task} Outcome: {outcome}")
db.execute("INSERT INTO episodes VALUES (?, ?, ?, ?)", [emb, task, outcome, now()])
db.commit()

# Retrieve similar
query_emb = embeddings.embed_query(current_task)
rows = db.execute("""
    SELECT task, outcome FROM episodes 
    ORDER BY vec_distance_cosine(embedding, ?) 
    LIMIT 3
""", [query_emb]).fetchall()
```

---

## Hardware Reality Check

| Model | VRAM/RAM | Speed (tokens/sec) | Quality |
|-------|----------|-------------------|---------|
| Llama 3.1 8B (4-bit) | 6 GB | ~30 (M2 Mac) / ~50 (RTX 3060) | Good for coding, reasoning |
| Qwen 2.5 14B (4-bit) | 10 GB | ~20 | Better reasoning |
| Phi-3.5 Mini (4-bit) | 3 GB | ~60 | Fast, decent for simple tasks |
| Llama 3.1 70B (4-bit) | 40 GB | ~5 | Best local quality, needs 48GB+ |

**Start with 8B.** Upgrade when you hit limits.

---

## The Philosophy

> "If you don't own the weights, you don't own the intelligence."

Local-first means:
- ✅ Works offline (on a plane, in a bunker, on Mars)
- ✅ Your proprietary data never leaves your disk
- ✅ No rate limits, no quotas, no surprise bills
- ✅ Model behavior is *yours* to customize (fine-tune, system prompts, LoRA)
- ✅ Skills transfer: what you learn applies to any model

---

## Trade-offs

| You Lose | You Gain |
|----------|----------|
| GPT-4o quality | Privacy, ownership, cost control |
| Managed scaling | Learning how systems actually work |
| Auto-updates | Control over when/how models change |

---

## Next Up

**Prompt engineering patterns that actually work** — stop guessing, start using structured templates for planning, tool use, reflection, and code generation.