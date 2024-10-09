def saddle_points(matrix):
    if not matrix:
        return []
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise ValueError("irregular matrix")

    columns = {}
    saddle_points = []
    for row in matrix:
        for i, value in enumerate(row):
            if i not in columns:
                columns[i] = []
            columns[i].append(value)

    for i, row in enumerate(matrix):
        row_max = max(row)
        for j, value in enumerate(row):
            col_min = min(columns[j])
            if value == row_max and value == col_min:
                saddle_points.append({"row": i + 1, "column": j + 1})
    return saddle_points