# algorithm that checks if it's possible to
# create a graph with a given list of degrees

# time complexity: O(n^2 * log n)

def havel_hakimi(degrees):

    # the nodes of the graph will be numbered from 1 to n
    # where n is the number of vertices
    nodes = list(range(1, len(degrees) + 1))

    # finding the sum of the degrees
    sum = 0

    for d in degrees:
        sum = sum + d
        # checking all degrees are smaller than the number of vertices
        if d >= len(degrees):
            exit("Degree cannot be bigger than number of vertices")

    # checking if the sum of degrees is even
    if sum % 2 == 1:
        exit("Degree sum must be even")

    # this will be the list of edges, IF the graph is constructable
    edges = []

    # the program should stop when all the values in the sequence are 0
    # or when any values is a negative number
    while any(d != 0 for d in degrees) and all(d >= 0 for d in degrees):

        # we sort the nodes based on the sorting of the degrees
        nodes = [x for _, x in sorted(zip(degrees, nodes), reverse=True)]
        # then we sort the list in descending order
        degrees.sort(reverse = True)

        # we start the construction of the graph from the node with the highest degree
        # and its neighbours will be the next nodes in descending order of degrees
        n = degrees[0]
        first_node = nodes[0]

        # we delete the first node and then we substract one degree from every neighbour
        # node because we create an edge connected to them
        degrees.pop(0)
        nodes.pop(0)

        for i in range(0, n):
            degrees[i] = degrees[i] - 1
            # we add the edge to the list as a tuple of the extremities
            edges.append((first_node,nodes[i]))


    # the graph is constructable only if all the elements in the sequence are equal to 0
    if all(d == 0 for d in degrees):

        print("The graph is constructable with Havel Hakimi algorithm")
        print(f"The edges of the graph are: {edges}")
    else:
        print("The graph is NOT constructable with Havel Hakimi algorithm")

#
# main entry
#

degrees = [int(x) for x in input("Degree sequence: ").split()]

# calling the function to create a graph using Havel Hakimi
# algorithm and passing a list of the degrees

havel_hakimi(degrees)

# the function will return a list of the edges if the graph is constructable
# otherwise it will print an error message
