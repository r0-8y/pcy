from itertools import combinations


# noinspection PyShadowingNames
def read_input():
    N = int(input())  # number of baskets in the file
    s = float(input())  # threshold (value is between 0 and 1)
    b = int(input())  # number of available buckets for the compression function
    baskets = []
    for _ in range(N):
        baskets.append([int(x) for x in input().strip().split(' ')])
    return s, b, baskets


# noinspection PyShadowingNames
def PCY(s, b, baskets):
    threshold = s * len(baskets)
    item_counter = {}

    for basket in baskets:
        for item in basket:
            if item not in item_counter:
                item_counter[item] = 1
            else:
                item_counter[item] += 1

    m = 0
    for item in item_counter:
        if item_counter[item] >= threshold:
            m += 1
    A = int((m * (m - 1)) / 2)

    buckets = {}
    item_counter_length = len(item_counter)

    for basket in baskets:
        for i, j in combinations(basket, 2):
            if item_counter[i] >= threshold and item_counter[j] >= threshold:
                k = ((i * item_counter_length) + j) % b
                if k not in buckets:
                    buckets[k] = 1
                else:
                    buckets[k] += 1

    pairs = {}
    P = 0

    for basket in baskets:
        for i, j in combinations(basket, 2):
            if item_counter[i] >= threshold and item_counter[j] >= threshold:
                k = ((i * item_counter_length) + j) % b
                if buckets[k] >= threshold:
                    if (i, j) not in pairs:
                        P += 1
                        pairs[(i, j)] = 1
                    else:
                        pairs[(i, j)] += 1

    print(A)
    print(P)
    for pair_occurence in sorted(pairs.values(), reverse=True):
        print(pair_occurence)


if __name__ == '__main__':
    s, b, baskets = read_input()
    PCY(s, b, baskets)
