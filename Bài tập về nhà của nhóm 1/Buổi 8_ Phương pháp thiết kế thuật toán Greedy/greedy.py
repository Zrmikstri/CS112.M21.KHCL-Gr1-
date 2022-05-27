from math import prod


def max_prod(lst: list) -> int:
    pos = [i for i in lst if i > 0]
    neg = [i for i in lst if i < 0]

    if len(neg) % 2:
        neg.remove(max(neg))

    if len(pos) > 0 or len(neg) > 0:
        return prod(pos) * prod(neg)

    return 0


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    print(max_prod(lst))