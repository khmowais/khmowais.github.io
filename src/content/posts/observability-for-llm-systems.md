---
title: 'Observability for LLM Systems: What to Record and Why'
description: Prompts, responses, tokens, latency, cost, and the trace that joins them. An LLM app without records is a demo with a production URL.
pubDate: '2026-04-18'
tags:
- Observability
- AI Engineering
- Production
author: Khawaja M. Owais
audience: both
readingMinutes: 7
sources:
- https://docs.smith.langchain.com/
- https://lilianweng.github.io/
---

The demos people remember fail the same way: they only look good because nobody kept receipts. An LLM application without records is not a system, it is a demo with a production URL. The moment something drifts, you have a feeling instead of a graph, and a feeling is not a rollback decision.

## Record the four numbers on every call

Per request, keep the disciplined minimum:

- **Tokens** in, tokens out, and the breakdown by layer (system, tools, retrieved, conversation) — this is your cost ledger and your context-budget audit at once.
- **Latency**, ideally split into time-to-first-token and total. For streaming UIs the split is the whole story.
- **Cost.** Tokens you paid for are money; multiplying the ledger by price per token every request turns "the bill doubled" into a statement about *when*, not a surprise.
- **Model + version.** If you upgrade and quality dips, the version column is the smoking gun. Without it, the incident becomes an argument about whether weekends count.

## Trace the agent thread

A model call is easy to observe. An agent is a thread through many calls, and the interesting questions are about the *thread*: which tool sequence produced this answer? Did the loop re-enter moderation twice? Which trace cost 40 cents?

That is what a tracing layer — LangSmith being the reference — gives you: call, tool, and turn become *spans*, and the whole run becomes a span tree you can walk backward from a bad answer. Every "why did it do that" turns into a query against your own traces instead of an interrogation of a black box.

## Record transcripts, not just scores

Scores without transcripts are a thesis nobody can examine. Store the prompts, the responses, the tool calls and results, at least sampled. Two uses that pay the storage back a thousandfold:

1. **Evals ground against reality.** The golden set is curated; production transcripts are the truth. Sample real traffic, label a slice, and the golden set stops being aspirational.
2. **Incident reconstruction.** The adversarial eval suite I keep going on about is built from transcripts of what actually broke. You cannot mine the past for regression tests if you threw the past away.

## Drift is a distribution problem

The failure mode you will actually meet is not a single gross error, it is a hundred slow ones. Inputs drift across the months (users learn to phrase differently, integrations change their formats), outputs drift because models change under you. Watch distributions, not just point errors: average input length, token-out-per-token-in ratio, tool-call rate, refusal rate. A quiet rise in tool-call rate is the canary; the evals suite is the diagnosis.

## Redact like the regulator is already here

Full-prompt recording is the most useful thing you can store and the least defensible thing to store carelessly. Scrubbing is not optional around personal data: redact PII at write time (names, emails, phone numbers, addresses, keys), hash internally-stable identifiers so joins survive, and treat raw payloads as secrets with retention. If your trace store is the same bucket as your `.env`, that is not observability, it is a liability.

## The one visualization that matters

Not the dashboard. The **diff**: this week's eval score against last week's, per feature, with the model version pinned. Everything else — the tree views, the flamegraphs — is negotiation. Your system is either measurably better than it was last week or it isn't, and the records are the only referee worth a damn.