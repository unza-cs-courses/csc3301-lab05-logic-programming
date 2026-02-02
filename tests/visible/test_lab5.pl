:- use_module(library(plunit)).
:- consult('../../src/task1_family.pl').
:- consult('../../src/task2_lists.pl').

:- begin_tests(family).
test(father) :- father(daniel, anna).
test(grandparent) :- grandparent(daniel, debra).
test(sibling) :- sibling(anna, justin).
test(ancestor_direct) :- ancestor(daniel, anna).
test(ancestor_indirect) :- ancestor(daniel, john).
:- end_tests(family).

:- begin_tests(lists).
test(append) :- my_append([2, 7, 16, 13], [32, 23], [2, 7, 16, 13, 32, 23]).
test(reverse) :- my_reverse([38, 45, 13, 10, 42], [42, 10, 13, 45, 38]).
test(member) :- my_member(17, [8, 24, 30, 17]).
test(length) :- my_length(['h', 'f', 'b', 'd', 'e'], 5).
:- end_tests(lists).
