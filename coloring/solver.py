#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_graph(node_count, edge_count, edges):
    print "node_count: ", node_count
    print "edge_count: ", edge_count, "\n"
    
    for edge in edges:
        print str(edge[0])+str('---->')+str(edge[1])
    print '\n'
    
def find_degree(node_count, edge_count, edges):
    degree_list=[0]*node_count
    
    for edge in edges:
        node0 = edge[0]
        node1 = edge[1]
        
        degree_list[node0] += 1
        degree_list[node1] += 1
    
    return degree_list

import numpy as np    
def build_adjacency_matrix(node_count, edge_count, edges):
    adj_mat = np.zeros((node_count,node_count),dtype=int)
    
    for edge in edges:
        node0 = edge[0]
        node1 = edge[1]
        adj_mat[node0][node1]=1
        adj_mat[node1][node0]=1
        
    return adj_mat

def print_adj_mat(adj_mat):
    nrows,ncols=adj_mat.shape
    print 'adj_mat:'
    print adj_mat
    print '\n'
    #for row in range(nrows):
    #    row=''
    #    for col in range(ncols):
    #        print adj_mat[row][col]
    #        row += str(adj_mat[row][col]) + '\t'
    #    print row
    
def print_degree_list(degree_list):
    print "degree:", degree_list
    print "max_degree: ", max(degree_list)
    print '\n'
    
    print sorted(range(len(degree_list)),key=lambda x:degree_list[x])
    print sorted(range(len(degree_list)),key=lambda x:degree_list[x],reverse=True)
    print '\n'
    
    
def greedy_algo_1(node_count,adj_mat):
    #1. Color first vertex with first color.
    #2. Do following for remaining V-1 vertices.
    #     a) Consider the currently picked vertex and color it with the 
    #        lowest numbered color that has not been used on any previously
    #        colored vertices adjacent to it. If all previously used colors 
    #        appear on vertices adjacent to v, assign a new color to it.
    colors = [-1]*node_count
    for node in range(node_count):
        if node==0:
            colors[node]=0
        else:
            adjacent=adj_mat[node]
            adj_nodes=[]
            for idx in range(1,node_count):
                if adjacent[idx]==1:
                    adj_nodes.append(idx)
            
            #print adj_nodes
            #get color of adjacent vertices
            colors_adj=[]
            for node_adj in adj_nodes:
                if colors[node_adj]>0:
                    colors_adj.append(colors[node_adj])
                #adj_color = 
            #print colors_adj
            #get min and max colors assigned to adjacent vertices
            if len(colors_adj)>0:
                max_color_adj=max(colors_adj)
                min_color_adj=0
                for color_adj in colors_adj:
                    if color_adj>0:
                        if color_adj<min_color_adj:
                            min_color_adj=color_adj
            else:
                min_color_adj=0
                max_color_adj=0
            
            #print 'min_color_adj:', min_color_adj, 'max_color_adj:', max_color_adj
            #get lowest numbered color that has not been used on any previously colored vertices
            if min_color_adj==0:
                new_color=max_color_adj+1
            elif min_color_adj>0:
                new_color=min_color_adj-1
            #print 'new_color:', new_color
            
            #assign lowest numbered color not in use
            colors[node]=new_color
    
    return colors

import os
def greedy_algo_degrees(node_count,adj_mat, idx_sorted_degree):
    #0. Sort vertices in order of decreasing degree
    #1. Color first vertex with first color.
    #2. Do following for remaining V-1 vertices.
    #     a) Consider the currently picked vertex and color it with the 
    #        lowest numbered color that has not been used on any previously
    #        colored vertices adjacent to it. If all previously used colors 
    #        appear on vertices adjacent to v, assign a new color to it.
    colors = [-1]*node_count
    color_space=[]
    #color_space_copy=[]
    #print sorted(range(len(degree_list)),key=lambda x:degree_list[x])
    
    #for node in range(node_count):
    for ndx in range(node_count):
        node = idx_sorted_degree[ndx]
        if ndx==0:
            colors[node]=0
            color_space.append(0)
            #color_space_copy.append(0)
        else:
            adjacent=adj_mat[node]
            adj_nodes=[]
            for idx in range(0,node_count):
                if adjacent[idx]==1:
                    adj_nodes.append(idx)
            
            print "node:",node, " adj_nodes:",adj_nodes
            #get color of adjacent vertices
            colors_adj=[]
            for node_adj in adj_nodes:
                if colors[node_adj]>=0:
                    colors_adj.append(colors[node_adj])
                #adj_color = 
            print 'colors_adj:',colors_adj, ' color_space:', color_space
            #get min and max colors assigned to adjacent vertices
#            if len(colors_adj)>0:
#                max_color_adj=max(colors_adj)
#                min_color_adj=min(colors_adj)
#                #min_color_adj=0#colors_adj[0]
#                #for color_adj in colors_adj:
#                #    if color_adj>0:
#                #        if color_adj<min_color_adj:
#                #            min_color_adj=color_adj
#            else:
#                min_color_adj=0#None
#                max_color_adj=0#None
#            
#            print 'min_color_adj:', min_color_adj, 'max_color_adj:', max_color_adj
#            #get lowest numbered color that has not been used on any previously colored vertices
#            #if len(colors_adj)>0:
#            if min_color_adj==0:
#                new_color=max_color_adj+1
#            elif min_color_adj>0:
#                new_color=min_color_adj-1
#            #else:
#            #    new_color=0
#            #if len(colors_adj)==0:
#            #    new_color=0
#            
            #get min and max colors assigned to adjacent vertices
            color_space_copy=[]
            for cdx in color_space:
                color_space_copy.append(cdx)
            
            for color in colors_adj:
                if color in color_space_copy:
                    color_space_copy.remove(color)
            print 'color_space_copy:',color_space_copy, ' color_space:', color_space
            
            if len(color_space_copy)==0:
                new_color=max(color_space)+1
            else:
                new_color=min(color_space_copy)
            print 'new_color:', new_color
            
            #assign lowest numbered color not in use
            colors[node]=new_color
            if new_color not in color_space:
                color_space.append(new_color)
                #color_space_copy.append(new_color)
            #os.system("pause")
    
    return colors
    
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
    
    degree_list = find_degree(node_count, edge_count, edges)
    print_degree_list(degree_list)
    idx_sorted_degree=sorted(range(len(degree_list)),key=lambda x:degree_list[x],reverse=True)
    
    #build adjacency matrix
    adj_mat = np.zeros((node_count,node_count),dtype=int)
    adj_mat = build_adjacency_matrix(node_count, edge_count, edges)
    print_adj_mat(adj_mat)
    
    # build a trivial solution
    # every node has its own color
    solution = range(0, node_count)
    #print solution
    
    #solution = greedy_algo_1(node_count,adj_mat)
    #print solution
    
    solution = greedy_algo_degrees(node_count,adj_mat,idx_sorted_degree)
    print solution
    
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

