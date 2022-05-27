lst = list(map(int, input().split()))
x, n = map(int, input().split())
best_sum = 0
best_solution = []
solution = []


def find_k_min(lst, k):
    lst.sort()
    return sum(lst[:k])


def branch_and_bound(i, solution):
    global best_sum, best_solution
    if sum(solution) <= x and len(solution) == n:
        if sum(solution) >= best_sum:
            best_sum = sum(solution)
            best_solution = solution[:]
        return 1

    # bound
    if sum(solution) + find_k_min(lst[i:], n - len(solution)) > x:
        return 0

    if sum(solution) > x or i == len(lst):
        return 0

    return branch_and_bound(i + 1, solution) + branch_and_bound(i + 1, solution + [lst[i]])


if temp := branch_and_bound(0, solution):
    print(temp)
    print(best_sum)
    print(best_solution)
else:
    print(0)