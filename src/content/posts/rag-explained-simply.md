---
title: 'RAG Explained: Why Your Chatbot Forgets Everything (And How to Fix It)'
description: You ask ChatGPT about your company's refund policy. It hallucinates a
  policy that doesn't exist.
pubDate: '2025-01-18'
tags:
- AI Engineering
- RAG
- Fundamentals
author: Khawaja M. Owais
audience: both
draft: false
---

You ask ChatGPT about your company's refund policy. It hallucinates a policy that doesn't exist.

**Why?** LLMs only know what was in their training data (cutoff: months/years ago). They don't know *your* docs.

**RAG (Retrieval-Augmented Generation)** fixes this.

---

## The Mental Model

Think of RAG like an **open-book exam**.

- **Without RAG:** Student memorizes textbook → takes closed-book test → guesses on specifics
- **With RAG:** Student brings textbook → looks up answer → writes accurate response

---

## The 3-Step Pipeline

```
Your Question → [SEARCH] → Relevant Chunks → [GENERATE] → Answer
                    ↑
              Your Documents
```

**Step 1: Chunk & Embed**
- Split your PDFs, docs, Notion pages into ~500-token chunks
- Run each through an embedding model (text-embedding-3-small, nomic-embed-text)
- Store vectors in a vector DB (Chroma, Pineapple, Qdrant, pgvector)

**Step 2: Retrieve**
- User asks question
- Embed the question
- Find top-K most similar chunks (cosine similarity)
- Return those chunks

**Step 3: Generate**
- Stuff chunks into prompt: *"Answer using only this context: [chunks]"*
- LLM answers grounded in your data

---

## Code in 20 Lines (Python + LlamaIndex)

```python
from llama_index import VectorStoreIndex, SimpleDirectoryReader

# 1. Load docs
documents = SimpleDirectoryReader("./my_docs").load_data()

# 2. Build index (chunks + embeds + vector store)
index = VectorStoreIndex.from_documents(documents)

# 3. Query
query_engine = index.as_query_engine()
response = query_engine.query("What's our refund policy?")
print(response)
```

That's it. Works locally. No API keys needed if you use local embeddings.

---

## The Gotchas Nobody Tells You

| Problem | Fix |
|---------|-----|
| Chunks too big → noise | Use smaller chunks (256-512 tokens), overlap 50 tokens |
| Chunks too small → lost context | Add "parent document" reference, use sentence-window retrieval |
| Irrelevant results | Hybrid search: vector + keyword (BM25) |
| LLM ignores context | Explicit prompt: *"Only use provided context. Say 'I don't know' if not there."* |
| Slow at scale | Use pgvector or Qdrant, add metadata filters (date, author, doc type) |

---

## When NOT to Use RAG

- General knowledge questions ("What is photosynthesis?") → LLM already knows
- Real-time data (stock prices, weather) → Use function calling / tools instead
- Massive datasets (millions of docs) → Needs proper infra, not a tutorial

---

## The Ownership Angle

Here's the key: **Your documents stay on your machine.**

With local embeddings (Ollama, sentence-transformers) + local vector DB (Chroma, SQLite-vec), your proprietary data never leaves your server. No OpenAI API calls with your secrets.

**Next up:** Building a memory layer so your agent remembers *you* across sessions — not just your documents.