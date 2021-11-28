import math  # Needed for giving nodes infinity weight


def relax(distance, i):
    if distance[i.source] != math.inf:
        distance[i.destination] = min(distance[i.destination], distance[i.source] + i.weight)   # min = shortest path


class Graph:
    class Edge:
        def __init__(self, source, destination, weight):  # an edge contains a source, destination and weight
            self.source = source
            self.destination = destination
            self.weight = weight

    def __init__(self, edges, count):  # A graph has edges and number of nodes in it
        self.edges = edges
        self.count = count

    def print_fastest_path(self, source, distance):
        for node in range(self.count):
            print("Source Node:" + str(source) + "      Destination Node: " + str(node) + "      Path Length: " + str(
                distance[node]))

    def check_negative(self, distance):     # check for any negative weight cycles in the graph
        for j in self.edges:
            if distance[j.source] != math.inf and distance[j.destination] > distance[j.source] + j.weight:
                return True
        return False

    def BellmanFord(self, source):
        distance = []
        for i in range(self.count):     # initialize values to infinite, except source node, which is value 0
            if i == source:
                distance.append(0)
            else:
                distance.append(math.inf)
        for node in range(self.count):
            for i in self.edges:
                relax(distance, i)
        negatives = self.check_negative(distance)
        if negatives:
            print("Negative cycles exist")
        else:
            print("No negative cycles exist")
            print("")
        self.print_fastest_path(source, distance)  # Print results


def main():
    edge1 = Graph.Edge(0, 1, 6)
    edge2 = Graph.Edge(0, 2, 5)
    edge3 = Graph.Edge(0, 3, 5)
    edge4 = Graph.Edge(3, 2, -2)
    edge5 = Graph.Edge(2, 1, -2)
    edge6 = Graph.Edge(1, 4, -1)
    edge7 = Graph.Edge(2, 4, 1)
    edge8 = Graph.Edge(3, 5, -1)
    edge9 = Graph.Edge(4, 6, 3)
    edge10 = Graph.Edge(5, 6, 3)

    nodes_number = 7
    source_node = 0
    edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10]

    my_graph = Graph(edges, nodes_number)
    my_graph.BellmanFord(source_node)


if __name__ == "__main__":
    main()
