DIGIT_DICT = {(" _ ", "| |", "|_|", "   "): '0', ("   ", "  |", "  |", "   "): '1', (" _ ", " _|", "|_ ", "   "): '2',
    (" _ ", " _|", " _|", "   "): '3', ("   ", "|_|", "  |", "   "): '4', (" _ ", "|_ ", " _|", "   "): '5',
    (" _ ", "|_ ", "|_|", "   "): '6', (" _ ", "  |", "  |", "   "): '7', (" _ ", "|_|", "|_|", "   "): '8',
    (" _ ", "|_|", " _|", "   "): '9', }


def convert(input_grid):
    check_errors(input_grid)
    result_lines = []

    for grid_start in range(0, len(input_grid), 4):

        grid_slice = input_grid[grid_start:grid_start + 4]
        result = ''
        total_digits = len(grid_slice[0]) // 3

        for i in range(total_digits):
            digit_grid_list = []
            for section in grid_slice:
                digit_slice = section[i * 3:(i + 1) * 3]
                digit_grid_list.append(digit_slice)

            digit_grid = tuple(digit_grid_list)

            if digit_grid in DIGIT_DICT:
                result += DIGIT_DICT[digit_grid]
            else:
                result += '?'

        result_lines.append(result)

    return ','.join(result_lines)


def check_errors(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError('Number of input lines is not a multiple of four')
    for section in input_grid:
        if len(section) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")
