n = int(input())
lst = list(map(int, input().split()))

f = [0] * n
f[1] = f[0] + abs(lst[1] - lst[0])

for i in range(2, n):
    f[i] = min(f[i - 1] + abs(lst[i] - lst[i - 1]), f[i - 2] + abs(lst[i] - lst[i - 2]))

print(f[n - 1])