#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def print_knapsack_info(items, item_count, capacity):
    print 'item_count:', item_count, ' K:', capacity
    print 'index\tvalue\tweight'
    for item in items:
        #print item.index, item.value, item.weight
        print str(item.index)+'\t'+str(item.value)+'\t'+str(item.weight)
    print '\n'

import numpy as np

def populate_T_arr(T,items,K):
    #K is capacity
    # dimension of T should be len(items), K+1
    n_rows,n_cols = T.shape
    
    for item in items:
        wt=item.weight
        val=item.value
        idx=item.index
        if idx==0:
            for jdx in range(n_cols):
                if jdx<wt:
                    T[idx][jdx]=0
                else:
                    T[idx][jdx]=val
        elif idx>0:
            for jdx in range(n_cols):
                if jdx<wt:
                    T[idx][jdx]=T[idx-1][jdx]
                else:
                    T[idx][jdx]=max(val+T[idx-1][jdx-wt],T[idx-1][jdx])


def get_chosen_items(T, items):
    n_rows,n_cols = T.shape
    
    chosen = [0]*n_rows
    
    max_val=T[n_rows-1][n_cols-1]
    lcol=n_cols-1
    lrow=n_rows-1
    #for lrow in range(n_rows-1,-1,-1):
    counter=0
    while(1):
        if lcol<=0 or lrow<0:
            break
        val=T[lrow][lcol]
        if counter==n_rows-1:
            if val>0:
                chosen[lrow]=1
                break
        
        val_up=T[lrow-1][lcol]
        #print counter,lrow,lcol,val,val_up
        
        if val>val_up:
            chosen[lrow]=1
            lcol=lcol-items[lrow].weight
        else:
            chosen[lrow]=0
        
        counter=counter+1
        lrow=lrow-1
        #print chosen,counter,lrow,lcol

    return chosen

def print_chosen(chosen):
    print 'chosen:'
    print chosen
    print '\n'

def print_T(T):
    n_rows,n_cols = T.shape
    print 'T:'
    for row in range(n_rows):
        row_str=''
        for col in range(n_cols):
            row_str=row_str+str(T[row][col])+str('\t')
        print row_str#T[row][col]
    print '\n'

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    #print_knapsack_info(items, item_count, capacity)
    
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)
    T = np.zeros((item_count,capacity+1), dtype=int)
    
    populate_T_arr(T,items,capacity)
    #print_T(T)
    
    taken = get_chosen_items(T,items)
    #print_chosen(taken)
    
    for idx in range(item_count):
        if taken[idx]==1:
            item=items[idx]
            value += item.value
            weight += item.weight
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

