import sys


class Graph:
    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.vertices_matrix = [[0 for column in range(num_of_vertices)]
                                for row in range(num_of_vertices)]

    def min_distance(self, distances_list, visited_list):
        min_distance = sys.maxsize

        for v in range(self.num_of_vertices):
            if distances_list[v] < min_distance and visited_list[v] is False:
                min_distance = distances_list[v]
                min_index = v
        return min_index

    def dijkstra_search(self, starting_vertex):
        distances_list = [sys.maxsize] * self.num_of_vertices
        distances_list[starting_vertex] = 0
        visited_list = [False] * self.num_of_vertices

        for vertex_number in range(self.num_of_vertices):
            current_vertex = self.min_distance(distances_list, visited_list)
            visited_list[current_vertex] = True
            for i in range(self.num_of_vertices):
                if self.vertices_matrix[current_vertex][i] > 0 \
                        and visited_list[i] is False \
                        and distances_list[i] > distances_list[current_vertex] + self.vertices_matrix[current_vertex][i]:
                    distances_list[i] = distances_list[current_vertex] + self.vertices_matrix[current_vertex][i]
        return distances_list


def main(vertices_matrix, starting_vertex: int):
    graph = Graph(len(vertices_matrix))
    graph.vertices_matrix = vertices_matrix
    distances_list = graph.dijkstra_search(starting_vertex)
    return distances_list


if __name__ == '__main__':
    vertices_matrix = [[0, 6, 0, 1, 0],
                       [6, 0, 5, 2, 2],
                       [0, 5, 0, 0, 5],
                       [1, 2, 0, 0, 1],
                       [0, 2, 5, 1, 0]]
    print(main(vertices_matrix, 0))


