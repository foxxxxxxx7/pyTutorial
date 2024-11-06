def transpose(text):
    if not text:
        return ""

    rows = text.split('\n')

    max_len = 0
    for row in rows:
        if len(row) > max_len:
            max_len = len(row)

    padded_rows = []
    for row in rows:
        padded_rows.append(row.ljust(max_len))

    transposed = []
    for col in range(max_len):
        new_row = ""
        for row in padded_rows:
            new_row += row[col]
        transposed.append(new_row)

    return '\n'.join(transposed).rstrip()
