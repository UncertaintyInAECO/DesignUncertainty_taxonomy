# Namespace policy

## Purpose

This policy documents the namespace declarations used in `taxonomy/extensions/design-uncertainty-annotations.ttl`.

The extension file adds research-specific classes, properties, and concept annotations to the taxonomy.

## Declared prefixes

The annotation file uses these prefixes:

```turtle
@prefix du:   <https://w3id.org/design-uncertainty/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
```

## Namespace usage

### `du:`
The `du:` namespace is used for:
- custom classes such as `du:Uncertainty`, `du:Mitigation`, `du:Nature`, `du:Object`, `du:Phase`, `du:Stakeholder`, and `du:ActionVerb`;
- custom properties such as `du:IsOfNature`, `du:addressesObject`, `du:emergesInPhase`, `du:introducedBy`, `du:performedByStakeholder`, `du:performedInPhase`, and `du:requiresAction`;
- concept URIs for the uncertainty and mitigation terms;
- supporting concepts for phases, stakeholders, objects, natures, and action verbs.

### `skos:`
The SKOS namespace is used for:
- `skos:Concept`;
- `skos:prefLabel`;
- `skos:definition`;
- `skos:broader`.

### `rdf:`
The RDF namespace is used for:
- class and property declarations, such as `rdf:Property`.

### `rdfs:`
The RDFS namespace is used for:
- class declarations, such as `rdfs:Class`;
- human-readable labels and schema constraints such as `rdfs:label`, `rdfs:domain`, and `rdfs:range`.

### `xsd:`
The XSD namespace is used for:
- typed literals such as `xsd:string`.

## URI style

The annotation file uses a stable, project-specific `du:` namespace.

Examples of adopted patterns:
- `du:U_T05`, `du:U_T06`, `du:U_T07` for taxonomy concepts;
- `du:nature_epistemic`, `du:nature_strategic`, `du:nature_aleatory` for analytical values;
- `du:phase_design`, `du:phase_briefing-requirements`, `du:phase_construction-execution` for lifecycle phases;
- `du:stakeholder_client-owner`, `du:stakeholder_designers` for actor categories;
- `du:object_requirements-brief`, `du:object_market-demand` for addressed objects;
- `du:verb_analyze`, `du:verb_define`, `du:verb_model` for action verbs.

## Naming rules

- Keep all extension identifiers under the `du:` namespace.
- Use consistent lowercase naming for non-code identifiers when new values are added.
- Preserve existing URIs when editing labels or definitions.
- Do not create a second namespace for the same extension file unless the model is explicitly restructured.

## Alignment rule

The namespace policy for the annotation file should not invent new namespaces that are not already used in the file.

Any future namespace expansion should be justified by a corresponding modelling need and documented before use.