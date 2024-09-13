def factors(value):
    result = []
    counter = 2
    while value > 1:
        if value % counter == 0:
            result.append(counter)
            value /= counter
        else:
            counter += 1
    return result