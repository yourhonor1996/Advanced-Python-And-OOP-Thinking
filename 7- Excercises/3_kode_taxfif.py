n, cod = input().split()
n = int(n)
data = []
for i in range(n):
    data.append(input())
    
def iscod(dat:str, cod:str):
    if set(dat) == set(cod):
        return True
    else: 
        return False
    
    
    
for dat in data:
    if iscod(dat, cod):
        print('Yes')
    else:
        print('No')
