from sys import maxsize
from collections import deque

def find_min(dist, Q):
    min = maxsize
    pos = -1
    for u in Q:
        if dist[u] < min:
            min = dist[u]
            pos = u 
    return pos

def Dijkstra(number_of_city, pair, start, end, matrix):
    dist = [maxsize] * number_of_city
    prev = [None] * number_of_city
    Q = deque(range(number_of_city))
    dist[start] = 0

    while Q:
        u = find_min(dist, Q)
        if u == end:
            break
        try:
            Q.remove(u)
        except ValueError:
            print(-1)
            return
        

        for v in Q:
            if matrix[u][v] != 0:
                temp = dist[u] + matrix[u][v]
                if temp < dist[v]:
                    dist[v] = temp
                    prev[v] = u
        # print(dist)
    # print(prev)
    print(dist[end])

def main():
    number_of_city, pair, start, end = map(int, input().split())
    matrix = [[0] * number_of_city for i in range(number_of_city)]

    for i in range(pair):
        first, second, cost = map(int, input().split())
        matrix[first - 1][second - 1] = matrix[second - 1][first - 1] = cost

    Dijkstra(number_of_city, pair, start - 1, end - 1, matrix)


if __name__ == '__main__':
    main()