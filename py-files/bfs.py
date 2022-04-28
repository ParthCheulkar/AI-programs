#!/usr/bin/env python
# coding: utf-8

# In[15]:


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


# In[ ]:





# In[14]:


# PRACTICE

visit = set()
line = []

def bfs2(visit, graph, node):
    line.append(node)
    visit.add(node)
    
    while line :
        m = line.pop(0)
        print(m)
        for child in graph[m]:
            if child not in visit:
                line.append(child)
                visit.add(child)

bfs2(visit, graph, 'Start')
        
    


# In[ ]:




