%
% Task 3: Logic Puzzle - Constraint Satisfaction
%
% This module implements a constraint satisfaction problem (CSP) using Prolog.
%
% The Puzzle:
% -----------
% Three people (Alice, Bob, Carol) each have a different pet (cat, dog, fish)
% and drink a different beverage (coffee, tea, juice).
%
% Constraints:
% 1. Alice doesn't have the cat
% 2. The coffee drinker has the dog
% 3. Carol drinks tea
% 4. Bob doesn't drink juice
%
% Your Task:
% ----------
% Implement solve_puzzle(Solution) where Solution unifies with a list of
% person-pet-drink triples that satisfy all constraints.
%
% The solution should be a list of three tuples:
%   [person(alice, pet_X, drink_Y), person(bob, pet_A, drink_B), person(carol, pet_C, drink_D)]
%
% Key Concepts:
% - Use member/2 to generate possible assignments
% - Use permutation/2 to ensure all items are different
% - Unify multiple solutions to prune the search space
% - Prolog's backtracking will find all valid solutions
%

% TODO: Implement member/2 predicate if not using built-in
% member(X, [X|_]).
% member(X, [_|T]) :- member(X, T).

% TODO: Implement permutation/2 predicate if not using built-in
% permutation([], []).
% permutation(L, [H|T]) :-
%     select(H, L, Rest),
%     permutation(Rest, T).

solve_puzzle(Solution) :-
    % TODO: Define the solution structure
    % Your solution should be a list with three elements:
    % - A person-pet-drink triple for Alice
    % - A person-pet-drink triple for Bob
    % - A person-pet-drink triple for Carol
    %
    % Each triple should be structured as: person(Name, Pet, Drink)
    % Example: person(alice, dog, coffee)
    %
    % Hints:
    % 1. Generate permutations of pets and drinks
    % 2. For each combination, check all constraints
    % 3. Unify Solution with the valid combination
    %
    % Constraint checking:
    % - Alice doesn't have the cat: Pet \= cat (for Alice)
    % - The coffee drinker has the dog: Use a rule like coffee_drinker_has_dog
    % - Carol drinks tea: Drink = tea (for Carol)
    % - Bob doesn't drink juice: Drink \= juice (for Bob)

    true.  % TODO: Replace with actual implementation

%
% Helper predicates you might want to define:
%

% TODO: Add helper predicate to check if coffee drinker has dog
% coffee_drinker_has_dog(Solution) :-
%     member(person(_, dog, coffee), Solution).

% TODO: Add any other helper predicates needed
