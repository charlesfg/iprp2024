import math


def entropy(p1, p2):
    return p1 * math.log2(p1) + p2 * math.log2(p2)

print(entropy(10, 20))