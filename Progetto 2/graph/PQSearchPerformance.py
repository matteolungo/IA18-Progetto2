from graph.GraphHelper import GraphHelper
from timeit import default_timer
import sys, os


def blockPrint():
    sys.stdout = open(os.devnull, 'w')


def enablePrint():
    sys.stdout = sys.__stdout__

def PQSearchPerformance(n, e):
    print("Binary Heap:")
    start = default_timer()
    graph = GraphHelper.buildGraph(n, e)
    blockPrint()
    graph.dHeapPrioritySearch(0, 2)
    enablePrint()
    elapsed = default_timer() - start
    print(f"Tempo totale: {elapsed} s")

    print("5-Heap:")
    start = default_timer()
    graph = GraphHelper.buildGraph(n, e)
    blockPrint()
    graph.dHeapPrioritySearch(0, 5)
    enablePrint()
    elapsed = default_timer() - start
    print(f"Tempo totale: {elapsed} s")

    print("Binomial Heap:")
    start = default_timer()
    graph = GraphHelper.buildGraph(n, e)
    blockPrint()
    graph.binomialHeapPrioritySearch(0)
    enablePrint()
    elapsed = default_timer() - start
    print(f"Tempo totale: {elapsed} s")


if __name__ == "__main__":
    print("-- 10 elementi, 10 archi --\n"), PQSearchPerformance(10, 10)
    print("\n-- 100 elementi, 100 archi --\n"), PQSearchPerformance(100, 100)
    print("\n-- 1000 elementi, 1000 archi --\n"), PQSearchPerformance(1000, 1000)
    print("\n-- 10000 elementi, 10000 archi --\n"), PQSearchPerformance(10000, 10000)

    print("\n-- 100 elementi, 200 archi --\n"), PQSearchPerformance(100, 200)
    print("-- 100 elementi, 300 archi --\n"), PQSearchPerformance(100, 300)
    print("\n-- 100 elementi, 400 archi --\n"), PQSearchPerformance(100, 400)
    print("\n-- 100 elementi, 500 archi --\n"), PQSearchPerformance(100, 500)