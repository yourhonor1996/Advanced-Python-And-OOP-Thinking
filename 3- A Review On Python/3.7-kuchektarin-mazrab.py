p, d = [int(item) for item in input().split()]
doIt = True
k = 0
while doIt:
    k += d
    if((k % p) <= p/2):
        doIt = False
        print(k)
        
        