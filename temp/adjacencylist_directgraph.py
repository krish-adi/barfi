# https://www.geeksforgeeks.org/print-adjacency-list-for-a-directed-graph/

# Python program for the above approach

# Function to add edges
def addEdge(adj, u, v):
	adj[u].append(v)

# Function to print adjacency list
def adjacencylist(adj, V):
	
	for i in range (0, V):
		print(i, "->", end="")
		
		for x in adj[i]:
			print(x , " ", end="")
	
		print()
	
# Function to initialize the adjacency list
# of the given graph
def initGraph(V, edges, noOfEdges):

	adj = [0]* 3
	
	for i in range(0, len(adj)):
		adj[i] = []

	# Traverse edges array and make edges
	for i in range(0, noOfEdges) :

		# Function call to make an edge
		addEdge(adj, edges[i][0], edges[i][1])
	

	# Function Call to print adjacency list
	adjacencylist(adj, V)

# Driver Code

# Given vertices
V = 3

# Given edges
edges = [[0, 1 ], [1, 2 ], [2, 0 ]]

noOfEdges = 3

# Function Call
initGraph(V, edges, noOfEdges)

# This code is contributed by AR_Gaurav
