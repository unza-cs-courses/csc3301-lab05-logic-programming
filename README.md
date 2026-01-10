# Lab 5: Logic Programming with Prolog

**CSC3301 Programming Language Paradigms**  
**Points:** 100

## Prerequisites
- SWI-Prolog installed: `sudo apt install swi-prolog` or download from swi-prolog.org
- Verify: `swipl --version`

## Tasks

### Task 1: Family Tree (25 points)
Define facts and rules for family relationships: parent, grandparent, sibling, cousin, ancestor.

### Task 2: List Processing (30 points)
Implement list predicates WITHOUT built-ins: my_append, my_reverse, my_member, my_length.

### Task 3: Logic Puzzle (25 points)
Solve a constraint satisfaction puzzle using Prolog's backtracking.

### Task 4: Expression Evaluator (20 points)
Implement eval/2 to evaluate arithmetic expressions represented as Prolog terms.

## Running Tests
```bash
swipl -g "run_tests" -t halt tests/test_lab5.pl
```
