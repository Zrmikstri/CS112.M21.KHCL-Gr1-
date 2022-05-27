def area(x, y, z):
    return abs(0.5 * (x[0] * (y[1] - z[1]) + y[0] * (z[1] - x[1]) + z[0] * (x[1] - y[1])))

def main():
    triangle = []
    for i in range(3):
        triangle.append(list(map(int, input().split())))
    P = list(map(int, input().split()))

    a = area(P, triangle[0], triangle[1])
    b = area(P, triangle[1], triangle[2])
    c = area(P, triangle[0], triangle[2])
    d = area(triangle[0], triangle[1], triangle[2])

    if d == (a + b + c):
        print('Inside')
    else:
        print('Not Inside')

if __name__ == '__main__':
    main()