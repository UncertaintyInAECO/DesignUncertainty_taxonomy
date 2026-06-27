# Model overview

## Purpose

This repository contains a two-layer model for representing design uncertainty knowledge:

1. a **core SKOS taxonomy** for publication and reuse;
2. an **extension layer** for research-oriented semantic enrichment.

The separation is intentional. The core model remains simple and interoperable, while the extension layer captures analytical dimensions that go beyond standard SKOS.

## Layer 1: Core taxonomy

File:

```text
taxonomy/core/design-uncertainty.ttl
```

This layer contains the main concept scheme and the hierarchical taxonomy.

### Main characteristics
- Uses `skos:ConceptScheme` and `skos:Concept`.
- Organises concepts through `skos:hasTopConcept`, `skos:broader`, and `skos:narrower`.
- Includes preferred labels and definitions.
- Acts as the canonical public taxonomy.

### Typical use cases
- publication as a taxonomy;
- loading into RDF stores and terminology services;
- reuse in SKOS-based catalogues;
- mapping to other vocabularies.

## Layer 2: Extension layer

File:

```text
taxonomy/extensions/design-uncertainty-annotations.ttl
```

This layer enriches the core concept set with additional domain semantics.

### Main characteristics
- Introduces custom classes such as:
  - `duUncertainty`,
  - `duMitigation`,
  - `duNature`,
  - `duPhase`,
  - `duStakeholder`,
  - `duObject`,
  - `duActionVerb`.
- Introduces custom properties such as:
  - `duIsOfNature`,
  - `duintroducedBy`,
  - `duemergesInPhase`,
  - `duperformedByStakeholder`,
  - `duperformedInPhase`,
  - `durequiresAction`,
  - `duaddressesObject`,
  - `duaddressesObjectm`.

### Typical use cases
- research analysis;
- faceted querying;
- filtering concepts by phase, actor, or uncertainty nature;
- connecting mitigation strategies to actions and project conditions.

## Why the model is split

A single file could technically hold both the SKOS taxonomy and the extension semantics, but this would make maintenance harder.

The split improves:
- **clarity**, because users immediately know which file is the public taxonomy;
- **interoperability**, because the core model stays close to SKOS;
- **maintainability**, because research-specific semantics can evolve independently;
- **reuse**, because external users may only need the core taxonomy.

## Editorial rule

The concept hierarchy should be maintained first in the core layer. If a concept exists in the extension layer, it should correspond clearly to a concept in the core taxonomy.

In practice:
- create or revise the concept in the core taxonomy first;
- then enrich it in the extension layer if analytical metadata is needed.

## Suggested future alignment

To keep the two layers aligned over time, use the same stable concept URIs in both files whenever possible.

Recommended practice:
- one URI per concept;
- SKOS assertions in the core file;
- analytical assertions in the extension file;
- no duplication of labels unless necessary.

## Example

A concept such as `Design requirements uncertainty` can appear:
- in the core layer as a `skos:Concept` with label, definition, and broader relation;
- in the extension layer as the same concept additionally typed as `duUncertainty` and linked to nature, phase, stakeholder, and addressed object.

## Exports

The repository may also publish derived exports such as:
- RDF/XML,
- JSON-LD.

These should be generated from the maintained Turtle sources and not treated as the primary editorial files.

## Validation priority

Validation should focus first on:
1. syntax validity of the Turtle files;
2. integrity of the core SKOS hierarchy;
3. consistency between core and extension concept URIs;
4. completeness of required labels and definitions.