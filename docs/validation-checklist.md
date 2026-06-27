# Validation checklist

Run the repository validation script before committing changes:

```bash
python scripts/validate_skos.py
```

The script parses the Turtle files, checks core SKOS integrity, checks alignment between the core and extension layers, and regenerates export files when validation passes.

## Automated validation

Before opening a pull request, run:

```bash
python scripts/validate_skos.py
```

If your environment does not yet have the required package, install it first:

```bash
pip install rdflib
```

A successful run should:
- parse the core Turtle file successfully;
- parse the extension Turtle file successfully;
- report no blocking errors;
- regenerate the export files in `taxonomy/exports/`.

## Syntax checks
- Turtle parses without errors.
- Prefix declarations are valid.
- URIs are consistently formed.

## SKOS checks
- A `skos:ConceptScheme` exists in the core file.
- Every concept has a `skos:prefLabel`.
- Concepts have consistent `skos:broader` / `skos:narrower` logic.
- Concepts are linked to the scheme appropriately.
- No self-referential broader relations exist.

## Editorial checks
- Labels are precise and non-duplicative.
- Definitions are concise and non-circular.
- `skos:altLabel` values are true alternatives, not definitions.
- Top concepts are used intentionally.

## Core-extension alignment
- Concepts reused in the extension layer match the same URI used in the core layer.
- Extension concepts do not introduce accidental duplicates of core concepts.
- Custom semantic assertions do not contradict the core taxonomy.

## Export checks
After successful validation, confirm that these files are updated as expected:
- `taxonomy/exports/design-uncertainty.rdf`
- `taxonomy/exports/design-uncertainty.jsonld`

Do not manually edit these export files unless there is a specific reason to do so.

## Pull request readiness
A change is ready for review when:
- the Python validation script runs successfully;
- the edited file is the correct source file;
- URIs remain stable;
- labels and definitions are consistent;
- documentation is updated if the modelling rules changed.