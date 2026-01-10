# Lab 5: Logic Programming with Prolog

**CSC3301 Programming Language Paradigms**
**Student ID:** {{STUDENT_ID}}
**Points:** 100

## Your Personalized Assignment

Your variant has been automatically generated. The test cases below are unique to you.

## Prerequisites
- SWI-Prolog installed: `sudo apt install swi-prolog` or download from swi-prolog.org
- Verify: `swipl --version`

## Tasks

### Task 1: Family Tree (25 points)
Define facts and rules for family relationships.

Your family members:
- Grandparent: `{{GRANDPARENT}}`
- Parent 1: `{{PARENT1}}`
- Parent 2: `{{PARENT2}}`
- Child 1: `{{CHILD1}}`
- Child 2: `{{CHILD2}}`
- Child 3: `{{CHILD3}}`
- Grandchild: `{{GRANDCHILD}}`

Test queries your code must pass:
```prolog
?- father({{FATHER_TEST_PARENT}}, {{FATHER_TEST_CHILD}}).  % should succeed
?- grandparent({{GRANDPARENT_TEST_GP}}, {{GRANDPARENT_TEST_GC}}).  % should succeed
?- sibling({{SIBLING_TEST_1}}, {{SIBLING_TEST_2}}).  % should succeed
?- ancestor({{ANCESTOR_TEST_A}}, {{ANCESTOR_TEST_D}}).  % should succeed
```

Required predicates:
- `parent(X, Y)` - X is parent of Y
- `father(X, Y)` - X is father of Y
- `mother(X, Y)` - X is mother of Y
- `grandparent(X, Y)` - X is grandparent of Y
- `sibling(X, Y)` - X and Y are siblings
- `ancestor(X, Y)` - X is ancestor of Y

### Task 2: List Processing (30 points)
Implement list predicates WITHOUT using built-in predicates.

Your test values:
```prolog
?- my_append({{APPEND_LIST1}}, {{APPEND_LIST2}}, {{APPEND_RESULT}}).  % should succeed
?- my_reverse({{REVERSE_INPUT}}, {{REVERSE_RESULT}}).  % should succeed
?- my_member({{MEMBER_ELEMENT}}, {{MEMBER_LIST}}).  % should succeed
?- my_length({{LENGTH_LIST}}, {{LENGTH_RESULT}}).  % should succeed
```

Required predicates:
- `my_append(L1, L2, L3)` - L3 is L1 appended with L2
- `my_reverse(L1, L2)` - L2 is reverse of L1
- `my_member(X, L)` - X is member of L
- `my_length(L, N)` - N is length of L

### Task 3: Logic Puzzle (25 points)
Solve a constraint satisfaction puzzle using Prolog's backtracking.

### Task 4: Expression Evaluator (20 points)
Implement `eval/2` to evaluate arithmetic expressions represented as Prolog terms.

## Running Tests

```bash
# Run all visible tests
swipl -g "run_tests" -t halt tests/visible/test_lab5.pl
```

## Submission
Complete the implementation in `src/` and push your changes.
