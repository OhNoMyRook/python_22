s=input()
big=0
small=1000
for x in s.split():
    if len(x)>big:
        big=len(x)
    else:
        big+=0
    if len(x)<small:
        small=len(x)
    else:
        big+=0
print(small, big)
