#!/bin/python3

import sys
from collections import defaultdict

def bfs(n, m, edges, s):

    edges_present = [False] * n
    edges_present[s-1] = None
    queue =[];

    for k,v in edges:
        #print(v)
        edges_present[v-1] = True
    #print(edges_present)
        #list_nodes[k].append(v)

    for edges in edges_present:
           # print(edges)
            if edges == False:
               queue.append(-1)
            elif edges == True:
                queue.append(6)
    return queue




    '''for i in range(n):
        if i+1 not in list_nodes :
            list_nodes[i+1] = None'''

    #for i in range(n):

    #print(list_nodes)




if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        edges = []
        for edges_i in range(m):
           edges_t = [int(edges_temp) for edges_temp in input().strip().split(' ')]
           edges.append(edges_t)
        s = int(input().strip())
        result = bfs(n, m, edges, s)
        print (" ".join(map(str, result)))
        print()