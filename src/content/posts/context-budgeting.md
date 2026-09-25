---
title: 'Context Budgeting: The Quiet Engineering Discipline Behind Good Agents'
description: A context window is a budget before it is a feature. Count tokens, rank what earns a seat, and keep the stall-clean prefix stable.
pubDate: '2026-03-22'
tags:
- Context Engineering
- Agents
- Cost
- AI Engineering
author: Khawaja M. Owais
audience: both
readingMinutes: 7
sources:
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://github.com/gkamradt/LLMTest_NeedleInAHaystack
---

Every time a model "forgets" something, the usual suspects are named: not enough tokens, wrong model, memory missing. Almost always the real answer is drier than that. You blew the budget. The context window is a budget before it is a feature, and nobody on the team was keeping the ledger.

## The budget, on paper

A 200k-token window is not 200k of thoughtful room. It is 200k tokens of *spend* — multiplication happens before generation. The polite upper bound for serious work is closer to 80-90% of the window, and the cost side is the one teams forget:

| Layer | Tokens (example) | Cost note |
|---|---|---|
| System / instructions | 1,500 | paid on *every* call |
| Tools / schemas | 2,000 | paid on every call — largest controllable fat |
| Conversation so far | grows | grows linearly, re-sent each turn |
| Retrieved context | 8k-50k | per retrieval, not per query |
| Current user query | tiny | the actual work |

That "tools" row is the surprise for most teams. A 5-tool registry with verbose descriptions can eat 3-5k tokens before the user has typed anything. Before optimizing the rest, count what you send unconditionally.

## Measure before you mourn

You cannot budget what you cannot count. Instrument token counts per call, per layer, and per turn; put them on the same dashboard as latency and cost. The number everyone quotes ("we're fine, the window is huge") is almost always the ephemeral one: the window. The number that matters is tokens-per-request, and it only gets worse as the conversation grows.

## Rank, don't cram

When context competes for a seat, apply a policy, not vibes:

1. **System-first.** Instructions are the cheapest tokens you will ever spend — they apply to every turn. Pay for them every time.
2. **Tools by cold start.** If a tool is unused in 80% of runs, it should not be in the hot registry. Load it on demand.
3. **Recency beats orthogonality.** The last N turns usually matter more than a "great summary" that was written once and is now stale. Summaries derail more runs than they save when they overwrite the evidence.
4. **Relevance by retrieval, not by reasoning.** If the context is bigger than the app needs from memory, that is what RAG is for. Full-transcript cramming is the decision to not decide, and you pay for it on every call.

## The stall-clean prefix

There is an established trick for cost and correctness simultaneously: put everything that must *unchanged* at the *same position every call* — system prompt, tool definitions, standing instructions — before any dynamic content. Providers cache that prefix, so the parts that stay still cost a fraction of the parts that move. Cache-stable ordering pays you twice: once in tokens, once in attention. Attention is spent on novelty, and the model's attendance at the stable prefix is better when it genuinely does not change.

## The needle you plant

The needle-in-a-haystack test is the instrument for this discipline: bury one specific fact deep in a long context and check whether the model retrieves it. Run it against your own prompt layouts; the failure mode to look for is not "it can't" but "it can, until the haystack gets taller than the careful part." When the needle falls out, the fix is rarely "bigger window." It is usually "your instructions are buried under output the model was told to ignore."

## Budgeted = boring = shippable

A context budget you can read at a glance — allocated, measured, enforced — is one of the strongest signals that a system will survive production. The window is a fact of the hardware. The budget is a fact of your discipline.