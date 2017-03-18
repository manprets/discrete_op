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
   
def get_next_node(non_adj_nodes, colored, adj_mat):
    #return node from non_adj_nodes
    #that is not in colored
    #that is not adjacent to colored
    #with max number of degrees
    
    #step1: get degrees of nodes in non_adj_nodes
    degree_list=[]
    for node in non_adj_nodes:
        degree=sum(adj_mat[node])
        degree_list.append(degree)
    
    #get inedex of sorted degree_list
    idx_sorted_degree=sorted(range(len(degree_list)),key=lambda x:degree_list[x],reverse=True)
    
    print 'non_adj_degree_list:',degree_list
    print 'idx_sorted_degree:',idx_sorted_degree
    
    #step2: parse sorted non_adj_nodes
    #step3: node not in colored
    #step4: node not adjacent to colored
    next_node=None
    for idx in idx_sorted_degree:
        node = non_adj_nodes[idx]
        if node in colored:
            pass
        else:
            adjacent=adj_mat[node]
            conn_arr=[]
            for color_node in colored:
                if adjacent[color_node]==0:
                    #if adjacent
                    #next_node=node
                    #print 'next_node:',next_node
                    conn_arr.append(0)
                else:
                    conn_arr.append(1)
            print 'node',node,'conn_arr:',conn_arr
            if sum(conn_arr)==0:
                next_node=node
                

        if next_node:
            break
    if next_node==None:
        #raw_input(['Here:'])
        print 'next_node=None'
        #break
    print 'next_node:',next_node    
    return next_node

def get_next_node_for_new_color(idx_sorted_degree, colors):
    #return node with max degree
    #that has not been colored yet
    
    for node_deg in idx_sorted_degree:
        if colors[node_deg]==-1:
            return node_deg
    #return next_node
    
def greedy_algo_welsh_powell(node_count,adj_mat, idx_sorted_degree):
    #Welsh Powell Algorithm
    #Find the degree of each vertex
    #List the verices in order of descending valence
    #valence i.e. degree(v(i))>=degree(v(i+1))
    #Colour the first vertex in the list
    #Go down the sorted list and color every vertex not connected to the colored vertices above, the same color then cross out all colored vertices in the list
    #Repeat the process on the uncolored vertices with a new color-always working in descending order of degree until all vertices are colored
    #Complexity of above algorithm = O(n)
    #Step 1: All vertices are sorted according to the decreasing value of their degree in a list V.
    #Step 2: Colors are ordered in a list C.
    #Step 3: The first non colored vertex v in V is colored with the first available color in C.
    #available means a color that was not previously used by the algorithm.
    #Step 4: The remaining part of the ordered list V is traversed and the same color is allocated to
    #every vertex for which no adjacent vertex has the same color.
    #Step 5: Steps 3 and 4 are applied iteratively until all the vertices have been colored.
    
    colors = [-1]*node_count
    color_space=[]
    #first node
    ndx=0
    color=0
    first_node=idx_sorted_degree[ndx]
    colors[first_node]=color
    color_space.append(color)
    #for jdx in range(1,node_count):
    first=True
    while (1):
        #node=idx_sorted_degree[jdx]
        if first:
            node=first_node
            first=False
        else:
            node=next_node
        #get set of colored vertices
        colored=[]
        for idx in range(node_count):
            if colors[idx]>-1 and colors[idx]==colors[node]:
                colored.append(idx)
        print "node:",node,"colored:", colored, "color_space:", color_space
        #go down sorted list and find vertices not connected to colored vertices
            
        adjacent=adj_mat[node]
        non_adj_nodes=[]
        adj_nodes=[]
        for iidx in range(0,node_count):
            if iidx<>node:
                if adjacent[iidx]==0 and colors[iidx]==-1:
                    non_adj_nodes.append(iidx)
                    #colors[iidx]=colors[node]
                else:
                    adj_nodes.append(iidx)
        print "node:",node, "non_adj_nodes:",non_adj_nodes
        print "node:",node, "adj_nodes:",adj_nodes
        #pick next node from non_adj_nodes with max number of degrees 
        #print adj_mat[non_adj_nodes]
        next_node = get_next_node(non_adj_nodes, colored, adj_mat)
        print "node:",node,"next_node:",next_node
        
        if next_node <> None:
            colors[next_node]=colors[node]
        else:
            new_color=max(colors)+1
            color_space.append(new_color)
            next_node=get_next_node_for_new_color(idx_sorted_degree, colors)
            print "node:",node,"next_node_new_color:",next_node
            colors[next_node]=new_color
        #node=next_node
        print 'colors:',colors
        if (-1 not in colors):
            break
        
        # is node connected to colored vertices
#        if node in colored:
#            continue
#        else:
#            connected_arr=[]
#            for node_colored in colored:
#                color_adjacent=adj_mat[node_colored]
#                if adj_mat[node_colored][node]==0:
#                    #node is not connected to colored vertex
#                    connected_arr.append(0)
#                else:
#                    #node is connected to colored vertex
#                    connected_arr.append(1)
#            print 'connected_arr:',connected_arr
        
#    #print sorted(range(len(degree_list)),key=lambda x:degree_list[x])
#    print '-1 index:',colors.index(-1)
#    #for node in range(node_count):
#    #for ndx in range(node_count):
#    ndx=0
#    color=0
#    #while(-1 in colors):
#    flag=True
#    while(flag):
#        node = idx_sorted_degree[ndx]
#        if ndx==0:
#            #color=0
#            colors[node]=color
#            color_space.append(color)
#            
#            adjacent=adj_mat[node]
#            non_adj_nodes=[]
#            for idx in range(0,node_count):
#                if adjacent[idx]==0:
#                    non_adj_nodes.append(idx)
#                    colors[idx]=colors[node]
#            print "node:",node, "non_adj_nodes:",non_adj_nodes
#            print "colors:",colors
#            print "color_space:",color_space
#        #else:
#        #find next ndx,node
#        if (-1 in colors):
#            ndx=colors.index(-1)
#        else:
#            flag=False
#        #if ndx==2:
#        #    break
#        
        
        
#        else:
#            adjacent=adj_mat[node]
#            adj_nodes=[]
#            for idx in range(0,node_count):
#                if adjacent[idx]==1:
#                    adj_nodes.append(idx)
#            
#            print "node:",node, " adj_nodes:",adj_nodes
#            #get color of adjacent vertices
#            colors_adj=[]
#            for node_adj in adj_nodes:
#                if colors[node_adj]>=0:
#                    colors_adj.append(colors[node_adj])
#                #adj_color = 
#            print 'colors_adj:',colors_adj, ' color_space:', color_space
#            #get min and max colors assigned to adjacent vertices
#            color_space_copy=[]
#            for cdx in color_space:
#                color_space_copy.append(cdx)
#            
#            for color in colors_adj:
#                if color in color_space_copy:
#                    color_space_copy.remove(color)
#            print 'color_space_copy:',color_space_copy, ' color_space:', color_space
#            
#            if len(color_space_copy)==0:
#                new_color=max(color_space)+1
#            else:
#                new_color=min(color_space_copy)
#            print 'new_color:', new_color
#            
#            #assign lowest numbered color not in use
#            colors[node]=new_color
#            if new_color not in color_space:
#                color_space.append(new_color)
#                #color_space_copy.append(new_color)
#            #os.system("pause")
#    
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
    
    #solution = greedy_algo_degrees(node_count,adj_mat,idx_sorted_degree)
    #print solution
    
    solution = greedy_algo_welsh_powell(node_count,adj_mat, idx_sorted_degree)
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

#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_graph(node_count, edge_count, edges):
    print "node_count: ", node_count
    print "edge_count: ", edge_count, "\n"
    
    for edge in edges:
        print str(edge[0])+str('---->')+str(edge[1])
    print '\n'
    
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
    solution = range(0, node_count)
    
    print solution
    
    #1. Color first vertex with first color.
    #2. Do following for remaining V-1 vertices.
    #     a) Consider the currently picked vertex and color it with the 
    #        lowest numbered color that has not been used on any previously
    #        colored vertices adjacent to it. If all previously used colors 
    #        appear on vertices adjacent to v, assign a new color to it.
    

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

