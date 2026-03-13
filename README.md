# Number Stations Numerology

A research-oriented repository about **how numbers function inside number station traffic** and how those same structures can be interpreted through a **numerological / symbolic framework**.

> This project separates **documented radio practice** from **interpretive symbolism**.
> It does **not** claim that operators intentionally use occult or mystical systems.
> Instead, it asks a narrower question:
>
> **When number stations already depend on structured numeric sequences, what kinds of patterns can be observed, categorized, and interpreted?**

## Project goals

- document repeatable number usage in selected stations
- build a clean vocabulary for describing numeric structures
- distinguish evidence from speculation
- create reusable CSV datasets for future pattern analysis
- make room for symbolic, numerological, or comparative interpretation without confusing it with verified history

## Core idea

In number stations, numbers can serve several different functions at once:

1. **Operational function**  
   Numbers can act as message groups, identifiers, counters, checks, or scheduling markers.

2. **Structural function**  
   Numbers can create rhythm, grouping, repetition, symmetry, null markers, and sequence logic.

3. **Interpretive function**  
   Researchers may assign symbolic meaning to repeated digits, mirrored groups, heavy zero usage, specific roots, or recurring schedule intervals.

This repository keeps those three layers separate.

## Recommended reading order

1. [`docs/methodology.md`](docs/methodology.md)
2. [`docs/terminology.md`](docs/terminology.md)
3. [`docs/evidence-scale.md`](docs/evidence-scale.md)
4. [`docs/symbolism-framework.md`](docs/symbolism-framework.md)
5. station pages in [`stations/`](stations/)
6. motif pages in [`motifs/`](motifs/)

## Folder structure

```text
number-stations-numerology/
├─ README.md
├─ docs/
│  ├─ methodology.md
│  ├─ terminology.md
│  ├─ symbolism-framework.md
│  └─ evidence-scale.md
├─ data/
│  ├─ stations.csv
│  ├─ transmissions.csv
│  ├─ number-patterns.csv
│  ├─ schedule-patterns.csv
│  ├─ frequency-patterns.csv
│  └─ hypotheses.csv
├─ stations/
│  ├─ e03.md
│  ├─ hm01.md
│  └─ v07.md
├─ motifs/
│  ├─ mirrored-groups.md
│  ├─ repeated-triples.md
│  ├─ root-7-patterns.md
│  └─ zero-heavy-groups.md
└─ references/
   ├─ bibliography.md
   └─ external-links.md
```

## Research principles

### 1. Observation before interpretation
We first log what is actually heard, scheduled, repeated, or printed in archives.

### 2. Pattern before meaning
A meaningful interpretation should only follow after a pattern has been described clearly.

### 3. Competing explanations stay visible
A repeated number may be:
- random traffic
- a formatting artifact
- a procedural convention
- an operational marker
- a symbolic choice
- a coincidence

### 4. Interpretive humility
Numerology can be used here as a **reading lens**, not as automatic proof of intent.

## Station set in this starter build

This starter version focuses on three well-known examples:

- **E03** — “Lincolnshire Poacher”
- **HM01** — Cuban hybrid voice + digital format
- **V07** — Russian “Spanish Lady” format

These are useful because they show three different relationships between numbers and structure:
- repeated 5-digit group logic
- daily or rotating counters
- repeated three-part transmissions and null markers

## Suggested future expansions

- add more station pages (E07, V02a, M12, XPA, SK01)
- add scripts for digital-root analysis
- track null messages versus full messages
- compare frequency changes by month or weekday
- map motif families across operators

## Status of this repo

This is a **starter research scaffold**: documentation is written, datasets are seeded, and the files are ready for manual expansion or later automation.

## Sources

See:
- [`references/bibliography.md`](references/bibliography.md)
- [`references/external-links.md`](references/external-links.md)

The factual backbone for the station summaries in this starter build comes primarily from Priyom station profiles and schedules. General framing for numerology and number symbolism is drawn from Encyclopaedia Britannica.

## License note

Add a license file that matches how you want others to reuse the material.  
For open research, **MIT** or **CC BY 4.0** are both common choices depending on whether you want to emphasize code-style reuse or text/data attribution.
