---
title: 'Multi-Agent Systems: When One Brain Isn''t Enough'
description: One agent doing everything = jack of all trades, master of none.
pubDate: '2025-02-05'
tags:
- AI Engineering
- Agentic AI
- Multi-Agent
- Architecture
author: Khawaja M. Owais
audience: both
draft: false
---

One agent doing everything = jack of all trades, master of none.

**Multi-agent systems** split work across specialists. Researcher finds info. Coder writes code. Reviewer catches bugs. Manager coordinates.

---

## Why Not One Big Agent?

| Single Agent | Multi-Agent |
|-------------|-------------|
| Context pollution (code + research + chat) | Clean separation of concerns |
| One prompt to rule them all = brittle | Specialized prompts per role |
| Hard to debug | Isolate failures per agent |
| Can't parallelize | Run agents concurrently |
| One model for everything | Different models per role (cheap for simple, strong for hard) |

---

## Common Patterns

### 1. Sequential Pipeline (Assembly Line)

```
User → Planner → Researcher → Coder → Reviewer → User
```

Each agent passes structured output to next. Simple, predictable.

```python
# LangGraph sequential
graph = StateGraph(State)
graph.add_node("plan", planner)
graph.add_node("research", researcher)
graph.add_node("code", coder)
graph.add_node("review", reviewer)
graph.add_edge("plan", "research")
graph.add_edge("research", "code")
graph.add_edge("code", "review")
graph.add_edge("review", END)
```

---

### 2. Supervisor + Workers (Hub and Spoke)

```
          ┌─────────────┐
          │  Supervisor │
          └──────┬──────┘
      ┌─────────┼─────────┐
      ▼         ▼         ▼
  Researcher  Coder   Reviewer
      │         │         │
      └─────────┼─────────┘
                ▼
          ┌─────────────┐
          │  Supervisor │
          └─────────────┘
```

Supervisor decides who acts next. Workers report back. Good for dynamic tasks.

---

### 3. Debate / Consensus (Adversarial)

```
Proposer → Critic → Proposer (revises) → Critic → ... → Consensus
```

Two agents argue. One proposes, one critiques. Iterate until agreement. Great for high-stakes decisions (code review, architecture).

---

### 4. Swarm (Peer-to-Peer)

Agents communicate freely. No central coordinator. Emergent behavior.

**Warning:** Hard to debug. Use sparingly.

---

## Concrete Example: Code Generation Team

```python
# agents.py
from langgraph.graph import StateGraph
from langchain_ollama import ChatOllama

class CodeState(TypedDict):
    task: str
    plan: str
    code: str
    review: str
    final: str

llm_fast = ChatOllama(model="phi3.5:mini")      # Cheap, fast
llm_smart = ChatOllama(model="llama3.1:8b")     # Better reasoning

def planner(state):
    prompt = f"Break this into steps: {state['task']}"
    return {"plan": llm_smart.invoke(prompt).content}

def researcher(state):
    # Uses web search tool
    prompt = f"Research for: {state['plan']}"
    return {"research": llm_fast.invoke(prompt).content}

def coder(state):
    prompt = f"""Write Python code for: {state['plan']}
    Research: {state['research']}"""
    return {"code": llm_smart.invoke(prompt).content}

def reviewer(state):
    prompt = f"""Review this code for bugs, style, security:
    {state['code']}
    Return: PASS or FAIL with specific issues."""
    review = llm_smart.invoke(prompt).content
    if "PASS" in review:
        return {"final": state["code"]}
    else:
        return {"review": review, "code": state["code"]}  # Loop back

def reviser(state):
    prompt = f"""Fix these issues: {state['review']}
    Code: {state['code']}"""
    return {"code": llm_smart.invoke(prompt).content}

# Graph with loop
graph = StateGraph(CodeState)
graph.add_node("plan", planner)
graph.add_node("research", researcher)
graph.add_node("code", coder)
graph.add_node("review", reviewer)
graph.add_node("revise", reviser)

graph.add_edge("plan", "research")
graph.add_edge("research", "code")
graph.add_edge("code", "review")

# Conditional edge: pass → end, fail → revise
graph.add_conditional_edges(
    "review",
    lambda s: "pass" if "PASS" in s.get("review", "") else "fail",
    {"pass": END, "fail": "revise"}
)
graph.add_edge("revise", "review")

app = graph.compile()
```

---

## Communication Protocol

Agents need a **shared schema**. Don't use prose.

```python
from pydantic import BaseModel

class AgentMessage(BaseModel):
    from_agent: str
    to_agent: str
    message_type: Literal["request", "response", "notification"]
    payload: dict
    correlation_id: str  # Track conversation thread
```

**Enforce via Pydantic.** Invalid messages = rejected.

---

## Model Routing (Save Money)

| Task | Model | Why |
|------|-------|-----|
| Planning, architecture | Llama 3.1 70B / GPT-4o | Best reasoning |
| Code generation | DeepSeek Coder / Llama 3.1 8B | Specialized, fast |
| Simple extraction, formatting | Phi-3.5 / Gemma 2B | Cheap, fast |
| Review, critique | Llama 3.1 8B | Good enough |

**Route dynamically** based on task complexity.

---

## The Trap: Agent Sprawl

> "I'll make 20 agents for everything!"

**Result:** Debugging nightmare. Context explosion. Cascading failures.

**Rule:** Start with 1 agent. Split only when:
- Prompt exceeds 4K tokens consistently
- Distinct skill sets needed (coding vs research vs creative)
- You need parallel execution
- Different quality/cost requirements per subtask

---

## Local-First Multi-Agent

All of this runs locally with **LangGraph + Ollama**:

```bash
# Models for different roles
ollama pull llama3.1:8b      # Planner, Coder, Reviewer
ollama pull phi3.5:mini      # Researcher, Formatter
ollama pull deepseek-coder:6b # Code specialist
```

No API keys. No cloud. Your agent team lives on your machine.

---

## The Philosophy

**Specialization beats generalization.** In humans. In LLMs. In systems.

Build a team. Not a monolith.

---

## Next Up

**Tool calling deep dive** — how to design tools agents actually use reliably, with schemas, error handling, and observability.