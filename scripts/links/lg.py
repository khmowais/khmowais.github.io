"""Shared helpers for building the link archive JSON files.

Schema per item:
  title, url, description,
  tags: list[str],
  type: one of
    paper|article|docs|repo|project|tool|book|archive|org|dataset|video|forum|guide|course|news
  subcategory: optional short group label,
  year: optional,
  source: optional short attribution ("arXiv", "GitHub", "O'Reilly").

Usage from a category script:
  import sys; sys.path.insert(0, "/tmp/opencode/links")
  from lg import L, write_cat
  CAT = {"name": "ai", "items": [ L("Title","https://…","desc",["tag"],"paper",sub="…"), ... ]}
  write_cat(CAT)
"""
import json, os

VALID_TYPES = {"paper","article","docs","repo","project","tool","book","archive","org","dataset","video","forum","guide","course","news"}

_DEDUP = {}

def L(title, url, desc, tags, typ, sub=None, year=None, source=None):
    assert typ in VALID_TYPES, f"bad type {typ!r} for {title!r}"
    assert url.startswith("http"), f"bad url {url!r}"
    d = {
        "title": title,
        "url": url,
        "description": desc,
        "tags": [str(t).strip().lower() for t in tags],
        "type": typ,
    }
    if sub: d["subcategory"] = sub
    if year: d["year"] = int(year)
    if source: d["source"] = source
    return d

def write_cat(name, items):
    """Dedupe by url (and by normalized title), validate, write JSON."""
    seen_url, seen_title, out = set(), set(), []
    for it in items:
        u_key = it["url"].rstrip("/")
        t = " ".join(it["title"].split()).lower()
        if u_key in seen_url or t in seen_title:
            print("  dup skipped:", it["title"])
            continue
        seen_url.add(u_key); seen_title.add(t)
        out.append(it)
    out.sort(key=lambda x: x["title"].lower())
    path = f"/home/ap2kmo/Downloads/wer/all_sites/owais-portfolio/src/data/links/{name}.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"{name}.json -> {len(out)} items")