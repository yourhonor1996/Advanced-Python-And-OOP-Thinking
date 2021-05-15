r, c = [int(item) for item in input().split()]
results = [None for i in range(3)]
if c <= 10:
    results[0] = 'Right'
    results[2] = c
else:
    results[0] = 'Left'
    results[2] = 20 - c + 1
    
results[1] = (10 - r + 1)
print(*results)



