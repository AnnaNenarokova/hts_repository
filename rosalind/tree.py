#!/usr/bin/python

def tree(file_path):
    n_points, adj_list = read_from_file(file_path)
    connected_graphs = []
    first = True

    for edge in adj_list:
        in_graphs = False
        if first:
            connected_graphs.append(list(edge))
            first = False
        else:
            for connected_graph in connected_graphs:
                for i in range(2):
                    if edge[i] in connected_graph:
                        in_graphs = True
                        connected_graph.append(edge[i-1])
                        break
            if not in_graphs:
                connected_graphs.append(list(edge))

    free_points = []

    for point in range(1, n_points + 1):
        is_free_point = True
        for graph in connected_graphs:
            if point in graph:
                is_free_point = False
        if is_free_point:
            free_points.append(point)

    result = len(connected_graphs) + len(free_points) - 1
    return result

def read_from_file(file_path):
    with open(file_path, 'r') as f:
        first = True
        adj_list = []
        for s in f:
            if first:
                n_points = int(s)
                first = False
            else:
                edge = (int(s.split(' ')[0]), int(s.split(' ')[1]))
                adj_list.append(edge)
        f.closed
    return n_points, adj_list


file_path = '/home/anna/bioinformatics/ngs/rosalind/data/tree.txt'
print tree(file_path)
