def invert_array(arr, N):
    a=[]
    for i in range (N):
        a.append(arr[i])
    a.reverse()
    return a


print(invert_array([1, 2, 3, 4, 5], 4))
print("Hello")
