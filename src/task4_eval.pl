%
% Task 4: Expression Evaluator
%
% This module implements an interpreter for a simple arithmetic expression language.
%
% Expression Format:
% ------------------
% Expressions are represented as Prolog terms:
%   - num(N)              : A number N
%   - add(E1, E2)         : Addition of E1 and E2
%   - sub(E1, E2)         : Subtraction of E1 from E2
%   - mul(E1, E2)         : Multiplication of E1 and E2
%   - div(E1, E2)         : Integer division of E1 by E2
%
% Examples:
%   num(42)               evaluates to 42
%   add(num(2), num(3))   evaluates to 5
%   mul(num(3), num(4))   evaluates to 12
%   add(num(2), mul(num(3), num(4)))  evaluates to 14
%
% Your Task:
% ----------
% Implement eval_expr(Expr, Value) that:
%   - Takes an expression (Expr) as input
%   - Returns the numeric result (Value)
%   - Handles nested expressions through recursion
%
% Strategy:
% 1. Base case: num(N) directly evaluates to N
% 2. Recursive cases: Evaluate subexpressions, then apply the operator
%

% Base case: A number evaluates to itself
eval_expr(num(N), N).

% TODO: Add case for addition
% eval_expr(add(E1, E2), Value) :-
%     eval_expr(E1, V1),
%     eval_expr(E2, V2),
%     Value is V1 + V2.

% TODO: Add case for subtraction
% eval_expr(sub(E1, E2), Value) :-
%     ...

% TODO: Add case for multiplication
% eval_expr(mul(E1, E2), Value) :-
%     ...

% TODO: Add case for division
% eval_expr(div(E1, E2), Value) :-
%     ...

%
% Example test cases:
% ?- eval_expr(num(42), V).
% V = 42.
%
% ?- eval_expr(add(num(2), num(3)), V).
% V = 5.
%
% ?- eval_expr(add(num(2), mul(num(3), num(4))), V).
% V = 14.
%
