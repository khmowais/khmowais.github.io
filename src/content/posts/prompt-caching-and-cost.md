---
title: "Prompt Caching and Cost: Pay Once for the Part That Doesn't Move"
description: Everything stable above the fold gets cached. Structure the prompt like a cache and you cut spend without touching quality.
pubDate: '2026-05-20'
tags:
- Cost
- Context Engineering
- Prompting
- AI Engineering
author: Khawaja M. Owais
audience: both
readingMinutes: 6
sources:
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
---

The most expensive tokens in an LLM application are the repeated ones. The system prompt, the tool registry, the standing instructions — sent on every call, identical each time — are the portion of your bill that describes the *constant* part of your system. Providers prompt-cache exactly that: a stable prefix that stays in memory earns a discount, often steep. Which makes prompt layout a billing decision as much as a modeling one.

## The cache is a prefix

Caching matches from the start of the request. It does not look inside and keep the "interesting bits." So the practical rule is brutal: **everything that never changes goes first, in the same order, every single call.** The moment you interleave dynamic content before a stable block, you have paid full price for both.

The layout that behaves well:

1. **System prompt** — instructions, persona, invariants. Absolutely static.
2. **Tool definitions** — the tool registry, in a fixed order.
3. **Standing context** — document summaries, brand facts, policy text that does not change per request.
4. **Dynamic** — the conversation, the retrieved documents, the current query.

The dynamic tail is small in most systems. The stable head is where your long-form knowledge lives — and it is precisely the part that used to feel "too expensive to put in the prompt."

## What caching changes about prompting

It changes the economics of *richness*. A detailed system prompt with an appendix of style rules used to be a luxury: every token, every call, full price. Cached, the appendix costs a fraction of a token used once — the write happens behind the scenes. So the discipline flips:

- **Write the prompt properly**, with the full instructions. The stable-block pricing makes careful prompting cheap.
- **Freeze the order.** Reordering the system prompt invalidates the cache for the whole world that reads it. Organize once, then never shuffle. Put optional additions at the *end* of the stable block, appended in a stable sub-order, so a small change does not evict the whole prefix.
- **Batch the changes.** If you need to update a policy text, do it in one daily edit, not ten calls that each sit at different cache positions.

## Cache correctness is an eval, not a guess

Nothing about caching changes the *content* the model sees — it sees the same prompt either way, which is the point. So correctness testing is ordinary: run the golden set, confirm scores are unchanged. The only new test worth adding is a **cache-miss audit**: instrument requests for whether the prefix actually hit, and graph the hit rate per workload. A system you designed to cache that keeps missing is a system whose prompt order drifted; the audit surfaces it before the bill does.

## The honest numbers

Caching is not free, and the discount is per-provider and per-tier — the exact rates move, and "cache write" and "cache hit" are billed differently. Two numbers to hold onto that do not move:

- A stable, correctly-ordered prefix typically cuts the *repeated-token* share of cost by a large multiple. For agent loops (where the same instructions ride along on ten tool calls) that is most of the bill.
- The biggest lever is still **send less**: fewer unconditionally-loaded tool schemas, smaller standing context. Cache discounts the fixed part; it does not forgive the part you did not need to send.

## A budget-shaped reminder

Cache the stable, shrink the dynamic, freeze the order, audit the hit rate. That is the whole practice. The frames argue about models; the people who win on cost argue about layout — and the model never notices the difference, because the prompt it reads is identical. You get the same output and a smaller bill. There is no downside except the discipline.