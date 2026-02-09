import math


def highest_and_lowest(int_list: list) -> list:
    # Initial values to be overwritten once scanning list
    lowest = math.inf
    highest = -math.inf
    for i in int_list:
        if i < lowest:
            lowest = i
        if i > highest:
            highest = i
    return [lowest, highest]


# Testing
examples = [
    [2, 4, 1, 0, 2, -1],
    [20, 50, 12, 6, 14, 8],
    [100, -100]
]

for example in examples:
    print(highest_and_lowest(example))
