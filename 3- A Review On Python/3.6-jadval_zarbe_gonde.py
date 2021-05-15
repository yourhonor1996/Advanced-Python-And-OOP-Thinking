n = int(input())

for i in range(1, n+1):
    temp = []
    for j in range(1, n+1):
        temp.append(i * j)
    print(' '.join(str(item) for item in temp))