def find(search_list, value):
    start = 0
    end = len(search_list) - 1
    while start <= end:
        mid_index = (start + end) // 2
        if search_list[mid_index] == value:
            return mid_index
        elif search_list[mid_index] < value:
            start = mid_index + 1
        else:
            end = mid_index - 1
    raise ValueError('value not in array')