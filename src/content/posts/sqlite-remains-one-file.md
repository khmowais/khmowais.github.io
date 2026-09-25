---
title: 'SQLite Remains One File: A Production Database for the Humane End of the Stack'
description: The most-replicated database in the world is the one-that-isn't-a-server. Where it shines, where it breaks, and why your agent tooling probably wants it.
pubDate: '2026-09-12'
tags:
- SQLite
- Local First
- Production
- AI Engineering
author: Khawaja M. Owais
audience: both
readingMinutes: 6
sources:
- https://www.sqlite.org/
---

The databases that get praised are the ones that need operations teams. The one that actually runs the world — phones, browsers, toasters, most of your favorite software's state — is the library that refuses to become a server, and this note is the defense of that refusal, aimed at the modern AI-adjacent stack (FastAPI, agents, evals, local-first tools) where it applies better than its reputation suggests.

## What it is that people get wrong

SQLite is not a toy that graduated. It is an embedded, zero-configuration SQL engine that stores the *entire* database in a single file on disk — a design that reads as a joke and functions as an engineering virtue. For an instrument-style workload — one process, one user, durable state — it is the correct answer and the fastest path to production correctness: the database is a file you can `cp`, version, and hand to a colleague, and a backup is a copy.

Where the confusion lives: people assume "single-user" means "single-activity," and treat it as a limitation of the same class as a spinning disk. It is not. SQLite handles concurrent readers beautifully, and single-writer concurrency with proper journaling handles a remarkable amount of genuinely concurrent traffic. The threshold is not "small app" — it is "multiple processes fighting over one write head at high rates," which is a narrower problem than the marketing implies.

## Where it shines, specifically for this shelf

- **Local-first tools.** A desktop agent, an eval harness, a field recorder: the data lives in one file on the user's machine, owned by the user, out of the vendor's reach. That is the ownership shelf made concrete — your state is a file.
- **Batch and extraction workloads.** Bulk inserts and read-heavy analytics are what it does best. An eval suite that writes a thousand labeled traces and then queries the loss by model version is a SQLite story with a build time of zero.
- **The single-file backup contract.** `cp app.db backup.db` is not a database migration, it is life. No snapshots to provision, no replica to babysit.

## Where it honestly breaks

Keep the grace notes honest, because this is a "where it breaks" section, not a revival meeting:

- **Multi-writer contention.** Multiple processes writing simultaneously get serialized, and under heavy contention you will feel it. The prescription is layered: keep writes short, batch them in transactions, and if you genuinely need many processes hammering one write head — that is the moment for a server database, and nobody is embarrassed to graduate.
- **It is not a server; do not expose it as one.** Serving the file directly over HTTP without a read-only arrangement is asking for corruption. Put your API in front of it; SQLite is the state, FastAPI is the door.

## The pattern that respects both worlds

The humane production shape for internal tooling: SQLite as the single source of truth, WAL journaling on, a FastAPI layer as the only way in and out, and backups as cron'd `cp`s. When the tool outgrows the file — genuinely, measurably — the migration is as boring as the database was: schema still exists, data is still exportable, and the server database inherits a design that was correct at a smaller scale. You did not build a throwaway; you built a system with a growth path that costs nothing until it must.

The whole case fits in a sentence, which is why it never wins punchy comparisons: the database that does not need to be *operated* earns its keep by leaving you alone — and your agent's state, your evals, and your honest backups live in a file you can hold in your hand.