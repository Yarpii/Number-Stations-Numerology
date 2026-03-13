# What We Know So Far + What To Add Next

This page is a practical bridge between the current repository state and a larger long-term library.

## What we can state with high confidence (documented)

### Station structure is not random noise
Across the current station set, numeric behavior regularly appears in predictable structural roles:
- fixed-size message grouping
- counters and lifecycle markers
- explicit group-count headers
- null/closure markers (including zero-heavy endings)
- repeating retransmission cycles

### Mode changes do not remove structure
Voice, Morse, and hybrid digital/voice examples all preserve analyzable numeric scaffolding.
The surface presentation changes, but segmentation, repetition, and marker logic remain trackable.

### Schedule behavior is part of numeric behavior
Numbers are not only in message bodies; they are also embedded in:
- slot recurrence
- weekday clustering
- multi-frequency reuse
- relay spacing

### Interpretation is strongest when layered
The project is most credible when it preserves a stack:
1. observation (logged behavior)
2. pattern claim (repeatable structure)
3. competing operational explanation
4. optional symbolic hypothesis

## What to add next (high-value expansion plan)

## 1) Add a message-level corpus
Create a `data/message-samples.csv` corpus with one row per transmission sample and fields for:
- raw group sequence
- normalized digits-only payload
- header ID
- group count (claimed vs observed)
- null/full flag
- source URL and timestamp

Why this matters: motif analysis becomes reproducible and scriptable.

## 2) Build reusable metrics
For each station, compute:
- digital-root distributions
- repeated n-gram rates (2/3/5-digit)
- zero-density and terminal-zero rates
- mirror/palindrome frequencies
- per-slot entropy and recurrence indices

Why this matters: symbolic claims can be tested against baseline statistics.

## 3) Separate station facts from operator-family facts
Add an `operators/` folder with pages for families (e.g., Russian-7 family) to avoid duplicating family-level claims inside each station page.

Why this matters: cleaner provenance and fewer contradictory summaries.

## 4) Add uncertainty metadata
Use explicit uncertainty tags in data rows:
- `direct-log`
- `secondary-summary`
- `inferred`
- `interpretive`

Why this matters: downstream analysis can filter by confidence.

## 5) Add change-tracking for active stations
For active stations, keep periodic snapshots of:
- schedule table
- frequency table
- known header formats

Why this matters: enables drift detection over months/years.

## 6) Add validation scripts and CI checks
Automate checks for:
- CSV schema consistency
- valid evidence-level range
- unique IDs
- required source URL presence
- station IDs matching `data/stations.csv`

Why this matters: expansion stays clean as the library grows.

## Suggested immediate milestones

### Milestone A (data quality)
- add message corpus schema
- add validation script for ID and foreign-key consistency
- enforce lint checks in CI

### Milestone B (analysis)
- run first cross-station digital-root report
- generate motif-frequency summary tables
- publish a short baseline report in `docs/`

### Milestone C (coverage)
- add 3–5 more stations with at least 10 sample rows each
- ensure each new station has at least one schedule pattern + one number pattern + one hypothesis

---

If we do only one thing next: build message-level sample data first.
That unlocks almost every deeper analysis path.
