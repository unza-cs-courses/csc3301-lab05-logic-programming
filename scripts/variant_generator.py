#!/usr/bin/env python3
"""
Variant Generator for Lab 5: Logic Programming with Prolog
CSC3301 Programming Language Paradigms

Generates unique Prolog-specific variants based on student ID.
Each student gets deterministic but unique family relationships
and list operation test values.
"""
import hashlib
import json
import sys
import random
from pathlib import Path


# Name pools for family tree generation
FIRST_NAMES_MALE = [
    'james', 'john', 'robert', 'michael', 'david', 'william', 'richard',
    'thomas', 'charles', 'daniel', 'matthew', 'anthony', 'mark', 'steven',
    'paul', 'andrew', 'joshua', 'kenneth', 'kevin', 'brian', 'george',
    'timothy', 'ronald', 'edward', 'jason', 'jeffrey', 'ryan', 'jacob',
    'gary', 'nicholas', 'eric', 'jonathan', 'stephen', 'larry', 'justin',
    'scott', 'brandon', 'benjamin', 'samuel', 'raymond', 'gregory', 'frank',
    'alexander', 'patrick', 'jack', 'dennis', 'jerry', 'tyler', 'aaron'
]

FIRST_NAMES_FEMALE = [
    'mary', 'patricia', 'jennifer', 'linda', 'elizabeth', 'barbara',
    'susan', 'jessica', 'sarah', 'karen', 'lisa', 'nancy', 'betty',
    'margaret', 'sandra', 'ashley', 'kimberly', 'emily', 'donna', 'michelle',
    'dorothy', 'carol', 'amanda', 'melissa', 'deborah', 'stephanie', 'rebecca',
    'sharon', 'laura', 'cynthia', 'kathleen', 'amy', 'angela', 'shirley',
    'anna', 'brenda', 'pamela', 'emma', 'nicole', 'helen', 'samantha',
    'katherine', 'christine', 'debra', 'rachel', 'carolyn', 'janet', 'catherine'
]


def generate_family_tree(rng):
    """
    Generate a unique family tree with consistent relationships.
    Returns family members and their relationships.
    """
    # Select unique names for family members
    males = rng.sample(FIRST_NAMES_MALE, 6)
    females = rng.sample(FIRST_NAMES_FEMALE, 4)

    # Family structure:
    # Generation 1: grandparent1 (male)
    # Generation 2: parent1 (child of grandparent1), parent2 (spouse)
    # Generation 3: child1, child2, child3 (children of parent1)
    # Generation 4: grandchild1 (child of child1)

    grandparent1 = males[0]  # male grandparent
    parent1 = females[0]     # daughter of grandparent
    parent2 = males[1]       # spouse (son of grandparent - sibling)
    child1 = females[1]      # grandchild
    child2 = males[2]        # grandchild
    child3 = males[3]        # great-grandchild's parent
    grandchild1 = males[4]   # great-grandchild

    family = {
        'grandparent1': grandparent1,
        'parent1': parent1,
        'parent2': parent2,
        'child1': child1,
        'child2': child2,
        'child3': child3,
        'grandchild1': grandchild1,
        'males': [grandparent1, parent2, child2, child3, grandchild1],
        'females': [parent1, child1]
    }

    # Define parent relationships
    # grandparent1 is parent of parent1 and parent2
    # parent1 is parent of child1, child2
    # child3 is parent of grandchild1
    parents = [
        (grandparent1, parent1),
        (grandparent1, parent2),
        (parent1, child1),
        (parent1, child2),
        (child3, grandchild1)
    ]

    family['parent_facts'] = parents

    # Test cases
    family['tests'] = {
        'father_test': (grandparent1, parent1),  # grandparent is father of parent1
        'grandparent_test': (grandparent1, child1),  # grandparent is grandparent of child1
        'sibling_test': (parent1, parent2),  # parent1 and parent2 are siblings
        'ancestor_direct': (grandparent1, parent1),  # direct ancestor
        'ancestor_indirect': (grandparent1, grandchild1)  # indirect through chain
    }

    return family


def generate_list_tests(rng):
    """
    Generate unique list operation test values.
    """
    # Generate unique list values for append test
    append_list1_len = rng.randint(2, 4)
    append_list2_len = rng.randint(2, 4)
    append_list1 = [rng.randint(1, 20) for _ in range(append_list1_len)]
    append_list2 = [rng.randint(21, 40) for _ in range(append_list2_len)]
    append_result = append_list1 + append_list2

    # Generate unique list for reverse test
    reverse_len = rng.randint(3, 5)
    reverse_list = [rng.randint(1, 50) for _ in range(reverse_len)]
    reverse_result = list(reversed(reverse_list))

    # Generate member test
    member_list = [rng.randint(1, 30) for _ in range(4)]
    member_element = rng.choice(member_list)

    # Generate length test
    length_elements = rng.sample(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], rng.randint(3, 6))

    return {
        'append': {
            'list1': append_list1,
            'list2': append_list2,
            'result': append_result
        },
        'reverse': {
            'input': reverse_list,
            'result': reverse_result
        },
        'member': {
            'element': member_element,
            'list': member_list
        },
        'length': {
            'list': length_elements,
            'result': len(length_elements)
        }
    }


def generate_variant(student_id: str) -> dict:
    """
    Generate a unique variant configuration based on student ID.

    Uses deterministic hashing so the same student ID always
    produces the same variant.
    """
    # Create deterministic seed from student ID
    seed = int(hashlib.sha256(student_id.encode()).hexdigest(), 16) % (2**32)
    rng = random.Random(seed)

    # Generate family tree
    family = generate_family_tree(rng)

    # Generate list tests
    list_tests = generate_list_tests(rng)

    variant = {
        "student_id": student_id,
        "variant_seed": seed,
        "family_tree": {
            "grandparent": family['grandparent1'],
            "parent1": family['parent1'],
            "parent2": family['parent2'],
            "child1": family['child1'],
            "child2": family['child2'],
            "child3": family['child3'],
            "grandchild": family['grandchild1'],
            "males": family['males'],
            "females": family['females'],
            "parent_facts": family['parent_facts']
        },
        "family_tests": family['tests'],
        "list_tests": list_tests
    }

    return variant


def update_source_files(variant: dict, repo_root: Path):
    """
    Update Prolog source files with variant-specific values.
    """
    family = variant["family_tree"]

    # Update task1_family.pl with variant-specific family facts
    task1_path = repo_root / "src" / "task1_family.pl"
    if task1_path.exists():
        # Generate new content with variant family
        content = f'''% Lab 5 Task 1: Family Tree
% Define facts for a family and implement relationship rules.

% Facts: parent(Parent, Child)
'''
        for parent, child in family['parent_facts']:
            content += f"parent({parent}, {child}).\n"

        content += "\n% Facts: male/female\n"
        for male in family['males']:
            content += f"male({male}).\n"
        for female in family['females']:
            content += f"female({female}).\n"

        content += '''
% YOUR TASK: Implement these rules

% father(X, Y) - X is father of Y
% father(X, Y) :- YOUR CODE HERE

% mother(X, Y) - X is mother of Y
% mother(X, Y) :- YOUR CODE HERE

% grandparent(X, Y) - X is grandparent of Y
% grandparent(X, Y) :- YOUR CODE HERE

% sibling(X, Y) - X and Y are siblings (same parent, different people)
% sibling(X, Y) :- YOUR CODE HERE

% ancestor(X, Y) - X is ancestor of Y (recursive!)
% ancestor(X, Y) :- YOUR CODE HERE

% Test queries:
'''
        tests = variant["family_tests"]
        content += f"% ?- father({tests['father_test'][0]}, {tests['father_test'][1]}).  % true\n"
        content += f"% ?- grandparent({tests['grandparent_test'][0]}, {tests['grandparent_test'][1]}).  % true\n"
        content += f"% ?- sibling({tests['sibling_test'][0]}, {tests['sibling_test'][1]}).  % true\n"
        content += f"% ?- ancestor({tests['ancestor_indirect'][0]}, {tests['ancestor_indirect'][1]}).  % true\n"

        task1_path.write_text(content)
        print(f"Updated {task1_path}")


def update_test_file(variant: dict, repo_root: Path):
    """
    Update test file with variant-specific test cases.
    """
    family = variant["family_tree"]
    tests = variant["family_tests"]
    list_tests = variant["list_tests"]

    test_path = repo_root / "tests" / "visible" / "test_lab5.pl"
    test_path.parent.mkdir(parents=True, exist_ok=True)

    content = f''':- use_module(library(plunit)).
:- consult('../../src/task1_family.pl').
:- consult('../../src/task2_lists.pl').

:- begin_tests(family).
test(father) :- father({tests['father_test'][0]}, {tests['father_test'][1]}).
test(grandparent) :- grandparent({tests['grandparent_test'][0]}, {tests['grandparent_test'][1]}).
test(sibling) :- sibling({tests['sibling_test'][0]}, {tests['sibling_test'][1]}).
test(ancestor_direct) :- ancestor({tests['ancestor_direct'][0]}, {tests['ancestor_direct'][1]}).
test(ancestor_indirect) :- ancestor({tests['ancestor_indirect'][0]}, {tests['ancestor_indirect'][1]}).
:- end_tests(family).

:- begin_tests(lists).
test(append) :- my_append({list_tests['append']['list1']}, {list_tests['append']['list2']}, {list_tests['append']['result']}).
test(reverse) :- my_reverse({list_tests['reverse']['input']}, {list_tests['reverse']['result']}).
test(member) :- my_member({list_tests['member']['element']}, {list_tests['member']['list']}).
test(length) :- my_length({list_tests['length']['list']}, {list_tests['length']['result']}).
:- end_tests(lists).
'''

    test_path.write_text(content)
    print(f"Updated {test_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python variant_generator.py <student_id>")
        print("Example: python variant_generator.py john_doe")
        sys.exit(1)

    student_id = sys.argv[1]
    repo_root = Path(__file__).parent.parent

    print(f"Generating variant for student: {student_id}")

    # Generate variant
    variant = generate_variant(student_id)

    # Save variant config
    config_path = repo_root / ".variant_config.json"
    with open(config_path, 'w') as f:
        json.dump(variant, f, indent=2)
    print(f"Saved variant config to {config_path}")

    # Update source files with variant values
    update_source_files(variant, repo_root)

    # Update test file
    update_test_file(variant, repo_root)

    # Display summary
    print("\n=== Variant Summary ===")
    print(f"Student ID: {variant['student_id']}")
    print(f"Seed: {variant['variant_seed']}")
    print(f"Family grandparent: {variant['family_tree']['grandparent']}")
    print(f"Family members: {variant['family_tree']['parent1']}, {variant['family_tree']['parent2']}, "
          f"{variant['family_tree']['child1']}, {variant['family_tree']['child2']}")
    print(f"List append test: {variant['list_tests']['append']['list1']} + {variant['list_tests']['append']['list2']}")
    print(f"List reverse test: {variant['list_tests']['reverse']['input']}")


if __name__ == "__main__":
    main()
