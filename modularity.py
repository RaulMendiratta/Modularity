#this time I'm using networkx because I don't think it's necessary to build a function to read a gml file for this exercise
import numpy as np
import networkx as nx
import sys
import matplotlib.pyplot as plt
import functools as fc

a_matrix=0
norm=0  
communities=[]
#this is part of the formula, i used the one the professor gave but with weigths wich the explanation is in the slide 50 of the slides about communities    
def value(a,b):
    global a_matrix
    global norm
    global communities
    delta=0
    for c in communities:
        if a in c and b in c:
            delta=1
    degree_a=np.sum(a_matrix[a])
    degree_b=np.sum(a_matrix[b])
    return (a_matrix.item((a,b))-(norm*degree_a*degree_b))*delta

#summing the values using the function value
def modularity(g,c):
    global communities
    global a_matrix
    global norm
    communities=c
    norm=1/(2*g.size(weight='value'))
    a_matrix=nx.to_numpy_matrix(g,weight='value')
    l=list(range(0,len(g)))
    result= sum(value(a,b) for a in l for b in l)
    result *= norm
    return result


if __name__ == "__main__":
    #reading from a gml file
    g=nx.read_gml(sys.argv[1])
    f = open(sys.argv[2],"r")
    

    #reading communities from a file for testing
    for line in f:
        list_of_nodes=[]
        nodes=line.strip().split(' ')
        for node in nodes:
            list_of_nodes.append(int(node))
            communities.append(set(list_of_nodes))

    f.close()  
    result=modularity(g,communities) 
    print(result)




