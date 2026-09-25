---
title: 'Structured Outputs in Production: Stop Parsing, Start Enforcing'
description: Freeform JSON from a model is a lie the model tells with confidence. Constrained output, one schema, and a validation-driven retry loop.
pubDate: '2026-03-04'
tags:
- Structured Outputs
- Tools
- AI Engineering
author: Khawaja M. Owais
audience: both
readingMinutes: 7
sources:
- https://platform.openai.com/docs/guides/structured-outputs
---

"Just JSON, please" is not a contract. The model returns what it returns — often *valid* JSON that disagrees with your schema in ways a parser cannot see: a missing field, a string where a float lives, an enum value that never existed. Production code that parses that JSON with a shrug is production code that fails at 2 a.m. And it will fail at 2 a.m., because that is when the unusual input arrives.

## Enforce, do not parse

Modern APIs let you constrain the model to a JSON Schema, not merely ask for it. Turns the output contract from polite suggestion to hard constraint. If you are pasting "answer only in JSON with these fields" into every prompt, the model obeys until the moment it forgets; the API doesn't forget.

The shape is the same experience either way — but with enforcement you get:

- guaranteed validity (no `try/except` reading the garbage heap)
- autocomplete-able types in your codebase
- a stable diff surface for evals

## One schema, one source

Declare the schema once, share it in both directions: the model sees it as its output contract, your code sees it as a runtime type.

```python
from pydantic import BaseModel, Field
from enum import Enum

class Tone(str, Enum):
    NEUTRAL = "neutral"
    CONCISE = "concise"
    CRITICAL = "critical"

class Review(BaseModel):
    """A structured review of a pull request."""
    files: list[str] = Field(description="Paths of files that need work")
    blocking: bool = Field(description="True if this stops the merge")
    tone: Tone = Field(description="Tone of the review")
    notes: list[str] = Field(default=[], description="Line-level suggestions")
```

The schema is the prompt. Field descriptions are the instructions — keep them precise; on many models they are the difference between `"blocking": true` on every review and `"blocking": true` only when a merge is actually unsafe.

## Design the schema like a signal, not a transcript

Three habits that read like magic but are just discipline:

1. **Default the boring fields.** Optional fields that 95% of calls leave empty should literally default in the schema. A missing key is indistinguishable from a bug from the outside; an explicit default documents intent.
2. **Kill the free-text enum.** If `tone` can be anything, why is it an enum? The model will happily invent `"private"` and `"sage"`; constrain it.
3. **Keep lists short and atomic.** A model asked for "a list of everything" will produce a list of everything — and blow past output limits. Split big outputs into multiple constrained calls (one per item) instead of one giant list.

## The validation loop

Even with enforced schemas, the *values* can be wrong while the *types* are right. Reject-and-retry is the pattern: validate semantically, feed the validation error back as context, and let the model fix itself.

```python
class ExtractAddress(BaseModel):
    street: str
    city: str
    postal_code: str

for attempt in range(2):
    result = model.with_structured_output(ExtractAddress).invoke(prompt)
    problems = semantic_check(result)          # e.g. postal matches /^\d{5}$/
    if not problems:
        return result
    prompt += f"Your previous answer failed: {problems}. Fix it."
raise ValueError(f"Structured extraction failed after retries: {problems}")
```

This turns a single point of failure into a feedback loop, and it feeds beautifully into your eval suite: every retry that finally succeeds is a labeled example you could have gotten right the first time.

## Where it breaks

- **Very long outputs.** If your schema demands a 50-row table, the token budget fights you. Paginate.
- **Nested deep structures.** Deeply nested schemas degrade quality; flatten to a few levels and let later steps expand.
- **Schema typos as ground truth.** A field name with a typo in the schema is enforced with confidence — your typo became the contract. Read your schema like a prompt reviewer.

Structured output is the difference between an agent that returns a dataclass and an agent that returns a dream about a dataclass. Parse the dream enough times and you'll choose the dataclass.