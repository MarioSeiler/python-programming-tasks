from Matrix2Dim import Matrix2Dim


def file_to_matrix(file) -> tuple[Matrix2Dim, tuple[int, int], tuple[int, int]]:
    with open(file, "r") as f:
        lines = f.readlines()

    elements: list[list[float]] = []

    for line in lines:
        sub_elements = []
        for x in line.strip().split():
            if x == 'X':
                end_position = (len(elements), len(sub_elements))
                sub_elements.append(1)
            elif x == 'Y':
                start_position = (len(elements), len(sub_elements))
                sub_elements.append(1)
            else:
                sub_elements.append(float(x))
        elements.append(sub_elements)
    print(elements)
    return Matrix2Dim((len(elements), len(elements[0])), elements), start_position, end_position


def find_path(matrix: Matrix2Dim, start_position: tuple[int, int], end_position: tuple[int, int]) -> list[tuple[int, int]]:

    visited_positions = set()
    path_positions = [start_position]

    current_position = start_position
    path = [matrix.elements[current_position[0]][current_position[1]]]

    while current_position != end_position:
        print(path)
        #print(f"Current value: {matrix.elements[current_position[0]][current_position[1]]}")
        for neighbour in get_possible_directions(matrix, current_position):
            if (neighbour_is_valid(matrix, neighbour, current_position) and neighbour not in visited_positions) or neighbour == end_position:
                current_position = neighbour
                visited_positions.add(current_position)
                path_positions.append(current_position)
                path.append(matrix.elements[current_position[0]][current_position[1]])
                break
        else:
            path_positions.pop(-1)
            current_position = path_positions[-1]
            path.pop(-1)


    print("End of path")
    return path


def neighbour_is_valid(matrix: Matrix2Dim, neighbour: tuple[int, int], current_position: tuple[int, int]) -> bool:

    neighbour_value = matrix.elements[neighbour[0]][neighbour[1]]
    current_value = matrix.elements[current_position[0]][current_position[1]]

    if current_value == 1:
        return True
        
    for i in range(2, int(min([neighbour_value, current_value])) + 1):
        if neighbour_value % i == 0 and current_value % i == 0:
            return True
        
    return False


def get_possible_directions(matrix: Matrix2Dim, position: tuple[int, int]) -> list[tuple[int, int]]:
    possible_neighbors = []
    if position[1] > 0:
        possible_neighbors.append((position[0], position[1] - 1))
    if position[1] < matrix.dimensions[1] - 1:
        possible_neighbors.append((position[0], position[1] + 1))
    if position[0] > 0:
        possible_neighbors.append((position[0] - 1, position[1]))
    if position[0] < matrix.dimensions[0] - 1:
        possible_neighbors.append((position[0] + 1, position[1]))
    return possible_neighbors

def main():
    matrix, start_position, end_position = file_to_matrix("alien.txt")

    print(matrix)

    path = find_path(matrix, start_position, end_position)
    print(path)


if __name__ == "__main__":
    main()