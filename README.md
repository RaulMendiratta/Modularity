# Modularity
Calculation of Modularity of partition(community) of a graph

modularity.py calculates modularity for a given set of partitions of a graph

To run the program just run the following command:
$python3 modularity.py [gml file] [file with the partitions]

The file with the partitions has to have the follwoing format: each partition is in each line and the nodes have to be separated by spaces.
For example:

1 2 3 3

4 5 6 7 8

9 10

Where each line is a partition of the original graph.


greedy.py generates communities using a greedy algorithym that uses the modularity calculation.

To run the program just run the following command:
$python3 greedy.py [gml file]

This program will output a new gml file called communities.gml
