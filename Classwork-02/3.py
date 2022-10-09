n = 5
a = [[i if i>=j else j for i in range(n)] for j in range(n)]
for x in a:
    print(*x)