#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Graph:
    def __init__(self,adjacentList):
        self.adjacentList=adjacentList
    
    def get_neighbours(self, node):
        return self.adjacentList[node]
    
    def UCS(self,start,goal):
        open_lst = set([start])
        closed_lst = set([])
        dis = {}
        dis[start] = 0
        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start

        sum=0
        while len(open_lst) > 0:
            n = None
 
            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or dis[v] < dis[n] :
                    n = v
            if n == None:
                print('Path does not exist!')
                return None
                
            # if the current node is the stop then we start again from start
            if n == goal:
                sum = dis[goal]
                path = []
                
                print("\nMinimum Cost to Reach Goal Node {}: ".format(sum))
                while par[n] != n:  
                    path.append(n)
                    n = par[n]
 
                path.append(start)
                path.reverse()
                return path
                 
            for (m, weight) in self.get_neighbours(n):
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    dis[m] = dis[n] + weight
               
                else:
                    if dis[m] > dis[n] + weight:
                        dis[m] = dis[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return None
    
nodes = [ item for item in input('Enter the nodes : ').split(' ')]
startnode = input("Enter the start Node : ") 
targetnode = input("Enter the target Node : ")
adj={}

for vertex in nodes:
    values = int(input('\nEnter of of edges from {} : '.format(vertex)))
    lst=[]
    for values in range(0,values):
        v = input("Input Node and weight comma seprated : ")
        l = v.split(",")
        l[1]=int(l[1])
        t = tuple(l)
        lst.append(t)
    # print(lst)
    adj[vertex]=lst
    
r=[]
for key, value in adj.items():
     if not value:
            r.append(key)         

for k in r:
    adj.pop(k)

print('\nNode \t Neighbour')
for node, child in adj.items():
  print(node, '\t', child)


graph1 = Graph(adj)
path = graph1.UCS(startnode,targetnode)
print('Path found:')
for i in path:
  if path.indexE(i) == len(path) - 1:
    print(i)
  else:
    print(i, '->', end='')

