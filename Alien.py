from Matrix2Dim import Matrix2Dim


def file_to_matrix(file) -> tuple[Matrix2Dim, tuple[int, int], tuple[int, int]]:
    """
    Read a matrix from a file and identify the start and end positions.

    :param file: File path to read the matrix from.
    :return: Matrix2Dim object, start position tuple, end position tuple.
    """
    with open(file, "r") as f:
        lines = f.readlines()

    elements: list[list[float]] = []

    for line in lines:
        sub_elements = []
        for element in line.strip().split():
            if element == 'X':
                end_pos = (len(elements), len(sub_elements))
                sub_elements.append(1)
            elif element == 'Y':
                start_pos = (len(elements), len(sub_elements))
                sub_elements.append(1)
            else:
                if not element.isdigit():
                    raise ValueError("Invalid character found in the matrix. Only integers are allowed.")
                sub_elements.append(float(element))
        elements.append(sub_elements)

    if 'start_pos' not in locals() or 'end_pos' not in locals():
        raise ValueError("Start or end position not found. Make sure the matrix contains a 'X' and a 'Y'.")
    
    return Matrix2Dim((len(elements), len(elements[0])), elements), start_pos, end_pos


def find_path(matrix: Matrix2Dim, start_pos: tuple[int, int], end_pos: tuple[int, int]) -> list[int]:
    """
    Find a path from the start position to the end position in the matrix.

    :param matrix: Matrix2Dim object.
    :param start_pos: Start position tuple.
    :param end_pos: End position tuple.
    :return: List of Values of the positions from start to end.
    """

    visited = set()
    path = [start_pos]
    current_pos = start_pos

    while current_pos != end_pos:
        for neighbour in get_possible_directions(matrix, current_pos):

            # Check if the neighbour is the end position or is valid and not visited
            if neighbour == end_pos or (neighbour_is_valid(matrix, neighbour, current_pos) and neighbour not in visited):
                current_pos = neighbour
                visited.add(current_pos)
                path.append(current_pos)
                break
        else: # No valid neighbours found so backtrack 1 step
            path.pop(-1)
            current_pos = path[-1]

    # Return the values of the positions in the path
    return [matrix.elements[pos[0]][pos[1]] for pos in path]


def neighbour_is_valid(matrix: Matrix2Dim, neighbour: tuple[int, int], current_pos: tuple[int, int]) -> bool:
    """
    Check if a neighbour position is valid based on the common divisor rule.

    :param matrix: Matrix2Dim object.
    :param neighbour: Neighbour position tuple.
    :param current_position: Current position tuple.
    :return: True if the neighbour is valid, False otherwise.
    """

    neighbour_value = matrix.elements[neighbour[0]][neighbour[1]]
    current_value = matrix.elements[current_pos[0]][current_pos[1]]

    if current_value == 1:
        return True
    # Check if the values have a common divisor
    return bool(neighbour_value % i == 0 and current_value % i == 0 for i in range(2, int(min([neighbour_value, current_value])) + 1))


def get_possible_directions(matrix: Matrix2Dim, pos: tuple[int, int]) -> list[tuple[int, int]]: # type: ignore
    """
    Get all possible neighboring positions from a given position in the matrix.

    :param matrix: Matrix2Dim object.
    :param pos: Current position tuple.
    :return: List of neighboring positions as tuples.
    """
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # Left Up, Right, Down
    for row, col in directions:
        new_row, new_col = pos[0] + row, pos[1] + col
        # Check if the new position is within the matrix bounds
        if 0 <= new_row < matrix.dimensions[0] and 0 <= new_col < matrix.dimensions[1]:
            # Yield the new position
            yield new_row, new_col


def main():

    # Transform text file into matrix
    matrix, start_position, end_position = file_to_matrix("alien.txt")

    # Find path from start to end
    path = find_path(matrix, start_position, end_position)

    # Print matrix and the path that it takes from start to end
    print(f"Matrix: \n {matrix.__str__()}")
    print(f"Path from start to end: \n {' --> '.join(map(str, path))}")


if __name__ == "__main__":
    main()