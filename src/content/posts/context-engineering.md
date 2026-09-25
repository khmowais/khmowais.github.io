---
title: 'Context Engineering: The Hidden Skill That Makes or Breaks Your Agent'
description: Everyone talks about prompt engineering. Context engineering is what
  actually makes agents work.
pubDate: '2025-01-25'
tags:
- AI Engineering
- Agentic AI
- Context Engineering
- Prompt Engineering
author: Khawaja M. Owais
audience: both
draft: false
---

Everyone talks about prompt engineering. **Context engineering** is what actually makes agents work.

---

## The Difference

| Prompt Engineering | Context Engineering |
|-------------------|---------------------|
| "Write the perfect prompt" | "Assemble the right information for *this specific call*" |
| Static, one-size-fits-all | Dynamic, changes per step |
| Human crafts it | System builds it programmatically |
| Focus on wording | Focus on *what's included* and *in what order* |

---

## The Context Budget

Every LLM call has a token budget. Say 8K tokens for context.

```
┌─────────────────────────────────────────────────────┐
│  CONTEXT WINDOW (8,000 tokens)                      │
├──────────────┬──────────────┬───────────────────────┤
│  SYSTEM      │  RETRIEVED   │  WORKING MEMORY       │
│  PROMPT      │  CONTEXT     │  (chat history,       │
│  (~500 tok)  │  (RAG,       │   tool results)        │
│              │   episodes)  │  (~2,000 tok)         │
│              │  (~5,000 tok)│                       │
└──────────────┴──────────────┴───────────────────────┘
```

**Your job:** Decide what goes in each slot, every single turn.

---

## The Context Builder Pattern

```python
class ContextBuilder:
    def __init__(self, max_tokens=8000):
        self.max_tokens = max_tokens
        self.system_prompt = load_system_prompt()
    
    def build(self, user_msg, working_memory, retrieved_context, semantic_memory):
        # 1. Always include system prompt
        parts = [("system", self.system_prompt)]
        
        # 2. Semantic memory (user facts) - high priority, small
        if semantic_memory:
            parts.append(("system", f"User profile: {semantic_memory}"))
        
        # 3. Retrieved context (RAG + episodes) - variable size
        # Trim to fit budget
        context_budget = self.max_tokens - self._tokens(parts) - 2000  # reserve for working memory
        trimmed_context = self._trim(retrieved_context, context_budget)
        if trimmed_context:
            parts.append(("system", f"Relevant context:\n{trimmed_context}"))
        
        # 4. Working memory (recent conversation) - always fits
        for msg in working_memory[-10:]:  # last 10 turns
            parts.append((msg.role, msg.content))
        
        # 5. Current user message
        parts.append(("user", user_msg))
        
        return parts
    
    def _trim(self, text, budget):
        # Smart truncation: keep beginnings/ends, drop middle
        tokens = count_tokens(text)
        if tokens <= budget:
            return text
        # Keep first 30% and last 70% of budget
        keep_start = int(budget * 0.3)
        keep_end = budget - keep_start
        return text[:keep_start] + "\n[...]\n" + text[-keep_end:]
```

---

## Priority Ordering (What Gets Cut First)

When budget is tight, cut in this order:

1. **Never cut:** System prompt, current user message, semantic memory
2. **Cut last:** Most recent 3-5 conversation turns
3. **Cut first:** Old RAG results, old episodic memories
4. **Summarize:** Middle conversation history → one paragraph

---

## Context for Different Agent Steps

| Agent Step | What Context Matters Most |
|------------|--------------------------|
| **Planning** | Goal, available tools, user constraints (semantic), similar past plans (episodic) |
| **Tool Selection** | Tool schemas, recent tool results, user preferences |
| **Tool Execution** | Tool input schema, only relevant params |
| **Reflection** | Full episode so far, expected vs actual outcome |
| **Final Answer** | User question, key findings, citations |

---

## The "Needle in Haystack" Problem

LLMs lose track of info buried in long context.

**Fixes:**
- Put critical instructions at **start AND end** of context
- Use **structured formats** (XML, JSON) not prose
- **Repeat key constraints** in system prompt + user message
- **Cite sources** inline: `[source: doc_3]` so you can verify

---

## Token Counting Matters

```python
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")
def count_tokens(text): return len(enc.encode(text))

# Always know your budget
print(f"System: {count_tokens(sys_prompt)} tokens)} tokens)")
print(f"RAG: {count_tokens(rag tokens)}")
print(f"History: {count_tokens(hist tokens)}")
```

---

## The Philosophy

**Context engineering is information architecture for LLMs.**

You're not "prompting." You're designing a dynamic information supply chain that feeds the right data to the model at the right time.

Every token is a decision. Spend wisely.

---

## Next Up

How to build a **local-first agent stack** — Ollama + LangGraph + Chroma + SQLite — that runs entirely on your laptop, owns your data, and costs $0/month.