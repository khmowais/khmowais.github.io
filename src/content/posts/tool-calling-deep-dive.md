---
title: 'Tool Calling Deep Dive: How to Design Tools Agents Actually Use'
description: Agents fail because tools are confusing. Bad names. Vague schemas. No
  error handling.
pubDate: '2025-02-08'
tags:
- AI Engineering
- Agentic AI
- Tools
- Function Calling
- Tutorial
author: Khawaja M. Owais
audience: both
draft: false
---

Agents fail because tools are confusing. Bad names. Vague schemas. No error handling.

**Good tools = reliable agents.** Here's how to design them.

---

## The Tool Contract

Every tool is a **function with a strict schema**:

```python
from pydantic import BaseModel, Field
from typing import Literal

class SearchWebArgs(BaseModel):
    query: str = Field(..., description="Specific search query, 5-10 words")
    max_results: int = Field(default=5, ge=1, le=20)
    recency_days: int = Field(default=365, description="How far back to search")

class SearchWebResult(BaseModel):
    results: list[dict]  # {title, url, snippet}
    query_used: str
```

**Agent sees:** Name, description, JSON schema for args, JSON schema for return.

---

## Naming: Verb + Noun

| Bad | Good |
|-----|------|
| `search` | `search_web` |
| `get_data` | `query_database` |
| `do_thing` | `send_email` |
| `api_call` | `fetch_weather` |

**Rule:** Name must tell *what it does* and *what domain*.

---

## Descriptions: The Hidden Prompt

The tool description **is a prompt**. LLMs read it to decide *when* to call.

```python
@tool(
    name="search_web",
    description="""Search the public web for current information.
    
    USE WHEN:
    - User asks about recent events, news, prices
    - You need facts not in your training data
    - Verifying claims with sources
    
    DO NOT USE WHEN:
    - General knowledge (capital of France)
    - Math, coding, reasoning tasks
    - User's private data (use query_memory instead)
    
    TIPS:
    - Be specific: "llama 3.1 release date 2024" not "llama"
    - Set recency_days for time-sensitive queries
    """
)
def search_web(args: SearchWebArgs) -> SearchWebResult:
    ...
```

---

## Schema Design Rules

### 1. Required vs Optional
```python
class SendEmailArgs(BaseModel):
    to: str = Field(..., description="Recipient email address")  # Required
    subject: str = Field(..., description="Email subject line")  # Required
    body: str = Field(..., description="Email body text")        # Required
    cc: list[str] = Field(default=[], description="CC recipients")  # Optional
    attachments: list[str] = Field(default=[], description="File paths")  # Optional
```

### 2. Enums for Constrained Values
```python
class LogLevel(str, Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

class LogArgs(BaseModel):
    level: LogLevel = Field(..., description="Severity level")
    message: str = Field(..., max_length=1000)
```

### 3. Structured Returns (Not Strings!)
```python
# BAD: Returns raw string
def bad_tool() -> str:
    return "Success: saved to file.txt"

# GOOD: Structured, parseable
class SaveResult(BaseModel):
    success: bool
    path: str
    bytes_written: int
    timestamp: str
```

---

## Error Handling: Don't Crash, Return Structure

```python
class ToolResult(BaseModel):
    success: bool
    data: Any = None
    error: str = None
    error_code: str = None  # RETRYABLE, PERMANENT, INVALID_ARGS

@tool
def fetch_url(args: FetchArgs) -> ToolResult:
    try:
        response = requests.get(args.url, timeout=10)
        response.raise_for_status()
        return ToolResult(success=True, data={"html": response.text})
    except requests.Timeout:
        return ToolResult(
            success=False,
            error="Request timed out after 10s",
            error_code="RETRYABLE"
        )
    except requests.HTTPError as e:
        return ToolResult(
            success=False,
            error=f"HTTP {e.response.status_code}",
            error_code="PERMANENT" if e.response.status_code >= 400 else "RETRYABLE"
        )
```

**Agent reads `error_code` and decides:** Retry? Try different tool? Ask user?

---

## Tool Categories (Mental Model)

| Category | Examples | Latency | Reliability |
|----------|----------|---------|-------------|
| **Read-only** | search, query_db, read_file, get_weather | Fast | High |
| **Write (idempotent)** | save_note, upsert_record | Medium | Medium |
| **Write (side effects)** | send_email, charge_card, post_tweet | Slow | Low (need confirmation) |
| **Compute** | run_code, calculate, transform | Variable | High |

**Agent should know category** → handles confirmation/retries appropriately.

---

## The "Tool Description" Prompt Pattern

```python
TOOL_SYSTEM_PROMPT = """
You have access to tools. Use them when appropriate.

TOOL SELECTION RULES:
1. Prefer read-only tools first (search, query, read)
2. Never call write tools without explicit user confirmation
3. If tool returns error_code=RETRYABLE, retry once with adjusted args
4. If tool returns error_code=PERMANENT, try alternative approach
5. Always cite tool results: [source: tool_name]

AVAILABLE TOOLS:
{tool_definitions}
"""
```

---

## Observability: Log Everything

```python
import time
import logging

tool_logger = logging.getLogger("tools")

def instrumented_tool(fn):
    def wrapper(args):
        start = time.time()
        tool_logger.info(f"TOOL_CALL {fn.__name__} args={args.model_dump()}")
        try:
            result = fn(args)
            duration = time.time() - start
            tool_logger.info(f"TOOL_RESULT {fn.__name__} success={result.success} duration={duration:.2f}s")
            return result
        except Exception as e:
            tool_logger.error(f"TOOL_ERROR {fn.__name__} error={str(e)}")
            raise
    return wrapper
```

---

## Testing Tools in Isolation

```python
def test_search_web():
    # Unit test: mock HTTP, verify args/result
    result = search_web(SearchWebArgs(query="python asyncio tutorial"))
    assert result.success
    assert len(result.data["results"]) > 0
    assert all("title" in r for r in result.data["results"])

def test_search_web_empty():
    result = search_web(SearchWebArgs(query="xyznonexistentquery123"))
    assert result.success
    assert result.data["results"] == []

# Integration test: real API
@pytest.mark.integration
def test_search_web_live():
    result = search_web(SearchWebArgs(query="current bitcoin price"))
    assert result.success
    assert any("bitcoin" in r["title"].lower() for r in result.data["results"])
```

---

## The Philosophy

**Tools are the API between agent and world.** Design them like you'd design a public REST API: versioned, documented, tested, monitored.

---

## Next Up

**Evaluating agents** — how to know if your agent actually works. Benchmarks, test cases, and the "vibe check" that isn't a vibe check.