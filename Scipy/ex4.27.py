# Graphs in scipy
# Floyd_marshall method
import numpy as np
import scipy.sparse as sp
myarray=np.array([
    [0,1,0],
    [1,0,2],
    [0,2,0]
])

mynewarr=sp.csr_matrix(myarray)

print("Usage of connected_components method")
# type
print(help(sp.csgraph.connected_components))
print(sp.csgraph.connected_components(mynewarr
))
# to determine the number of connected components in the CSR matrix
print('-'*50)
print("Usage of Dijkstra method")
# to find the shortest path from a given starting node (index 0)
# to all other nodes in a graph represented by the mynewarr array.
# here The return_predecessors parameter is set to True, which means
# that the algorithm will also return the predecessor nodes for each node in the shortest path
print(sp.csgraph.dijkstra(mynewarr, return_predecessors=True, indices=0))
print('-'*50)
# to discover the shortest path between all pair of nodes
# in a graph represented by the mynewarr array.
print("Usage of Floyd_Warshall method")
print(sp.csgraph.floyd_warshall(mynewarr, return_predecessors=True))