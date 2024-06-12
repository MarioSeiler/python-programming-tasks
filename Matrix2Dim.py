class Matrix2Dim:
    """
    Two-dimensional matrix based on a list of lists of items and a tuple that defines the dimensions
    of the matrix (number of rows and number of columns).
    """

    def __init__(self, dimensions: tuple[int, int], elements=None) -> None:
        """ Constructor
        :param dimensions: tuple (pair) of the size of both the dimensions.
        (first item of dimensions corresponds to the rows, second item to the columns)
        Important: the dimensions must be greater or equal to 1.
        :param elements: content of the matrix (list of lists of elements).
        """
        if dimensions[0] < 1 or dimensions[1] < 1:
            raise ValueError("The dimensions must be greater or equal to 1.")
        if elements is None:
            elements = []
        self.dimensions = dimensions
        self.elements = elements

        # check if every element in the list is a number in one line
        if not all([all([isinstance(element, (int, float)) for element in row]) for row in self.elements]):
            raise ValueError("The elements of the matrix must be numbers.")


    def initialize(self, value: float) -> None:
        """
        Initialize the content of the matrix with given value.
        :param value: value assigned to all the elements of matrix.
        """
        self.elements = []
        xs = [value] * self.dimensions[1]
        for i in range(self.dimensions[0]):
            self.elements.append(xs)

    def __str__(self):
        """
        Defines the way that class instance should be displayed. The __str__ method is called when
        the following functions are invoked on the object and return a string: print() and str().
        Without this function print() displays a class instance as an object and not as a human-readable way.
        :return: the human-readable string of a class instance (object).
        """
        output = "(" + str(self.dimensions[0]) + \
            ", " + str(self.dimensions[1]) + ")" + "\n"
        for line in self.elements:
            for element in line:
                output += "|" + str(element) + "|"
            output += "\n"
        return output

    def transpose(self):
        """
        Performs the matrix transposition based on swapping row and column.
        :return: the transposed matrix.
        """
        if not self.is_coherent():
            raise ValueError("The matrix is not coherent.")
        self.elements = [[
            self.elements[j][i] for j in range(self.dimensions[0])]
            for i in range(self.dimensions[1])]
        self.dimensions = (self.dimensions[1], self.dimensions[0])

    def is_symmetric(self) -> bool:
        """
        Determine if a matrix is symmetric or not.
        :return: true if the matrix is symmetric, false otherwise.
        """
        if self.dimensions[0] != self.dimensions[1]:
            return False
        for i in range(self.dimensions[0]):
            for j in range(i, self.dimensions[1]):
                if self.elements[i][j] != self.elements[j][i]:
                    return False
        return True

    def total(self) -> float:
        """
        :return: the sum of all the elements of the matrix.
        """
        total = 0
        for line in self.elements:
            total += sum(line)
        return total

    def average(self) -> float:
        """
        :return: the average of the elements of the matrix.
        """
        return self.total() / (self.dimensions[0] * self.dimensions[1])
    

    def stddeviation(self) -> float:
        """
        :return: the standard deviation of all the elements of the matrix.
        """
        deviations = []
        for line in self.elements:
            for element in line:
                deviations.append((element - self.average()) ** 2)
        return (sum(deviations) / deviations.__len__()) ** 0.5

    def is_coherent(self):
        """
        Determine if the matrix is coherent.  A matrix is coherent if and only if all the lines (sub-lists) of
        elements have the same number of elements which is the number of lines in the dimension tuple and the
        number of sub-lists of elements is the same as the number of columns in the dimension tuple.
        :return: true if the matrix is coherent, false otherwise.
        """
        
        return self.dimensions[0] == len(self.elements) and self.dimensions[1] == len(self.elements[0])


def main():
    matrix = Matrix2Dim((2, 3), [[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]])
    print(matrix)
    matrix2 = Matrix2Dim((3, 3))
    matrix2.initialize(0.0)
    print(matrix2)


if __name__ == "__main__":
    main()
