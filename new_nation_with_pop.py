# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 22:45:55 2023

@author: nba35
"""


import csv
import numpy as np
import copy


def load_regions(filename):
    states_dict = dict()

    with open(filename, 'r') as f:
        for line in csv.reader(f):
            states_dict[line[1]] = int(line[3])

    return states_dict


def load_borders(filename):
    border_dict = {}
    with open(filename, 'r') as f:
        for line in csv.reader(f, 1):
            states = line[1].split('-')
            if len(states) == 2:
                border_dict.setdefault(frozenset({states[0]}), set()).add(states[1])
                border_dict.setdefault(frozenset({states[1]}), set()).add(states[0])
    return border_dict


def most_populous_neighbor(now_state_dict, pop_dict, now_border_dict, borders_dict):
    new_state_pop_dict = {}
    new_border_dict = {}
    for now_state in now_state_dict.keys():
        from_state = frozenset({list(now_state)[-1]})
        now_border = now_border_dict.get(now_state, set()).copy()
        now_state = set(now_state)

        if from_state in borders_dict.keys():
            neighbor_border = borders_dict.get(from_state)
            now_border.update(neighbor_border)
        else:
            continue

        for border in now_border:
            neighbor_pop = pop_dict.get(border, 0)
            key = now_state.union({border})
            key = frozenset(key)
            if new_state_pop_dict.get(key, 0) == 0 and len(key) > len(now_state):               
                new_state_pop_dict[key] = now_state_dict.get(frozenset(now_state)) + neighbor_pop
                new_border_dict[key] = now_border

    return new_state_pop_dict, new_border_dict


def new_nation_with_pop(p, region_filename, border_filename):
    new_nations = []
    flag = 0
    state_pop = load_regions(region_filename)
    borders = load_borders(border_filename)
    now_state = {}
    now_border = copy.deepcopy(borders)
    # If there is only one country that outnumber the assign number, it should be returned
    for state in state_pop.keys():
        pop = state_pop.get(state, 0)
        if pop >= p * 10 ** 6:
            new_nations.append((state,))
            flag = 1
        state = frozenset({state})
        now_state[state] = pop

    # This is a "greedy" algorithm - we simply find the most populous
    # state bordering our candidate nation and append it to the list.
    while flag == 0:
        target_state_list = []
        new_state_dict, new_border_dict = most_populous_neighbor(now_state, state_pop, now_border, borders)
        new_state_dict_key = np.array(list(new_state_dict.keys()))
        new_state_dict_value = np.array(list(new_state_dict.values()))
        target_state_list = new_state_dict_key[new_state_dict_value >= p * 10 ** 6]

        if target_state_list.size > 0:
            new_nations = target_state_list
            flag = 1

        now_state = new_state_dict
        now_border = new_border_dict
    return new_nations

new_nation_with_pop(40, r"C:\Users\nba35\OneDrive\桌面\python\chanllenge\usstates.csv", r"C:\Users\nba35\OneDrive\桌面\python\chanllenge\border_data.csv")


# Remove and return the value associated with the key 'b'
# If the key is not found, you can provide a default value as the second argument.
# If the key is not found and no default value is provided, it will raise a KeyError.

print(my_dict)  # Output
a = {'12','23','34'}
a[-1]
B = 'AB'
B = {B}
B.add('AB')
B.add('BC')
B
A = frozenset({'a', 'b'})
C = {'a'}
len(A)
len(C)
print(type(A))
A = {A}
C = {'a', 'b'}
B = frozenset(['a', 'c'])
dict1 = {}
dict1[A] = 0
dict1[B] = 2
dict1
dict1.get(frozenset(C))

a = {A:2, B:3}
a.keys()
for num in a.keys():
    print(list(num))
b = a.add(5)
a
a.add(5)

set1 = {1, 2, 3, 4}
set2 = 3
set4 = 5

# Using union() method to return a new set containing the union of set1 and set2
union_result = set1.union({set2})
union_result
