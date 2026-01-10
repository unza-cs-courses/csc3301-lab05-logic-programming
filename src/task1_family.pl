% Lab 5 Task 1: Family Tree
% Define facts for a family and implement relationship rules.

% Facts: parent(Parent, Child)
parent(tom, mary).
parent(tom, james).
parent(mary, ann).
parent(mary, pat).
parent(pat, jim).

% Facts: male/female
male(tom).
male(james).
male(pat).
male(jim).
female(mary).
female(ann).

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
% ?- father(tom, mary).  % true
% ?- grandparent(tom, ann).  % true
% ?- sibling(mary, james).  % true
% ?- ancestor(tom, jim).  % true
