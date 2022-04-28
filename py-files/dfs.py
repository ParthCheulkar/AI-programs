#!/usr/bin/env python
# coding: utf-8

# In[3]:


graph = {
   'Start' : ['Intro', 'Model', 'Agents'],
    'Intro' : ['Role', 'Types', 'Application'],
    'Model' : ['Model Type', 'Algorithm'] ,
    'Agents' : ['Simplex','Goal-based','Utility'] ,
    'Role' : ['History','Sub-roles'] ,
    'Types' : ['History'] ,
    'Application' : ['Autocars'] ,
    'Model Type' : [] ,
    'Algorithm' : ['A*','DFID'],
    'Simplex' : ['Result','Prediction'] ,
    'Goal-based' :['Result'] ,
    'Utility' : ['Result'] ,
    'Sub-roles' : ['Development'] ,
    'History' : ['Development'] ,
    'A*' : ['A*'] ,
    'DFID' : ['Prediction'] ,
    'Result' : ['Prediction'],
    'Development' : [],
    'Autocars' : ['Result'] ,
    'Prediction' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
#         print(visited)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search : ")
dfs(visited, graph, 'Start')


# In[ ]:





# In[ ]:




