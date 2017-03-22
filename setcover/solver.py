#!/usr/bin/python
# -*- coding: utf-8 -*-

# The MIT License (MIT)
#
# Copyright (c) 2014 Carleton Coffrin
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


from collections import namedtuple

Set = namedtuple("Set", ['index', 'cost', 'items'])

def get_trivial_solution(set_count,sets,item_count):
    # pick add sets one-by-one until all the items are covered
    solution = [0]*set_count
    coverted = set()
    
    for s in sets:
        solution[s.index] = 1
        coverted |= set(s.items)
        if len(coverted) >= item_count:
            break
    return solution

import operator
def get_next_item_density_based(set_count, items_covered, solution, sets, remove_these_sets):
    print 'set_count: {}, remove_these_sets: {}'.format(set_count,remove_these_sets)
    density_set = [-1]*set_count
    
    for idx_set in range(set_count):
        if idx_set in remove_these_sets:
            pass
        else:
            set_i = sets[idx_set]
            set_cost = set_i.cost
            set_items = set_i.items
            new_item_len = len(set(set_items)-set(items_covered))
            
            #handle set_cost = 0 case
            density_set[idx_set]=new_item_len/float(set_cost)
    
    print 'density_set: {}'.format(density_set)
    print 'items_covered: {}'.format(items_covered)
    
    index, value = max(enumerate(density_set), key=operator.itemgetter(1))
    print 'index: {}'.format(index)
    return index
    
def is_this_set_selectable(iset, sets, solution, items_covered):
    is_selectable = 0
    this_set = sets[iset]
    
    print 'this_set:{},items_covered:{}'.format(this_set,items_covered)
    items = this_set.items
    for item in items:
        if item in items_covered:
            is_selectable |= 0
        else:
            is_selectable |= 1
    
    return is_selectable
    
def populate_items_covered(solution, sets):
    items_covered=set()
    
    for idx_set in range(len(solution)):
        if solution[idx_set] == 1:
            set_i = sets[idx_set]
            set_items = set_i.items

            #for item in set_items:
            items_covered |= set(set_items)
    # items_covered has been populated
    items_covered = list(items_covered)
    
    return items_covered
    
def get_greedy_solution(set_count, sets, item_count):
    solution = [0]*set_count
    
    # create a list of length equal to num of sets 
    # assign it density (len_of_set/cost)
    # choose set with highest density
    remaining_sets = list(range(set_count))
    remove_these_sets = []
    items_covered = []
    while len(items_covered) < item_count:
        
        iset = get_next_item_density_based(set_count, items_covered, solution, sets, remove_these_sets)
        
        # find if this set can be selected
        #select_this_set = is_this_set_selectable(iset, sets, solution, items_covered)
        #if select_this_set:
        #solution[iset] = select_this_set
        solution[iset] = 1
        remaining_sets.remove(iset)
        remove_these_sets.append(iset)
        
        items_covered = populate_items_covered(solution, sets)
    
    return solution
    
def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    parts = lines[0].split()
    item_count = int(parts[0])
    set_count = int(parts[1])
    
    sets = []
    for i in range(1, set_count+1):
        parts = lines[i].split()
        sets.append(Set(i-1, float(parts[0]), map(int, parts[1:])))

    # print input
    for iset in range(set_count):
        set_p = sets[iset]
        print 'set_p {}'.format(set_p)
        
    # build a trivial solution
    # solution = get_trivial_solution(set_count,sets,item_count)
    
    # implement greedy solution
    solution = get_greedy_solution(set_count, sets, item_count)
      
    # calculate the cost of the solution
    obj = sum([s.cost*solution[s.index] for s in sets])

    # prepare the solution in the specified output format
    output_data = str(obj) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/sc_6_1)')

