% Lab 5 Task 2: List Processing
% Implement these WITHOUT using built-in predicates.

% my_append(L1, L2, L3) - L3 is L1 concatenated with L2
% Hint: Base case - appending to an empty list. Recursive case - move head across.
% TODO: Implement my_append/3
my_append(_, _, _) :- fail.

% my_reverse(List, Reversed) - use accumulator for O(n)
% Hint: Use my_reverse_acc/3 with an initially empty accumulator.
% TODO: Implement my_reverse/2
my_reverse(_, _) :- fail.

% my_reverse_acc(List, Accumulator, Reversed) - helper with accumulator
% Hint: Move elements from List onto Accumulator one at a time.
% TODO: Implement my_reverse_acc/3
my_reverse_acc(_, _, _) :- fail.

% my_member(X, List) - X is a member of List
% Hint: X is a member if it's the head, or if it's in the tail.
% TODO: Implement my_member/2
my_member(_, _) :- fail.

% my_length(List, N) - N is the length of List
% Hint: Base case for empty list, recurse on tail and add 1.
% TODO: Implement my_length/2
my_length(_, _) :- fail.

% my_nth(N, List, Element) - Element is the Nth element of List (0-indexed)
% Hint: Base case when N=0 (take head). Recurse with N-1 on tail.
% TODO: Implement my_nth/3
my_nth(_, _, _) :- fail.
