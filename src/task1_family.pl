% Lab 5 Task 1: Family Tree
% Define facts for a family and implement relationship rules.

% Facts: parent(Parent, Child)
parent(daniel, anna).
parent(daniel, justin).
parent(anna, debra).
parent(anna, jeffrey).
parent(david, john).

% Facts: male/female
male(daniel).
male(justin).
male(jeffrey).
male(david).
male(john).
female(anna).
female(debra).

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
% ?- father(daniel, anna).  % true
% ?- grandparent(daniel, debra).  % true
% ?- sibling(anna, justin).  % true
% ?- ancestor(daniel, john).  % true
