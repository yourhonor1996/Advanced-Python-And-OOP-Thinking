a, b, l = [int(item) for item in input().split()]
result = []
for i in range(l):
    time = 0
    if i % 2 == 0:
        time += a
        result.append(time)
    else:
        time += b
        result.append(time)
    
print(sum(result))