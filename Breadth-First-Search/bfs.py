# algorithm for traversing a connected graph
# using the breadth first search method

# time complexity: O(n + m)

def adjacencyList(file, orientation):
    
    f = open(file)

    n = int(f.readline().split()[0])
    list = [[] for _ in range(n)]

    if orientation == "undirected" or orientation == "directed":
        for linie in f:
            i, j = [int(x) for x in linie.split()]

            if j not in list[i -1]:
                list[i - 1].append(j)

            if orientation == "undirected" and i not in list[j - 1]:
                list[j - 1].append(i)
    else:
        exit("Graph orientation is wrong")

    for i in range(n):
        list[i].sort()

    f.close()

    return list

def bfs(list, node):

    # list with the final result
    nodes = []
    visited.append(node)
    queue.append(node)

    # we add a nodes into the queue while traversing them
    # and we pop it out when have visited all of its neighbours
    while queue:

        s = queue.pop(0)
        nodes.append(s)
        # when we add a node to the final list
        # we also take it out of the queue

        # we visit all the neighbours of the current
        # node and we mark them as visited
        for neighbour in list[s - 1]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return nodes

# transforms the input file into an adjacency list of nodes
list = adjacencyList ("bfs.in", "undirected")

f = open("bfs.in", "r")

queue = []
visited = []

# number of vertices and edges
n, m = [int(x) for x in f.readline().split()]

# start node
s = 1

nodes = bfs(list, s)

# nodes after traversing the graph with bfs
for i in nodes:
    print(i, end = ", ")

f.close()