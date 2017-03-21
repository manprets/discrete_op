#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_graph(node_count, edge_count, edges):
    print "node_count: ", node_count
    print "edge_count: ", edge_count, "\n"
    
    for edge in edges:
        print str(edge[0])+str('---->')+str(edge[1])
    print '\n'

def print_solution(solution):
    print "solution:"
    print solution
    print "\n"

def do_greedy_algo(node_count, edge_count, edges):
    #1. Color first vertex with first color.
    #2. Do following for remaining V-1 vertices.
    #     a) Consider the currently picked vertex and color it with the 
    #        lowest numbered color that has not been used on any previously
    #        colored vertices adjacent to it. If all previously used colors 
    #        appear on vertices adjacent to v, assign a new color to it.
    colors = [-1]*node_count
    
    for i in range(node_count):
        #print i
        if i==0:
            colors[i]=0
         else:
            #is 
         
    

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))

    print_graph(node_count, edge_count, edges)
		
    # build a trivial solution
    # every node has its own color
    #solution = range(0, node_count)
    if node_count<=10:
        solution = do_greedy_algo(node_count, edge_count, edges)
    else:
        solution = range(0, node_count)

    print_solution(solution)

    

    # prepare the solution in the specified output format
    output_data = str(node_count) + ' ' + str(0) + '\n'
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
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')

