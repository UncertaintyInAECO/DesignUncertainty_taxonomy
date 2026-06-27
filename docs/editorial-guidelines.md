# Editorial guidelines

## Purpose

These guidelines define how concepts are added, edited, reviewed, and validated in the Design Uncertainty Taxonomy.

The goal is to keep the taxonomy:
- consistent;
- interoperable;
- traceable;
- easy to maintain over time.

## Scope

These rules apply to:
- the core SKOS taxonomy in `taxonomy/core/`;
- the research extension layer in `taxonomy/extensions/`;
- any derived exports generated from the maintained Turtle sources.

## Editorial principles

1. Prefer stability over novelty.
2. Prefer clear labels over clever labels.
3. Prefer small, reviewable changes over large unstructured edits.
4. Prefer one concept, one URI, one meaning.
5. Preserve provenance and version history.

## Concept creation

Before adding a new concept, check whether:
- it already exists under another label;
- it belongs in the core taxonomy or only in the extension layer;
- it is a broader concept, narrower concept, or related concept;
- it needs a custom property or simply a SKOS relation.

A new concept should be added only if it represents a distinct and reusable idea.

## Label rules

### Preferred labels
- Use `skos:prefLabel` as the primary name of the concept.
- Use singular noun phrases where possible.
- Use sentence case.
- Keep labels short and precise.
- Avoid articles at the start unless grammatically necessary.

### Alternative labels
Use `skos:altLabel` for:
- synonyms;
- abbreviations;
- spelling variants;
- domain-specific aliases.

Do not use `altLabel` for unrelated terms or broad paraphrases.

### Disallowed label patterns
Avoid:
- vague labels such as “Other issues”;
- duplicated labels with small wording changes;
- labels that combine multiple concepts;
- long explanatory labels that should instead be definitions.

## Definition rules

Every core concept should have a definition unless there is a clear reason not to.

Definitions should:
- explain the meaning, not repeat the label;
- be concise and specific;
- describe the scope of the concept;
- avoid circular wording.

Good definition style:
- one or two sentences;
- direct and domain-specific;
- written in plain language.

## Hierarchy rules

### Broader/narrower relations
Use `skos:broader` and `skos:narrower` only when a true hierarchical relationship exists.

A narrower concept should be:
- a more specific kind of the broader concept;
- a meaningful subcategory;
- consistent with the scheme’s logic.

Do not use hierarchy for:
- chronology;
- causality;
- procedural sequence;
- mere association.

### Top concepts
Only concept classes intended as top-level entry points should be declared with `skos:topConceptOf` and included in `skos:hasTopConcept`.

Avoid creating too many top concepts. The scheme should remain navigable.

### Related concepts
Use `skos:related` when:
- two concepts are clearly connected;
- neither is broader or narrower than the other.

## URI rules

- Use stable URIs.
- Do not rename URIs casually after publication.
- Prefer opaque or semi-opaque identifiers for concepts.
- Reuse the same URI across the core and extension layers when the concept is the same.
- Never create two different URIs for the same concept just because one file is core and the other is extension.

## Core vs extension rules

### Core taxonomy
The core file should contain:
- the concept scheme;
- concept URIs;
- labels;
- definitions;
- hierarchical relations;
- minimal metadata needed for publication.

### Extension layer
The extension file should contain:
- custom classes;
- custom properties;
- analytical dimensions;
- additional semantic assertions about the same concepts.

The extension layer must not contradict the core taxonomy.

## Language rules

- Use English as the primary language unless multilingual labels are explicitly required.
- If multilingual labels are added, keep language tags consistent.
- Do not mix languages inside a single label.
- When adding another language, mirror the editorial meaning, not a literal word-for-word translation.

## Relationship validation

Before committing, check that:
- every concept has a `skos:prefLabel`;
- broader/narrower links point to valid concepts;
- there are no circular hierarchical loops;
- custom properties are used consistently;
- URIs are spelled exactly the same across files.

## Editing workflow

1. Draft the change in the correct file.
2. Run local validation.
3. Review the diff for URI consistency and label quality.
4. Commit with a meaningful message.
5. Regenerate exports only after the source files are approved.

## Validation

Before opening a pull request, run:

```bash
python scripts/validate_skos.py
```

This script:
- parses the core and extension Turtle files;
- checks basic SKOS completeness and consistency;
- checks concept alignment between the two layers;
- regenerates RDF/XML and JSON-LD exports from the core taxonomy.

If needed, install dependencies first:

```bash
pip install rdflib
```

## Review checklist

A change is ready for merge when:
- the concept is genuinely needed;
- the label is precise;
- the definition is clear;
- the hierarchy is correct;
- the URI is stable;
- the extension layer aligns with the core taxonomy;
- validation passes.

## Examples

### Good
- `Design requirements uncertainty`
- `Regulatory uncertainty`
- `Evidence-based interpretation`

### Avoid
- `Problems`
- `Issues`
- `Better design`
- `Various mitigation strategies`

## Commit granularity

Keep one pull request focused on one type of change:
- concept additions;
- definition refinements;
- hierarchy cleanup;
- namespace updates;
- extension-layer enrichment.

Avoid mixing unrelated changes in one PR.

## Final rule

If a change is difficult to explain in one sentence, it probably needs to be split into smaller changes.