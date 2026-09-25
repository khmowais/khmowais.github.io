---
title: 'Eval-Driven Development: The Harness Ships Before the Feature'
description: An AI feature isn't finished when it works once. It's finished when a machine can tell you it still works tomorrow. Four harness layers deep.
pubDate: '2026-02-12'
tags:
- AI Engineering
- Evaluation
- Agentic AI
- Practices
author: Khawaja M. Owais
audience: both
readingMinutes: 8
sources:
- https://github.com/openai/evals
- https://docs.smith.langchain.com/
- https://arxiv.org/abs/2303.11366
---

An AI feature isn't finished when it works once. It's finished when a machine can tell you it still works tomorrow. That is the entire argument for eval-driven development: the harness ships before the feature, because the harness is what makes the feature finishable.

## The demo premium

Your first agent demo works. That is a fact about the demo, not about the agent. Demo-grade demos are selected by the person holding the laptop, which means the failure modes never get a turn. The only honest way out is to stop trusting the demo and start trusting a test suite the agent cannot argue with.

## Four harness layers

Treat them as cumulative. Most teams stop at layer two; the ones that stop at layer zero are the ones rewriting the prompt on a Friday.

### 1. Unit layer — the schema

An agent that returns invalid JSON, hallucinated tool names, or a `timestamp` field that is a string instead of an ISO date is not a subtle failure, it's a compile-time failure wearing a trench coat. Assert on it:

```python
# tests/test_tool_schema.py
from pydantic import BaseModel, ValidationError

class SearchResult(BaseModel):
    title: str
    url: str
    score: float  # 0..1

def test_search_result_rejects_missing_score():
    with pytest.raises(ValidationError):
        SearchResult(title="x", url="https://example.com")
```

If your agent output can't be validated by Pydantic, your agent doesn't have a schema. Fix that first; it is the cheapest layer and catches the most embarrassing failures.

### 2. Golden set — the stories the product lives on

A golden set is 30-200 curated inputs with a known-good answer. Every release, run them, score them, and diff the score. This catches degradation that feel-based testing cannot: model updates, prompt drift, tool renames.

```python
# tests/eval_golden.py
GOLDEN = [
    ("search for pricing", {"tool": "search_web", "max_results": 5}),
    ("what is your cancellation policy", {"tool": "search_help", "query": "cancel"}),
]

def test_golden_routes():
    for prompt, expected_tool in GOLDEN:
        result = run_agent(prompt)
        assert result.first_tool == expected_tool["tool"], prompt
```

Scoring can be exact, rubric-based, or LLM-as-judge. Use an LLM judge sparingly and always against a human-labeled holdout, otherwise the judge just becomes a second generative model agreeing with the first.

### 3. Differential layer — the model upgrade test

Before you bump the model version, run the golden set on the old model and the new model side by side. "The new model is better" is a vibe; a score diff is a decision. This is the layer that stops you from silently shipping a regression because the new model *felt* smarter on your manual test.

### 4. Adversarial layer — the ones that broke last time

Every production incident becomes a regression test. "The agent sent six emails because the user typed the recipient name twice" — that transcript goes into the adversarial set, labeled *TERMINATE*, and it has to pass from now on. This is where your eval suite compounds: it turns incidents into insurance.

## The loop is the test

A single tool call is easy to verify. An agent is a loop of tool calls with state, and the interesting failures live in the loop: it runs forever, it repeats the same failing action, it terminates before it's done. So evaluate the transcript, not the last message:

- Did it terminate within the turn budget?
- Did it retry the same call more than twice?
- Did it ask permission before side-effecting writes?
- Did the final answer cite the tool result it actually used?

This is the Reflexion idea with the sign flipped: reflection isn't a prompt trick, it's a test that reads the transcript. If your harness looks at the loop, the loop stops being a black box.

## Where the shelf earns its keep

These are not my inventions, they are the field: OpenAI's `evals` is the reference implementation of scored golden sets; LangSmith is the environment where transcripts become datasets and datasets become regression runs. The connection to The Bitter Lesson holds here too — the models win with compute, but your *system* wins with measurement. Measurement is the moat that doesn't go stale when the model card changes.

## The rule of one

If you take nothing else: every schema change, prompt edit, or model bump ships with a recorded score, and every incident ships with a new regression test. That is eval-driven development. The demo premium is what you pay to learn that later.