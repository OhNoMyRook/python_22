N, M = map(int, input().split())
a = []
for i in input().split():
    a.append( int(i) )
a=a[-(N-M):]+a[:-(N-M)]
print (" ".join(map(str, a)))