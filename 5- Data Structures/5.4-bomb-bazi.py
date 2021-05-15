n, m = [int(item) for item in input().split()]
k = int(input())
map = [[0 for j in range(m)] for i in range(n)]
for i in range(k):
    i1, i2 = [int(item) for item in input().split()]
    i1 -= 1
    i2 -= 1
    map[i1][i2] = '*'
    for n1 in range(i1-1, i1+2, 1):
        for n2 in range(i2-1, i2+2, 1):
            if((n1>=0 and n1<n) and (n2>=0 and n2<m)):
                if map[n1][n2] != '*':
                    map[n1][n2] += 1

for i in range(n):
    print(' '.join([str(item) for item in map[i]]))



    
