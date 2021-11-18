import sys


class Graph:

    def __init__(self, vertices_matrix):
        self.vertices_matrix = vertices_matrix
        self.num_of_vertices = len(vertices_matrix)

    def bfs_search(self, start_vertex, vertex_to_find, parents_list):
        visited_vertices = [False] * self.num_of_vertices
        bfs_queue = [start_vertex]
        visited_vertices[start_vertex] = True
        while bfs_queue:
            current_vertex = bfs_queue.pop(0)
            for vertex_number, vertex_connection_weight in enumerate(self.vertices_matrix[current_vertex]):
                if not visited_vertices[vertex_number] and vertex_connection_weight > 0:
                    bfs_queue.append(vertex_number)
                    visited_vertices[vertex_number] = True
                    parents_list[vertex_number] = current_vertex
        return True if visited_vertices[vertex_to_find] else False

    def find_max_flow(self, input_source, input_sink):
        parents_list = [-1] * self.num_of_vertices
        max_flow = 0

        while self.bfs_search(input_source, input_sink, parents_list):
            edge_flow = sys.maxsize
            current_sink = input_sink
            while current_sink != input_source:
                edge_flow = min(edge_flow, self.vertices_matrix[parents_list[current_sink]][current_sink])
                current_sink = parents_list[current_sink]
            max_flow += edge_flow

            first_reducing_vertex = input_sink
            while first_reducing_vertex != input_source:
                second_reducing_vertex = parents_list[first_reducing_vertex]
                self.vertices_matrix[second_reducing_vertex][first_reducing_vertex] -= edge_flow
                first_reducing_vertex = parents_list[first_reducing_vertex]

        return max_flow


if __name__ == '__main__':
    adjacency_matrix = [[0, 8, 0, 0, 3, 0],
                        [0, 0, 9, 0, 0, 0],
                        [0, 0, 0, 0, 7, 2],
                        [0, 0, 0, 0, 0, 5],
                        [0, 0, 7, 4, 0, 0],
                        [0, 0, 0, 0, 0, 0]]
    source = 1
    sink = 3
    graph = Graph(adjacency_matrix)
    resulting_max_flow = graph.find_max_flow(source, sink)
    print(resulting_max_flow)
