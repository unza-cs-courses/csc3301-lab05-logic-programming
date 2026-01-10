:- use_module(library(plunit)).
:- consult('../../src/task1_family.pl').
:- consult('../../src/task2_lists.pl').

:- begin_tests(family).
test(father) :- father(tom, mary).
test(grandparent) :- grandparent(tom, ann).
test(sibling) :- sibling(mary, james).
test(ancestor_direct) :- ancestor(tom, mary).
test(ancestor_indirect) :- ancestor(tom, jim).
:- end_tests(family).

:- begin_tests(lists).
test(append) :- my_append([1,2], [3,4], [1,2,3,4]).
test(reverse) :- my_reverse([1,2,3], [3,2,1]).
test(member) :- my_member(2, [1,2,3]).
test(length) :- my_length([a,b,c], 3).
:- end_tests(lists).
