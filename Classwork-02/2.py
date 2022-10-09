m, n = 5, 6
a = [[0 if i == j else 1 if i>j else 2 for i in range(m)] for j in range(n)]
for x in a:
    print(*x)