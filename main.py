def generate_step(number):
    if number % 2 == 0:
        yield number / 2
    else:
        yield number * 3 + 1


def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0
    while number != 1:
        step = generate_step(number)
        number = next(step)
        count += 1
    return count