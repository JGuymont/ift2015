from graph.graph import Graph

if __name__ == '__main__':
    graph = Graph()
    print(graph)
    u = graph.insert_vertex('A')
    v = graph.insert_vertex('B')
    graph.insert_edge(u, v, 'a')
    print(graph)