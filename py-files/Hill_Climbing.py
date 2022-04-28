#!/usr/bin/env python
# coding: utf-8

# In[3]:


succlist  = {
    'Start' : [('Intro', 12), ('Model',11), ('Agents', 15)],
    'Intro' : [('Role', 20), ('Types',19), ('Application',16)],
    'Model' : [('Model Type', 24), ('Algorithm', 10)] ,
    'Agents' : [('Simplex', 22), ('Goal-based', 24), ('Utility', 26)],
    'Role' : [('History',33), ('Sub-roles',40)] ,
    'Types' : [('History', 42)] ,
    'Application' : [('Autocars', 60)] ,
    'Model Type' : [] ,
    'Algorithm' : [('A*', 9), ('DFID', 56)],
    'Simplex' : [('Result', 65), ('Prediction', 80)] ,
    'Goal-based' :[('Result', 70)] ,
    'Utility' : [('Result',71)] ,
    'Sub-roles' : [('Development', 88)] ,
    'History' : [('Development', 90)] ,
    'A*' : [('Autocars', 6)] ,
    'DFID' : [('Prediction', 99)] ,
    'Result' : [],
    'Development' : [],
    'Autocars' : [('Result', 0)] ,
    'Prediction' : []
}


start = 'Start'
Closed = list()

def MOVEGEN(N):
    new_list = list()
    if N in succlist.keys():
        new_list = succlist[N]
    return new_list

def SORT(L):
    L.sort(key = lambda x: x[1])
    return L

def heu(Node):
    return Node[1]

def APPEND(L1,L2):
    new_list = list(L1) + list(L2)
    return new_list

def Hill_Climbing(start):
    global closed
    N = start
    child = MOVEGEN(N)
    SORT(child)
    N = [start,100]
    print("\nStart: ",N)
    
    print("Sorted Child  List: ", child)
    newnode = child[0]
    closed = [N]

    
    while heu(newnode) <= heu(N):
        print('\n------------------')
        N=newnode
        print('N = ',N)
        closed = APPEND(closed,[N])
        child = MOVEGEN(N[0])
        SORT(child)
        print("Sorted Child List = ", sorted(child))
        print("Closed List: ", closed)
        if len(child) == 0:
            break
        else:
            newnode = child[0]
#         newnode = child[0]
    Closed = closed
    

Hill_Climbing(start) #calling the search algorithm 


# In[ ]:




