## Breadth First Search Algorithm

Algorithm for traversing a connected graph using the breadth first search method

1. Select a starting point for the traversing
2. Visit its adjacent unvisited node
3. Mark it as visited and save it in a list of nodes
4. Insert the visited node into the queue
5. If there is no adjacent node, remove the first node from the queue
6. Repeat the above steps until the queue is empty

## Example

Input file > bfs.in
```
8 7
1 2
1 3
1 4
1 5
2 6
2 7
3 8
```
```python
# start node
start = 1

nodes = bfs(adjacencyList, start)

print(nodes)
```
The nodes after traversing the graph in BFS order:
```
1, 2, 3, 4, 5, 6, 7, 8
```

## Visual Representation

![Alt Text]()
<img src="https://miro.medium.com/max/875/1*fYKrGW0IUeoS_8XtCoNaLw.gif" alt="bfs" width="200"/>