#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict
import re
import sys

from rdflib import Graph, Namespace
from rdflib.namespace import RDF, SKOS

ROOT = Path(__file__).resolve().parents[1]
CORE_FILE = ROOT / "taxonomy" / "core" / "design-uncertainty.ttl"
EXT_FILE = ROOT / "taxonomy" / "extensions" / "design-uncertainty-annotations.ttl"
EXPORTS_DIR = ROOT / "taxonomy" / "exports"

DCT = Namespace("http://purl.org/dc/terms/")
OWL = Namespace("http://www.w3.org/2002/07/owl#")

errors = []
warnings = []


def load_graph(path: Path) -> Graph:
    g = Graph()
    try:
        g.parse(path, format="turtle")
        print(f"[OK] Parsed: {path}")
        return g
    except Exception as e:
        errors.append(f"Failed to parse {path}: {e}")
        return Graph()


def qname_or_str(graph: Graph, node):
    try:
        return graph.qname(node)
    except Exception:
        return str(node)


def is_taxonomy_concept(graph: Graph, node) -> bool:
    if (node, RDF.type, SKOS.Concept) not in graph:
        return False

    uri = str(node)
    return bool(re.search(r"/U_T\d+$", uri)) or uri.endswith("/Uncertainty") or uri.endswith("/Mitigation")


def check_core(core: Graph):
    schemes = list(core.subjects(RDF.type, SKOS.ConceptScheme))
    if not schemes:
        errors.append("Core file: no skos:ConceptScheme found.")
    elif len(schemes) > 1:
        warnings.append(f"Core file: multiple ConceptSchemes found ({len(schemes)}).")

    concepts = {c for c in core.subjects(RDF.type, SKOS.Concept) if is_taxonomy_concept(core, c)}
    if not concepts:
        errors.append("Core file: no skos:Concept found.")

    pref_labels = defaultdict(list)

    for concept in concepts:
        labels = list(core.objects(concept, SKOS.prefLabel))
        if not labels:
            errors.append(f"Core file: concept missing skos:prefLabel -> {qname_or_str(core, concept)}")

        for label in labels:
            lang = label.language or ""
            pref_labels[(str(label).strip().lower(), lang)].append(concept)

        in_schemes = list(core.objects(concept, SKOS.inScheme))
        if not in_schemes:
            warnings.append(f"Core file: concept missing skos:inScheme -> {qname_or_str(core, concept)}")

        broader = list(core.objects(concept, SKOS.broader))
        top_of = list(core.objects(concept, SKOS.topConceptOf))
        if not broader and not top_of:
            warnings.append(
                f"Core file: concept has neither skos:broader nor skos:topConceptOf -> {qname_or_str(core, concept)}"
            )

        defs = list(core.objects(concept, SKOS.definition))
        if not defs:
            warnings.append(f"Core file: concept missing skos:definition -> {qname_or_str(core, concept)}")

    for (label, lang), nodes in pref_labels.items():
        if len(nodes) > 1:
            joined = ", ".join(qname_or_str(core, n) for n in nodes)
            warnings.append(
                f"Core file: duplicate skos:prefLabel '{label}'@{lang or 'none'} used by: {joined}"
            )

    for child, parent in core.subject_objects(SKOS.broader):
        if (parent, RDF.type, SKOS.Concept) not in core:
            warnings.append(
                f"Core file: skos:broader target is not typed skos:Concept -> {qname_or_str(core, child)} -> {qname_or_str(core, parent)}"
            )
        if child == parent:
            errors.append(f"Core file: self-referential skos:broader -> {qname_or_str(core, child)}")


def check_extension(ext: Graph):
    concepts = {c for c in ext.subjects(RDF.type, SKOS.Concept) if is_taxonomy_concept(ext, c)}
    if not concepts:
        warnings.append("Extension file: no skos:Concept found.")

    for concept in concepts:
        labels = list(ext.objects(concept, SKOS.prefLabel))
        if not labels:
            warnings.append(f"Extension file: concept missing skos:prefLabel -> {qname_or_str(ext, concept)}")


def check_alignment(core: Graph, ext: Graph):
    core_concepts = {c for c in core.subjects(RDF.type, SKOS.Concept) if is_taxonomy_concept(core, c)}
    ext_concepts = {c for c in ext.subjects(RDF.type, SKOS.Concept) if is_taxonomy_concept(ext, c)}

    only_in_ext = sorted(ext_concepts - core_concepts, key=str)
    if only_in_ext:
        for c in only_in_ext:
            warnings.append(
                f"Alignment: concept appears in extension but not in core -> {qname_or_str(ext, c)}"
            )


def export_core(core: Graph):
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    rdf_path = EXPORTS_DIR / "design-uncertainty.rdf"
    jsonld_path = EXPORTS_DIR / "design-uncertainty.jsonld"

    try:
        core.serialize(destination=rdf_path, format="xml")
        print(f"[OK] Wrote export: {rdf_path}")
    except Exception as e:
        errors.append(f"Failed to write RDF/XML export: {e}")

    try:
        core.serialize(destination=jsonld_path, format="json-ld")
        print(f"[OK] Wrote export: {jsonld_path}")
    except Exception as e:
        errors.append(f"Failed to write JSON-LD export: {e}")


def main():
    if not CORE_FILE.exists():
        errors.append(f"Missing core file: {CORE_FILE}")
    if not EXT_FILE.exists():
        warnings.append(f"Missing extension file: {EXT_FILE}")

    core = load_graph(CORE_FILE) if CORE_FILE.exists() else Graph()
    ext = load_graph(EXT_FILE) if EXT_FILE.exists() else Graph()

    if len(core):
        check_core(core)
    if len(ext):
        check_extension(ext)
        check_alignment(core, ext)

    if len(core) and not errors:
        export_core(core)

    print("\n--- Validation report ---")
    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"- {w}")

    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"- {e}")
        sys.exit(1)

    print("\nValidation passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()