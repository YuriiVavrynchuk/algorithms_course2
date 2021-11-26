def find_ijones_combinations(starting_coordinates_list: list, ijones_matrix: list):
    coordinates_number = len(starting_coordinates_list)
    for coordinates in starting_coordinates_list:
        parents_coordinates = find_parents_coordinates(coordinates, ijones_matrix)
        if len(parents_coordinates) > 0:
            coordinates_number += find_ijones_combinations(parents_coordinates, ijones_matrix) - 1
    return coordinates_number


def find_parents_coordinates(children_coordinates: tuple, ijones_matrix: list):
    value = ijones_matrix[children_coordinates[0]][children_coordinates[1]]
    parents_coordinates_array = []
    for row in range(len(ijones_matrix)):
        for column in range(children_coordinates[1]):
            if ijones_matrix[row][column] == value:
                parents_coordinates_array.append((row, column))
    if children_coordinates[1] != 0 and ijones_matrix[children_coordinates[0]][children_coordinates[1] - 1] != value:
        parents_coordinates_array.append((children_coordinates[0], children_coordinates[1] - 1))
    return parents_coordinates_array


def main(path_to_ijones_file: str):
    ijones_matrix = open(path_to_ijones_file, 'r').read().split('\n')[1:]
    width = len(ijones_matrix[0])
    height = len(ijones_matrix)
    combination_number = 0
    if len(ijones_matrix) == 1:
        combination_number = find_ijones_combinations([(0, width - 1)], ijones_matrix)
    elif len(ijones_matrix) > 1:
        combination_number = find_ijones_combinations([(0, width - 1), (height - 1, width - 1)], ijones_matrix)
    else:
        print("Bad format of the file!")

    with open("ijones_out.txt", "w") as ijones_out_file:
        ijones_out_file.write(str(combination_number))
    ijones_out_file.close()


if __name__ == '__main__':
    main("ijones_in.txt")
