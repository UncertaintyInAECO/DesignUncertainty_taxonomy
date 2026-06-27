# Design Uncertainty Taxonomy

A GitHub repository for maintaining and publishing a SKOS taxonomy on design uncertainty and mitigation strategies in the building and construction domain.

## Overview

This repository hosts a controlled vocabulary describing:
- types of design uncertainty,
- mitigation strategies,
- hierarchical relations between concepts,
- and an optional semantic extension for analytical dimensions such as phase, stakeholder, nature, object, and action.

The repository separates the **core SKOS taxonomy** from the **research extension layer** derived from a qualitative study.

## Canonical files

- `taxonomy/core/design-uncertainty.ttl` is the **canonical SKOS taxonomy**.
- `taxonomy/extensions/design-uncertainty-annotations.ttl` is the **semantic extension layer** used to enrich the taxonomy with analytical metadata.

## Modelling approach

The core taxonomy is intended for broad reuse in SKOS-compatible tools and knowledge organization workflows.

The extension file adds research-specific semantics, including dimensions such as:
- uncertainty nature,
- lifecycle phase,
- stakeholder,
- addressed object,
- mitigation action.

This allows the same concept set to support both:
1. taxonomy publication and browsing;
2. research analysis and richer querying.

## Scope

| Property | Value |
|---|---|
| Domain | Design uncertainty in building projects |
| Main standard | SKOS |
| Core format | Turtle (`.ttl`) |
| Primary language | English |
| Main namespace | To be defined in `docs/namespace-policy.md` |

## How to use

### Use the taxonomy only
Use:

```text
taxonomy/core/design-uncertainty.ttl
```

This file is best for:
- SKOS publication,
- browsing concept hierarchies,
- reuse in RDF stores,
- interoperability with external vocabularies.

### Use the enriched model
Use:

```text
taxonomy/extensions/design-uncertainty-annotations.ttl
```

This file is best for:
- research analysis,
- advanced querying,
- classification by phase, stakeholder, nature, and object,
- linking mitigation concepts to action patterns.

## Editing policy

- Edit the **core taxonomy** when adding, removing, or changing concepts and SKOS relations.
- Edit the **extension layer** when adding analytical dimensions or custom semantic assertions.
- Do not manually edit derived exports unless explicitly needed.

## Contributing

See [docs/editorial-guidelines.md](editorial-guidelines.md) for workflow, editorial rules, and pull request guidance.

Before committing, run:

```bash
python scripts/validate_skos.py
```

This script validates the Turtle files and regenerates derived exports.

## Citation and provenance

The taxonomy is based on research modelling work and should be versioned carefully. Every structural change to concepts, labels, or semantic relations should be recorded in `CHANGELOG.md`.

## Licence

Add the selected licence in `LICENSE`.