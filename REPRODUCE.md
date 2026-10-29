# How this repository was made

Built by `scripts/australia-tasmania-law/` in the Lexifina repository (not public), by an AI coding agent:
Claude Opus 5.5 (claude-opus-5-5), run as a Claude Code agent. No model writes or edits legal text, and no model runs at build time; the build is deterministic Python.

## Steps

```
python -X utf8 fetch.py list     # 1 request x 7: Acts in force (BrowseDataSource)
python -X utf8 fetch.py meta     # 2 requests per Act: version list + commencement records
python -X utf8 fetch.py xml      # 1 request per point-in-time version
python -X utf8 build.py --today 2026-10-29
python -X utf8 build.py --today 2026-10-29 --verify-rebuild   # hash-identical main
python -X utf8 check_repo.py --today 2026-10-29               # byte + independent word check
```

## Fetch rate

One process, at most 4 parallel requests to www.legislation.tas.gov.au, 0.25 s pause per worker between
requests, gzip (`curl --compressed`). robots.txt sets no Crawl-delay. Every answer is cached, errors and truncated
responses too (as negative answers), so a rebuild makes no requests.

## Counts

- Acts in force (principal): 609; built 567; not built 42 (NOT-FETCHED.md).
- Point-in-time versions: 3290. Commits on main: 1601 law + 1 documentation; future: 1.
- Amending sources credited: 1146. Commits by kind: {'act': 1297, 'baseline': 253, 'no-act': 4, 'several': 23, 'unclear': 24}.
- Provision changes recorded: 37272 (changes.csv).

## Determinism

The commit stream is written with `git fast-import` from sorted inputs; author and committer dates are the in-force
day at noon in Hobart; the documentation commit is dated the data's retrieval day (2026-10-29). Two builds from
the same cache give the same `main` hash.
