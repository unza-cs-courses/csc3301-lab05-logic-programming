% Lab 5 Task 2: List Processing
% Implement these WITHOUT using built-in predicates.

% my_append(L1, L2, L3) - L3 is L1 concatenated with L2
my_append([], L, L).
my_append([H|T], L, [H|R]) :- my_append(T, L, R).

% my_reverse(List, Reversed) - use accumulator for O(n)
% TODO: Implement my_reverse/2 with accumulator pattern
my_reverse(L, R) :- my_reverse_acc(L, [], R).
my_reverse_acc([], Acc, Acc).
my_reverse_acc([H|T], Acc, R) :- my_reverse_acc(T, [H|Acc], R).

% my_member(X, List) - X is a member of List
my_member(X, [X|_]).
my_member(X, [_|T]) :- my_member(X, T).

% my_length(List, N) - N is the length of List
my_length([], 0).
my_length([_|T], N) :- my_length(T, N1), N is N1 + 1.

% my_nth(N, List, Element) - Element is the Nth element of List (0-indexed)
% TODO: Implement my_nth/3
my_nth(0, [H|_], H).
my_nth(N, [_|T], E) :- N > 0, N1 is N - 1, my_nth(N1, T, E).
