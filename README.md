# Lab 5: Logic Programming with Prolog

**CSC3301 Programming Language Paradigms**
**Points:** 100

## Overview

This lab introduces logic programming with Prolog. You will implement family relationship rules, list processing predicates, solve a logic puzzle, and build an expression evaluator.

## Variant System

This assignment uses a **variant-based assessment system**. When you accept this assignment through GitHub Classroom:

1. A GitHub Action automatically generates your unique variant
2. Your personal `ASSIGNMENT.md` file is created with your specific:
   - Family tree names and relationships
   - List operation test values
3. Tests are customized to your variant

**Important:** Always refer to your `ASSIGNMENT.md` file for your specific test cases.

## Environment Setup

### Installing SWI-Prolog

#### macOS
```bash
brew install swi-prolog
```

#### Ubuntu/Debian
```bash
sudo apt install swi-prolog
```

#### Windows
Download the installer from [swi-prolog.org](https://www.swi-prolog.org/download/stable) and follow the installation wizard.

### Verify Installation

```bash
swipl --version
```

You should see output like: `SWI-Prolog version 9.x.x`

### Running Tests

Run all visible tests:
```bash
swipl -g "run_tests" -t halt tests/visible/test_lab5.pl
```

### Interactive Development

Start the SWI-Prolog interactive shell:
```bash
swipl
```

Then load your code:
```prolog
?- consult('src/task1_family.pl').
?- consult('src/task2_lists.pl').
```

### Debugging Tips

#### Enable Tracing
Step through your predicates to debug execution:
```prolog
?- trace.
?- father(X, Y).
?- notrace.
```

#### List Predicate Definitions
View all clauses of a predicate:
```prolog
?- listing(ancestor/2).
?- listing(my_append/3).
```

#### Common Prolog Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `Undefined procedure` | Predicate not defined or wrong arity | Check predicate name and number of arguments |
| `Instantiation error` | Variable should be instantiated | Ensure variables are bound before use |
| `Syntax error` | Typo or missing punctuation | Check parentheses, periods, and commas |
| `False` | Query fails | Use `trace` to debug the execution path |
| `Infinite loop` | Infinite recursion without base case | Add a base case to prevent infinite backtracking |

## Repository Structure

```
.
├── .github/
│   └── workflows/
│       ├── autograding.yml      # Runs tests on push
│       └── generate-variant.yml # Generates your unique variant
├── scripts/
│   ├── variant_generator.py     # Generates variant config
│   └── generate_assignment.py   # Creates personalized ASSIGNMENT.md
├── src/
│   ├── task1_family.pl          # Family tree (your facts are here)
│   └── task2_lists.pl           # List processing predicates
├── tests/
│   └── visible/
│       └── test_lab5.pl         # Visible test cases
├── .variant_config.json         # Your variant configuration (generated)
├── ASSIGNMENT.md                # Your personalized assignment (generated)
├── ASSIGNMENT_TEMPLATE.md       # Template for assignment generation
└── README.md                    # This file
```

## Tasks

### Task 1: Family Tree (25 points)
Define rules for family relationships using the facts provided in your variant:
- `father(X, Y)` - X is father of Y
- `mother(X, Y)` - X is mother of Y
- `grandparent(X, Y)` - X is grandparent of Y
- `sibling(X, Y)` - X and Y are siblings
- `ancestor(X, Y)` - X is ancestor of Y (recursive)

### Task 2: List Processing (30 points)
Implement list predicates WITHOUT built-ins:
- `my_append(L1, L2, L3)` - concatenate lists
- `my_reverse(L1, L2)` - reverse a list
- `my_member(X, L)` - check membership
- `my_length(L, N)` - compute length

### Task 3: Logic Puzzle (25 points)
Solve a constraint satisfaction puzzle using Prolog's backtracking.

### Task 4: Expression Evaluator (20 points)
Implement `eval/2` to evaluate arithmetic expressions represented as Prolog terms.

## Running Tests

```bash
# Run all visible tests
swipl -g "run_tests" -t halt tests/visible/test_lab5.pl

# Load and test interactively
swipl
?- consult('src/task1_family.pl').
?- father(X, Y).
```

## Submission

1. Complete all tasks in the `src/` directory
2. Ensure all visible tests pass locally
3. Push your changes to trigger autograding
4. Check the Actions tab for test results

## Grading

| Component | Points |
|-----------|--------|
| Visible Tests | 40 |
| Hidden Tests | 30 |
| Code Quality | 20 |
| Plagiarism Check | -10 (if flagged) |
| **Total** | 100 |

## Academic Integrity

- Discuss concepts with classmates: allowed
- Use Prolog documentation: allowed
- Share or copy code: not allowed
- Use AI tools to generate solutions: not allowed

Your unique variant ensures your solution is personalized. Submissions will be checked for similarity.
