#!/usr/bin/env python3
"""
Generate personalized ASSIGNMENT.md from template.
CSC3301 Programming Language Paradigms - Lab 5: Logic Programming
"""
import json
from pathlib import Path


def format_prolog_list(lst):
    """Format a Python list as a Prolog list string."""
    if all(isinstance(x, str) for x in lst):
        return '[' + ','.join(lst) + ']'
    return '[' + ','.join(str(x) for x in lst) + ']'


def main():
    repo_root = Path(__file__).parent.parent

    # Load variant config
    config_path = repo_root / ".variant_config.json"
    if not config_path.exists():
        print("No variant config found. Run variant_generator.py first.")
        return

    with open(config_path) as f:
        variant = json.load(f)

    # Load template
    template_path = repo_root / "ASSIGNMENT_TEMPLATE.md"
    if not template_path.exists():
        print("No assignment template found.")
        return

    template = template_path.read_text()

    # Replace placeholders
    family = variant["family_tree"]
    tests = variant["family_tests"]
    list_tests = variant["list_tests"]

    assignment = template
    assignment = assignment.replace("{{STUDENT_ID}}", variant["student_id"])

    # Family tree placeholders
    assignment = assignment.replace("{{GRANDPARENT}}", family["grandparent"])
    assignment = assignment.replace("{{PARENT1}}", family["parent1"])
    assignment = assignment.replace("{{PARENT2}}", family["parent2"])
    assignment = assignment.replace("{{CHILD1}}", family["child1"])
    assignment = assignment.replace("{{CHILD2}}", family["child2"])
    assignment = assignment.replace("{{CHILD3}}", family["child3"])
    assignment = assignment.replace("{{GRANDCHILD}}", family["grandchild"])

    # Test case placeholders
    assignment = assignment.replace("{{FATHER_TEST_PARENT}}", tests["father_test"][0])
    assignment = assignment.replace("{{FATHER_TEST_CHILD}}", tests["father_test"][1])
    assignment = assignment.replace("{{GRANDPARENT_TEST_GP}}", tests["grandparent_test"][0])
    assignment = assignment.replace("{{GRANDPARENT_TEST_GC}}", tests["grandparent_test"][1])
    assignment = assignment.replace("{{SIBLING_TEST_1}}", tests["sibling_test"][0])
    assignment = assignment.replace("{{SIBLING_TEST_2}}", tests["sibling_test"][1])
    assignment = assignment.replace("{{ANCESTOR_TEST_A}}", tests["ancestor_indirect"][0])
    assignment = assignment.replace("{{ANCESTOR_TEST_D}}", tests["ancestor_indirect"][1])

    # List test placeholders
    assignment = assignment.replace("{{APPEND_LIST1}}", format_prolog_list(list_tests["append"]["list1"]))
    assignment = assignment.replace("{{APPEND_LIST2}}", format_prolog_list(list_tests["append"]["list2"]))
    assignment = assignment.replace("{{APPEND_RESULT}}", format_prolog_list(list_tests["append"]["result"]))
    assignment = assignment.replace("{{REVERSE_INPUT}}", format_prolog_list(list_tests["reverse"]["input"]))
    assignment = assignment.replace("{{REVERSE_RESULT}}", format_prolog_list(list_tests["reverse"]["result"]))
    assignment = assignment.replace("{{MEMBER_ELEMENT}}", str(list_tests["member"]["element"]))
    assignment = assignment.replace("{{MEMBER_LIST}}", format_prolog_list(list_tests["member"]["list"]))
    assignment = assignment.replace("{{LENGTH_LIST}}", format_prolog_list(list_tests["length"]["list"]))
    assignment = assignment.replace("{{LENGTH_RESULT}}", str(list_tests["length"]["result"]))

    # Write personalized assignment
    output_path = repo_root / "ASSIGNMENT.md"
    output_path.write_text(assignment)
    print(f"Generated personalized assignment: {output_path}")


if __name__ == "__main__":
    main()
