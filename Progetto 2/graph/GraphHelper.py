from graph.Graph_IncidenceList import GraphIncidenceList as Graph
from random import randint, choice


class GraphHelper:
    """
    Utility functions for graph management.
    """

    @staticmethod
    def sortEdges(graph):
        """
        Return the list of edges, sorted by their weight.
        :param graph: the graph.
        :return: the list of edges, sorted by their weight.
        """
        l = graph.getEdges()
        l.sort()
        return l

    @staticmethod
    def buildGraph(num_nodes, num_edges):
        """
        Build a sample complete graph.
        :param num_nodes number of nodes.
        :return: a sample complete graph.
        """
        if num_edges >= num_nodes:
            graph = Graph()

            if num_edges > (num_nodes * (num_nodes - 1)) / 2:
                print("Numero di archi troppo elevato")
                exit()

            nodes = []
            for i in range(num_nodes):
                nodes.append(graph.addNode(randint(1, 100000), randint(1, 100)))

            for i in range(len(nodes) - 1):
                graph.insertEdge(i, randint(i + 1, len(nodes) - 1), randint(1, 10))
            while graph.numEdges() < num_nodes:
                graph.insertEdge(len(nodes) - 1, randint(0, len(nodes) - 2), randint(1, 10))

            while graph.numEdges() < (num_edges):
                i = choice(graph.nodes).id
                j = choice(graph.nodes).id
                if not i == j:
                    graph.insertEdge(i, j, randint(1, 10))

            return graph

        elif num_edges < num_nodes:
            print("Numero di archi inferiore al numero di nodi")
            exit()

if __name__ == "__main__":
    graph = GraphHelper.buildGraph(5, 8)

    graph.print()

    edges = GraphHelper.sortEdges(graph)

    print([str(i) for i in edges])

    print("\nGeneric Search:"), graph.genericSearch(0)

    print("\nBinary Heap Search:"), graph.dHeapPrioritySearch(0, 2)

    print("\n5-Heap Search:"), graph.dHeapPrioritySearch(0, 5)

    print("\nBinomial Heap Search:"), graph.binomialHeapPrioritySearch(0)
