results = []
while True:
    inp = input()
    if inp == '0':
        break
    results.append(inp)
    
for i in range(len(results)-1, -1, -1):
    print(results[i])