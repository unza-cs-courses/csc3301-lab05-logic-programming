# Lab 5: Logic Programming with Prolog

**CSC3301 Programming Language Paradigms**
**Student ID:** programming
**Estimated Time:** 1.5-2 hours
**Points:** 100

---

## Your Unique Variant

This assignment has been personalized for you. Your specific family tree and test values are unique to your student ID.

### Your Family Tree

Your Prolog facts define this family structure:

| Role | Name |
|------|------|
| Grandparent | `daniel` |
| Parent 1 | `anna` |
| Parent 2 | `justin` |
| Child 1 | `debra` |
| Child 2 | `jeffrey` |
| Child 3 | `david` |
| Grandchild | `john` |

### Your Test Cases

**Family Relationship Tests:**
```prolog
?- father(daniel, anna).  % should succeed
?- grandparent(daniel, debra).  % should succeed
?- sibling(anna, justin).  % should succeed
?- ancestor(daniel, john).  % should succeed
```

**List Operation Tests:**
```prolog
?- my_append([2,7,16,13], [32,23], [2,7,16,13,32,23]).  % should succeed
?- my_reverse([38,45,13,10,42], [42,10,13,45,38]).  % should succeed
?- my_member(17, [8,24,30,17]).  % should succeed
?- my_length([h,f,b,d,e], 5).  % should succeed
```

**Important:** Your code must work with these exact values to pass the tests.

---

## Prerequisites

- SWI-Prolog installed: `sudo apt install swi-prolog` or download from swi-prolog.org
- Verify: `swipl --version`

---

## Tasks

### Task 1: Family Tree Rules (25 points)

Open `src/task1_family.pl`. The family facts have been defined for you. Implement these relationship rules:

1. **`father(X, Y)`** - X is the father of Y
   - X is a parent of Y AND X is male

2. **`mother(X, Y)`** - X is the mother of Y
   - X is a parent of Y AND X is female

3. **`grandparent(X, Y)`** - X is a grandparent of Y
   - X is a parent of someone who is a parent of Y

4. **`sibling(X, Y)`** - X and Y are siblings
   - X and Y share a parent AND X is not the same as Y

5. **`ancestor(X, Y)`** - X is an ancestor of Y (recursive!)
   - Base case: X is a parent of Y
   - Recursive case: X is a parent of someone who is an ancestor of Y

### Task 2: List Processing (30 points)

Open `src/task2_lists.pl`. Implement these list predicates WITHOUT using built-in predicates:

1. **`my_append(L1, L2, L3)`** - L3 is L1 concatenated with L2
   - Base case: appending to empty list
   - Recursive case: process head, recurse on tail

2. **`my_reverse(List, Reversed)`** - Reversed is List in reverse order
   - Use an accumulator for O(n) performance
   - Hint: Define a helper predicate `my_reverse(List, Acc, Reversed)`

3. **`my_member(X, List)`** - X is a member of List
   - Base case: X is the head
   - Recursive case: X is in the tail

4. **`my_length(List, N)`** - N is the length of List
   - Base case: empty list has length 0
   - Recursive case: length is 1 + length of tail

### Task 3: Logic Puzzle (25 points)

Open `src/task3_puzzle.pl`. Solve the following constraint satisfaction puzzle using Prolog's backtracking:

**The Puzzle:** Three people (Alice, Bob, Carol) each have a different pet (cat, dog, fish) and drink a different beverage (coffee, tea, juice).

Given clues:
- Alice doesn't have the cat
- The coffee drinker has the dog
- Carol drinks tea
- Bob doesn't drink juice

Implement `solve_puzzle(Solution)` where Solution is a list of person-pet-drink triples.

### Task 4: Expression Evaluator (20 points)

Open `src/task4_eval.pl`. Implement `eval(Expr, Value)` to evaluate arithmetic expressions represented as Prolog terms:

- `num(N)` - a number N
- `add(E1, E2)` - addition
- `sub(E1, E2)` - subtraction
- `mul(E1, E2)` - multiplication
- `div(E1, E2)` - division (integer)

**Example:**
```prolog
?- eval(add(num(2), mul(num(3), num(4))), V).
V = 14.
```

---

## Running Tests

```bash
# Run all visible tests
swipl -g "run_tests" -t halt tests/visible/test_lab5.pl

# Load your code interactively
swipl
?- consult('src/task1_family.pl').
?- father(daniel, anna).
```

---

## Submission

1. Complete all tasks in the `src/` directory
2. Ensure all visible tests pass
3. Push your changes to trigger autograding
4. **Note:** Hidden tests will run after the deadline

---

## Grading Breakdown

| Component | Points | Type |
|-----------|--------|------|
| Visible Tests | 40 | Automatic |
| Hidden Tests | 30 | After deadline |
| Code Quality | 20 | Manual review |
| Plagiarism Check | -10 | Penalty if flagged |
| **Total** | 100 | |

---

## Prolog Tips

1. **Unification:** Variables start with uppercase, atoms with lowercase
2. **Backtracking:** Prolog tries all possibilities automatically
3. **Cut (!):** Use sparingly to prevent unwanted backtracking
4. **Recursion:** Most list operations need a base case and recursive case
5. **Testing:** Use `?-` queries to test predicates interactively

---

## Academic Integrity

- Discuss concepts with classmates: allowed
- Use Prolog documentation: allowed
- Share or copy code: not allowed
- Use AI tools to generate solutions: not allowed

Your submission will be checked for similarity with other students.
