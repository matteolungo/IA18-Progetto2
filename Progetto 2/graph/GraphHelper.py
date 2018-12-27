from graph.Graph_IncidenceList import GraphIncidenceList as Graph


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
    def buildGraph(num_nodes):
        """
        Build a sample complete graph.
        :param num_nodes number of nodes.
        :return: a sample complete graph.
        """
        graph = Graph()

        for i in range(4,7):
            graph.addNode(i)
        for i in range(1,4):
            graph.addNode(i)

        graph.insertEdge(1, 0, 1)
        graph.insertEdge(0, 1, 1)
        graph.insertEdge(1, 3, 2)
        graph.insertEdge(3, 1, 2)
        graph.insertEdge(2, 4, 2)
        graph.insertEdge(4, 2, 2)
        graph.insertEdge(3, 4, 1)
        graph.insertEdge(4, 3, 1)
        graph.insertEdge(4, 5, 1)
        graph.insertEdge(5, 4, 1)
        graph.insertEdge(2, 5, 3)
        graph.insertEdge(5, 2, 3)

        return graph


if __name__ == "__main__":
    graph = GraphHelper.buildGraph(5)

    graph.print()

    edges = GraphHelper.sortEdges(graph)

    print([str(i) for i in edges])

    print("\nGeneric Search:"), graph.genericSearch(0)

    print("\nD-Heap Search:"), graph.dPrioritySearch(0, 4, 5)

    print("\nBinary Heap Search:"), graph.binaryPrioritySearch(0, 4)

    print("\nBinomial Heap Search:"), graph.binomialPrioritySearch(0, 4)