import operator


def answer(question):
    ops = {'plus': operator.add, 'minus': operator.sub, 'multiplied': operator.mul, 'divided': operator.truediv}
    question = question.removeprefix('What is').strip('?').split()
    if not question or (question[-1] in ops and question[-2].isdigit()) or (
            question[0] in ops and question[1].isdigit()):
        raise ValueError("syntax error")

    numbers = []
    operations = []

    for word in question:
        if word.isdigit() or (word.startswith('-') and word[1:].isdigit()):
            numbers.append(int(word))
        elif word in ops:
            operations.append(ops[word])
        elif word == "by":
            continue
        else:
            raise ValueError("unknown operation")
    if len(numbers) != len(operations) + 1:
        raise ValueError("syntax error")
    result = numbers[0]
    for i, operation in enumerate(operations):
        result = operation(result, numbers[i + 1])

    return result
