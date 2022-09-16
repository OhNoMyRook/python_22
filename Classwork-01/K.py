N=int(input())
a=[]
for i in range(N):
    a.append(input())
print(*a[N::-1], sep='\n')
