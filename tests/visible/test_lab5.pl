:- use_module(library(plunit)).
:- consult('../../src/task1_family.pl').
:- consult('../../src/task2_lists.pl').

:- begin_tests(family).
test(father) :- father(daniel, anna).
test(grandparent) :- grandparent(daniel, debra).
test(sibling) :- sibling(anna, justin).
test(ancestor_direct) :- ancestor(daniel, anna).
test(ancestor_indirect) :- ancestor(daniel, john).
test(father_basic_fact_1) :- father(daniel, anna).
test(father_basic_fact_2) :- father(daniel, justin).
test(mother_basic_fact) :- mother(anna, debra).
test(parent_rule) :- parent(daniel, anna).
test(grandparent_recursive) :- grandparent(daniel, debra).
:- end_tests(family).

:- begin_tests(lists).
test(append) :- my_append([2, 7, 16, 13], [32, 23], [2, 7, 16, 13, 32, 23]).
test(reverse) :- my_reverse([38, 45, 13, 10, 42], [42, 10, 13, 45, 38]).
test(member) :- my_member(17, [8, 24, 30, 17]).
test(length) :- my_length(['h', 'f', 'b', 'd', 'e'], 5).
test(append_empty_first) :- my_append([], [1, 2, 3], [1, 2, 3]).
test(append_empty_second) :- my_append([1, 2, 3], [], [1, 2, 3]).
test(member_head) :- my_member(1, [1, 2, 3]).
test(member_tail) :- my_member(3, [1, 2, 3]).
test(length_empty) :- my_length([], 0).
test(length_single) :- my_length([42], 1).
test(reverse_empty) :- my_reverse([], []).
test(reverse_single) :- my_reverse([42], [42]).
:- end_tests(lists).
