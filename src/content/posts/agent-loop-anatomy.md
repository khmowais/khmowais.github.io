---
title: 'The Agent Loop: Anatomy of the Loop Beneath the Demo'
description: Observe, decide, act, reflect, repeat — with a turn budget, a permission gate, and a wire. The loop is the product.
pubDate: '2026-04-01'
tags:
- Agentic AI
- Tools
- AI Engineering
author: Khawaja M. Owais
audience: both
readingMinutes: 8
sources:
- https://github.com/openai/openai-agents-python
- https://arxiv.org/abs/2304.03442
- https://arxiv.org/abs/2303.11366
---

Strip the marketing and an agent is a loop: **observe the world, decide the next act, act through a tool, observe again.** Everything that impresses you about an agent demo — and everything that frustrates you about an agent in production — lives in this loop. The demo sells the loop; production runs it a thousand times in a row, and the loop's patience is the product.

## The canonical loop

```python
import time

class AgentLoop:
    def __init__(self, model, tools, *, max_turns=12, budget_seconds=90):
        self.model = model
        self.tools = {t.name: t for t in tools}
        self.max_turns = max_turns
        self.budget_seconds = budget_seconds
        self.trace = []

    def run(self, task):
        messages = [{"role": "user", "content": task}]
        started = time.time()
        for turn in range(self.max_turns):
            if time.time() - started > self.budget_seconds:
                return {"status": "timeout", "trace": self.trace}
            reply = self.model.invoke(messages, tools=self.tools)
            self.trace.append(reply)
            if not reply.tool_calls:
                return {"status": "done", "answer": reply.content, "trace": self.trace}
            messages.append(reply.model_dump())
            for call in reply.tool_calls:
                result = self.tools[call.name].invoke(call.arguments)
                messages.append({
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": result,
                })
        return {"status": "budget_out", "trace": self.trace}
```

The skeleton is twenty lines. The whole craft is in what the skeleton is wrapped in.

## The turn budget is oxygen

An agent that can call tools in a loop needs a leash as a first-class citizen, not an afterthought. `max_turns` and a wall-clock budget are the minimum; both, because a model that fires repeated failing calls can exhaust turns quickly while a long tool can exhaust the clock. Return the trace on the way out — the budget was hit, and the trace is the evidence of what went wrong.

## The permission gate

Not all tools are equal. Read-only tools (search, read a file) are safe to fire freely. Writes with consequences — send mail, charge a card, mutate production — belong behind a gate that pauses the loop and asks a human. The gate is not friction; it is the difference between a tool that remembers and a tool that regrets. Ask permission *before* the side effect, not after the agent has already discovered disaster.

## Termination is a design decision

Three exits, designed in from the start:

1. **The model says done.** `no tool_calls` is the natural end. Evals should assert it actually terminates this way on the golden set.
2. **No progress.** If the same tool with the same arguments appears twice in a row, the agent is dancing. Detect repeats, break the loop.
3. **Budget exhausted.** Not a failure — a *state*. The transcript on the way out is the feature; ship it to the eval suite and it becomes the next regression test.

## Memory only for what needs it

The loop's raw transcript is the cheapest memory there is and the one agents underuse. Generative Agents made the observation the durable unit — a fact recorded at action time, retrievable later — and that sentiment carries: don't build elaborate memories over transcripts you don't keep. Keep the wire. The "memory layer" of most products is a retrieval problem over the loop's own trace, and you cannot retrieve what you never recorded.

## Reflection, wired in

Reflexion showed that telling the agent to reflect on its failures — with the failure text fed back as context — materially raises success on hard tasks. The mechanism is simple: on failure, generate a short self-summary ("I tried X, it failed because Y, so try Z") and append it before the next attempt. In production this is one extra model call at the failure boundary, and it converts "the agent gave up" into "the agent learned, on tape."

## The loop is the unit of quality

A one-shot model call is measured. The loop is measured by its transcript: turn count, tool distribution, repeats, exits, cost per run. Put those five on a dashboard and the loop stops being a demo and becomes an instrument. That is what the shelf says, in the end: agents are systems, and systems are only as honest as their traces.