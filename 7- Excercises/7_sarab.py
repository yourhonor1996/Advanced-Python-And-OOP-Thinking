import math
n = int(input())
data = []
for i in range(n):
    data.append([int(item) for item in input().split()])
    
for p in data:
    div = p[1]/2
    if p[0] == p[1]:
        print(1*math.ceil(div) + 3*math.floor(div))        
        
    elif p[1] == p[0] - 2:
        print(2 + 1*math.ceil(div) + 3*math.floor(div))        

    else:
        print(-1)