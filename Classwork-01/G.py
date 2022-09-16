a = input()
a = a.split()
for i in a:
    if len(i)<=3:
        a.remove (i)
print(*a)
