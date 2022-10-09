with open("2.txt", "r", encoding="utf-8") as f:
    f = f.readlines()
    for line in f[::-1]:
         print(*line)