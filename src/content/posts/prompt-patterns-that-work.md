---
title: Prompt Patterns That Actually Work (Stop Guessing)
description: Most prompts are vibes. "Be helpful." "Think step by step." That's not
  engineering.
pubDate: '2025-02-01'
tags:
- AI Engineering
- Prompt Engineering
- Patterns
- Tutorial
author: Khawaja M. Owais
audience: both
draft: false
---

Most prompts are vibes. "Be helpful." "Think step by step." That's not engineering.

**Patterns** are reusable, testable structures. Here are the 6 that matter.

---

## 1. XML/Structured Output

LLMs follow structure better than prose.

```xml
<instructions>
<role>Senior Python Developer</role>
<task>Refactor this function for readability</task>
<constraints>
<constraint>Keep same function signature</constraint>
<constraint>Add type hints</constraint>
<constraint>Max 50 lines</constraint>
</constraints>
<output_format>
<code>...</code>
<explanation>...</explanation>
</output_format>
</instructions>
```

**Why it works:** Explicit boundaries. Easy to parse. Hard to hallucinate format.

---

## 2. Chain-of-Thought with Scratchpad

Don't just ask for answer. Ask for *reasoning trace*.

```xml
<task>Solve this problem</task>
<process>
<step>Identify knowns and unknowns</step>
<step>Choose approach</step>
<step>Execute calculation</step>
<step>Verify result</step>
</process>
<scratchpad>
Write your reasoning here. Be explicit.
</scratchpad>
<final_answer>...</final_answer>
```

**Pro tip:** Parse the scratchpad separately. Use it for debugging, not the user.

---

## 3. Few-Shot with Diverse Examples

```xml
<examples>
<example>
<input>User wants to book flight to Tokyo</input>
<output>
<plan>
<step>Check calendar for conflicts</step>
<step>Search flights API</step>
<step>Filter by preferences</step>
</plan>
</output>
</example>
<example>
<input>User wants vegan restaurant nearby</input>
<output>
<plan>
<step>Get user location</step>
<step>Search places API for vegan</step>
<step>Filter by rating > 4.0</step>
</output>
</example>
<!-- 3-5 diverse examples -->
</examples>
```

**Key:** Examples must cover *edge cases* (ambiguous, multi-step, failure modes).

---

## 4. ReAct (Reason + Act) Pattern

Standard for tool-using agents:

```
Thought: I need to find the user's timezone to check calendar
Action: get_user_profile(user_id="owais")
Observation: {"timezone": "PKT", "preferences": {...}}
Thought: Now I can check calendar for next week in PKT
Action: check_calendar(start="2025-02-03", end="2025-02-09", tz="PKT")
Observation: [{"time": "10:00", "event": "Meeting"}, ...]
Thought: Found conflict on Monday 10am. Propose alternatives.
Final Answer: ...
```

**Enforce format:** Parse `Thought:` / `Action:` / `Observation:` loops programmatically.

---

## 5. Reflection / Self-Correction

After any output, add a reflection pass:

```xml
<reflection>
<criteria>
<criterion>Does this answer the exact question asked?</criterion>
<criterion>Are all constraints satisfied?</criterion>
<criterion>Any hallucinated facts?</criterion>
<criterion>Is tone appropriate?</criterion>
</criteria>
<verdict>PASS / FAIL - [specific issue]</verdict>
<revision_if_fail>...</revision_if_fail>
</reflection>
```

Run this as a **separate LLM call** (cheaper model works). Only show user if PASS.

---

## 6. Constitutional AI (Guardrails)

Define rules the model must follow:

```xml
<constitution>
<rule id="1">Never execute code without user confirmation</rule>
<rule id="2">Never share personal data from memory</rule>
<rule id="3">Admit uncertainty instead of guessing</rule>
<rule id="4">Ask for clarification if ambiguous</rule>
</constitution>

<enforcement>
Before every response, check against constitution.
If violation: refuse and explain which rule.
</enforcement>
```

---

## Putting It Together: Agent Prompt Template

```python
AGENT_SYSTEM_PROMPT = """
<agent_config>
<name>Research Agent</name>
<model>llama3.1:8b</model>
<tools>web_search, read_url, save_note, query_memory</tools>
</agent_config>

<constitution>
<rule>Only use tools when needed</rule>
<rule>Cite sources for every claim</rule>
<rule>Max 3 tool calls per turn</rule>
<rule>If stuck, ask user for clarification</rule>
</constitution>

<process>
<phase name="PLAN">
<instruction>Break goal into 3-5 atomic steps. Output XML plan.</instruction>
<output><plan><step>...</step></plan></output>
</phase>
<phase name="EXECUTE">
<instruction>Follow plan. Use ReAct format. One tool per turn.</instruction>
</phase>
<phase name="REFLECT">
<instruction>Verify output against goal. Self-correct if needed.</instruction>
</phase>
</process>

<memory>
<working>{working_memory}</working>
<semantic>{user_profile}</semantic>
<episodic>{relevant_episodes}</episodic>
</memory>
"""
```

---

## Testing Your Prompts

```python
def test_prompt(prompt_template, test_cases):
    results = []
    for case in test_cases:
        output = llm.invoke(prompt_template.format(**case))
        passed = evaluate(output, case["expected"])
        results.append({"input": case, "output": output, "passed": passed})
    return results

# Run nightly. Track pass rate. Regress = broken prompt.
```

---

## The Philosophy

**Prompts are code.** Version them. Test them. Refactor them. Don't "vibe prompt."

---

## Next Up

**Multi-agent systems** — when one agent isn't enough. How to orchestrate specialists (researcher, coder, reviewer) that actually collaborate instead of chaos.