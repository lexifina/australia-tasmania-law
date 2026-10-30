# How this repository was made

Built by `scripts/australia-tasmania-law/` in the Lexifina repository (not public), by an AI coding agent:
Claude Opus 5.5 (claude-opus-5-5), run as a Claude Code agent. No model writes or edits legal text, and no model runs at build time; the build is deterministic Python.
It reads the files retrieved from Tasmanian Legislation on 2026-10-30 (see [SOURCES.md](SOURCES.md)); how they were
retrieved is not part of this record.

## Steps

With the retrieved files in place:

```
python -X utf8 build.py --today 2026-10-29
python -X utf8 build.py --today 2026-10-29 --verify-rebuild   # hash-identical main
python -X utf8 check_repo.py --today 2026-10-29               # byte + independent word check
```

## Counts

- Acts in force (principal): 609; built 609; not built 0 (NOT-BUILT.md).
- Statutory rules in force (principal): 1365; built 1365; not built 0 (NOT-BUILT.md);
  1816 versions; 1786 commits on main, 289 on future.
- Point-in-time versions of Acts: 4521. Commits on main: 3974 law + 1 documentation; future: 300.
- Amending sources credited: 3198. Commits by kind: {'act': 3569, 'baseline': 276, 'no-act': 6, 'several': 61, 'unclear': 62}.
- Provision changes recorded: 78194 (changes.csv).

## Determinism

The commit stream is written with `git fast-import` from sorted inputs; author and committer dates are the in-force
day at noon in Hobart; the documentation commit is dated the data's retrieval day (2026-10-30). Two builds from
the same retrieved files give the same `main` hash.
