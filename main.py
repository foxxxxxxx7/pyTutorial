def slices(series, length):
    result = []
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if len(series) == 0:
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    for i in range(0, len(series)):
        if i > len(series) - length:
            continue
        result.append(series[i:i + length])
    return result