def fib(n):
    f = [1, 2]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n - 1]

n = int(input())
print(fib(n))