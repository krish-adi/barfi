# https://www.geeksforgeeks.org/find-dependencies-of-each-vertex-in-a-directed-graph/

# Python3 program to find the
# dependency of each node

# Adding edges
def addEdge(u, v, bidir = True):
	global adjList
	adjList[u].append(v)
	if (bidir):
		adjList[u].append(v)

# Performing DFS on each node
def dfs(src):
	global adjList, V
	
	# Map is used to mark
	# the current node as visited
	visited = [False for i in range(V+1)]
	dependent = []
	count = 0
	s = []

	# Push the current vertex
	# to the stack which
	# stores the result
	s.append(src)
	visited[src] = True

	# Traverse through the vertices
	# until the stack is empty
	while (len(s) > 0):
		n = s[-1]
		del s[-1]

		# Recur for all the vertices
		# adjacent to this vertex
		for i in adjList[n]:

			# If the vertices are
			# not visited
			if (not visited[i]):
				dependent.append(i + 1)
				count += 1

				# Mark the vertex as
				# visited
				visited[i] = True

				# Push the current vertex to
				# the stack which stores
				# the result
				s.append(i)

	# If the vertex has 0 dependency
	if (not count):
		print("Vertex ", src + 1,
			" is not dependent on any vertex.")
		return count

	print("Vertex ",src + 1," dependency ",end="")
	for i in dependent:
		print("-> ", i, end = "")
	print()
	return count

# Function to find the
# dependency of each node
def operations(arr, n, m):

	# Creating a new graph
	global adjList
	for i in range(m):
		addEdge(arr[i][0], arr[i][1], False)
	ans = 10**18
	node = 0

	# Iterating through the graph
	for i in range(n):
		c = dfs(i)

		# Finding the node with
		# minimum number of
		# dependency
		if (c < ans):
			ans = c
			node = i + 1
	print("Node", node, "has minimum dependency of ", ans)

# Driver code
if __name__ == '__main__':
	V = 6
	adjList = [[] for i in range(V+1)]
	n, m = 6, 6


	# Defining the edges of the
	# graph
	arr = [ [ 0, 1 ],
			[ 0, 2 ],
			[ 2, 3 ],
			[ 4, 5 ],
			[ 3, 4 ],
			[ 1, 5 ] ]

	operations(arr, n, m)

	# This code is contributed by mohit kumar 29.
