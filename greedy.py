import modularity as mdl
import numpy as np
import networkx as nx
import sys
import copy
import matplotlib.pyplot as plt

g=nx.read_gml(sys.argv[1])
communities= []
nodes=list(range(0,len(g)))
x=[]
y=[]
#creating initial list of communities
communities=list(map(lambda x: {x},nodes))

max_mdl=-1000

i=0
#greedy algorithm
for node in nodes:
    temp_c=copy.deepcopy(communities)
    
    #taking the node out of the community
    for c in temp_c:
        if node in c:
            temp_c.remove(c)
            c.remove(node)
            if len(c)!=0:
                temp_c.append(c)
    
    #pickng the best choice of partition 
    for s in temp_c:
        x.append(i)
        i += 1
        st=s.copy()
        temp_c2=copy.deepcopy(temp_c)
        temp_c2.remove(st)
        st.add(node)
        temp_c2.append(st)
        modularity=mdl.modularity(g,temp_c2)
        y.append(modularity)
        if modularity > max_mdl:
            communities=copy.deepcopy(temp_c2)
            max_mdl=modularity

plt.plot(x,y)
plt.show() 

#printing results           
j=0
names=list(g.nodes)
for community in communities:
    for node in community:
        g.nodes[names[node]]['modularity']=j
        print(str(names[node])+ ' node ' + str(node) + '   ---- Modularity  class= ' + str(j))
    j +=1     
print('Modularity= ' + str(modularity))            
print('communities: ' + str(communities))
nx.write_gml(g,"communities.gml")



