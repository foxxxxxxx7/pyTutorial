class Matrix:
    def __init__(self, matrix_string):
        rows = matrix_string.split('\n')
        self.matrix = []
        for row in rows:
            number_strings = row.split()
            numbers = []
            for num_str in number_strings:
                numbers.append(int(num_str))
            self.matrix.append(numbers)

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        column_elements = []
        for row in self.matrix:
            column_value = row[index - 1]
            column_elements.append(column_value)
        return column_elements