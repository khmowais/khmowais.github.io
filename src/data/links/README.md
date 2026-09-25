# Link archive data

The Interesting Links archive lives here — one JSON file per category,
plus `src/lib/links.ts` which aggregates them into `CATEGORIES` /
`ALL_LINKS` for the pages under `/links`.

## Schema (per item)

| field         | type   | notes                                                        |
| ------------- | ------ | ------------------------------------------------------------ |
| `title`       | string | human title                                                   |
| `url`         | string | external href (verified with a curl sweep at build time)      |
| `description` | string | 1–2 sentence, engineering-flavoured                          |
| `tags`        | string[] | lowercase, singular-ish keywords used by the client search   |
| `type`        | string | one of the `LinkType` values below                            |
| `subcategory` | string | optional grouping label inside the category (e.g. `rag`)      |
| `year`        | number | optional original publication year                            |
| `source`      | string | optional short attribution (e.g. `arXiv`, `GitHub`)           |

`LinkType` values (see `src/lib/links.ts`):

paper · article · docs · repo · project · tool · book · archive ·
org · dataset · video · forum · guide · course · news

## Adding links

1. Edit the matching category JSON in this folder (or add a new file and
   register it in `src/lib/links.ts`).
2. Keep descriptions useful, tags lowercase, and `type` from the list.
3. Every URL must be real — run the verification sweep before shipping:

```sh
scripts/links/verify.py      # prints dead / questionable results
```

The generator scripts that produced these files live in
`scripts/links/` and can regenerate a category from its source list:

```sh
python3 scripts/links/ai.py  # rewrites ai.json from the curated list
```

Counts are honest: the archive reports how many links actually pass
verification, not a round number.

## Categories

| file           | id          | focus                                                          |
| -------------- | ----------- | -------------------------------------------------------------- |
| `ai.json`      | `ai`        | AI engineering: papers, agents, RAG, evals, tooling            |
| `local-ai.json`| `local-ai`  | Ollama/llama.cpp, GGUF, self-hosted models, homelab            |
| `lowlevel.json`| `lowlevel`  | silicon, assembly, emulation, OS internals, retro/homebrew     |
| `radio.json`   | `radio`     | ham radio, digital modes, packet, LoRa/Meshtastic/Reticulum, SDR |
| `wildlife.json`| `wildlife`  | raptors, falconry, ornithology, Pakistan/Himalaya              |
| `history.json` | `history`   | Kashmir/north-west primary sources, gazetteers, archives       |
| `ownership.json`| `ownership`| DRM, right to repair, preservation, abandonware, local-first   |
| `systems.json` | `systems`   | distributed systems, internet infrastructure, servers          |
| `software.json`| `software`  | languages, books, tools, craft                                 |
| `misc.json`    | `misc`      | robotics, science, machines, resilience, rabbit holes          |