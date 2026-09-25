---
title: 'The Memory Layer: Why Your Agent Forgets You Tomorrow'
description: 'You tell your agent: "I prefer window seats, hate early flights, and
  my budget is $500."'
pubDate: '2025-01-22'
tags:
- AI Engineering
- Agentic AI
- Memory
- Architecture
author: Khawaja M. Owais
audience: both
draft: false
---

You tell your agent: "I prefer window seats, hate early flights, and my budget is $500."

Next week you ask: "Book me a flight to Denver."

It books a 6 AM middle seat for $800.

**Why?** No memory layer.

---

## Three Types of Memory

```
┌─────────────────────────────────────────────────────────┐
│                    AGENT MEMORY                         │
├──────────────┬──────────────┬──────────────────────────┤
│   WORKING    │   EPISODIC   │       SEMANTIC           │
│  (Short-term)│  (Episodes)  │      (Facts)             │
├──────────────┼──────────────┼──────────────────────────┤
│ Current chat │ Past tasks   │ User preferences         │
│ Tool results │ Outcomes     │ Domain knowledge         │
│ Scratchpad   │ Conversations│ Learned patterns         │
└──────────────┴──────────────┴──────────────────────────┘
```

---

## Working Memory = Context Window

This is just the conversation history + current tool results fed to the LLM.

**Limitation:** Context window fills up. Old stuff gets dropped.

**Fix:** Summarize old turns. Keep only last 10 messages + summary of earlier ones.

```python
# Simple sliding window with summary
def manage_context(messages, max_tokens=8000):
    if count_tokens(messages) > max_tokens:
        # Summarize oldest half
        old = messages[:len(messages)//2]
        summary = llm.summarize(old)
        # Keep summary + recent messages
        return [{"role": "system", "content": f"Previous context: {summary}"}] + messages[len(messages)//2:]
    return messages
```

---

## Episodic Memory = "What Happened"

Stores complete episodes: task → steps → outcome → feedback.

**Use case:** "Remember that time I asked for a vegan restaurant and you suggested a steakhouse? Don't do that again."

**Implementation:** Vector store where each episode is a document:
```json
{
  "task": "Find vegan restaurant",
  "steps": ["searched yelp", "filtered vegan", "presented 3 options"],
  "outcome": "User rejected all - wanted gluten-free too",
  "feedback": "negative",
  "timestamp": "2025-01-20"
}
```

Retrieve similar past episodes before planning new task.

---

## Semantic Memory = "What I Know About You"

Persistent facts: preferences, constraints, identity.

**Storage:** Simple key-value or structured profile:
```json
{
  "user_id": "owais",
  "travel": {"seat": "window", "max_price": 500, "avoid_early": true},
  "food": {"diet": "vegan", "allergies": ["gluten"]},
  "work": {"timezone": "PKT", "preferred_hours": "10-18"}
}
```

**Update rule:** Extract facts from conversations automatically. "I hate early flights" → update `travel.avoid_early = true`.

---

## The Architecture

```
User Message
     │
     ▼
┌──────────────────┐
│  Memory Router   │──→ Working Memory (recent context)
└────────┬─────────┘
         │
    ┌────┴────┐
    ▼         ▼
Episodic   Semantic
Memory     Memory
    │         │
    └────┬────┘
         ▼
┌──────────────────┐
│  Context Builder │──→ Builds prompt for LLM
└────────┬─────────┘
         │
         ▼
      LLM
```

---

## Local-First = You Own It

All three memory types can live in **local SQLite + vector extension** or **local Chroma/Qdrant**.

No cloud. No subscription. Your agent's memory of you stays on *your* machine.

```python
# sqlite-vec example (runs in-process, no server)
import sqlite3
import sqlite_vec

db = sqlite3.connect("agent_memory.db")
db.enable_load_extension(True)
sqlite_vec.load(db)
# Now you have vector search in SQLite
```

---

## Minimal Starter

Don't build all three at once. Start with:

1. **Working memory** — sliding window (already in most frameworks)
2. **Semantic memory** — a `user_profile.json` you update manually
3. Add **episodic** later when you feel the pain

---

## The Philosophy

Memory is what turns a *tool* into a *teammate*.

A calculator has no memory. A colleague remembers you hate meetings before 10 AM.

**Next up:** Context engineering — how to pack the right context into every LLM call without blowing your token budget.