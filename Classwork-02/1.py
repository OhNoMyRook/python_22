m, n = 5, 6
a = [[ i*5+j for j in range(m)] for i in range(n)]
for x in a:
    print(*x)