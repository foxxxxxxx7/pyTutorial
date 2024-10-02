NUM_DICT = {0: "No", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten"}


def recite(start, take=1):
    result = []
    for i in range(take):
        pluralA = "s"
        pluralC = "s"

        if start == 2:
            pluralC = ""
        if start == 1:
            pluralA = ""

        verseA = f"{NUM_DICT[start]} green bottle{pluralA} hanging on the wall,"
        verseB = "And if one green bottle should accidentally fall,"
        verseC = f"There'll be {NUM_DICT[start - 1].lower()} green bottle{pluralC} hanging on the wall."

        result.extend([verseA, verseA, verseB, verseC])
        if i < take - 1:
            result.append("")
        start -= 1

    return result
