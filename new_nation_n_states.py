# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 09:11:38 2023

@author: nba35
"""

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


def new_nation_n_states(num, region_filename, border_filename):
    new_nations = []
    index = 1
    state_pop = load_regions(region_filename)
    borders = load_borders(border_filename)
    now_state = {}
    now_border = copy.deepcopy(borders)
    now_state_dict_key = np.array(list(state_pop.keys()))
    now_state_dict_value = np.array(list(state_pop.values()))
    # If there is only one country that outnumber the assign number, it should be returned
    for state in state_pop.keys():
        pop = state_pop.get(state, 0)
        state = frozenset({state})
        now_state[state] = pop
    # If there is only one country that outnumber the assign number, it should be returned 
    if num == 1:
       target_state_list = now_state_dict_key[now_state_dict_value == now_state_dict_value.max()]
       new_nations = target_state_list
       new_nations = tuple(new_nations)
       max_pop = now_state_dict_value.max()
    # This is a "greedy" algorithm - we simply find the most populous
    # state bordering our candidate nation and append it to the list.
    while index < num:
        new_nations = []
        new_state_dict, new_border_dict = most_populous_neighbor(now_state, state_pop, now_border, borders)
        
        new_state_dict_key = np.array(list(new_state_dict.keys()))
        new_state_dict_value = np.array(list(new_state_dict.values()))
        target_state_list = new_state_dict_key[new_state_dict_value == new_state_dict_value.max()]
        max_pop = new_state_dict_value.max()
        
        index += 1
        now_state = new_state_dict
        now_border = new_border_dict
        # if plus biggest can not more than target delete it! not work
        new_nations = target_state_list  
        new_nations = tuple(list(new_nations)[0])
    return (new_nations, max_pop) 

new_nation_n_states(1, r"C:\Users\nba35\OneDrive\桌面\python\chanllenge\usstates.csv", r"C:\Users\nba35\OneDrive\桌面\python\chanllenge\border_data.csv")
    


