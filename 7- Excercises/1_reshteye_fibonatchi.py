from copy import deepcopy as dc
n = int(input())
resutls = []

def fibo(num:int):
    f1 = 1
    f2 = 2
    curr = 3
    result = [1, 2]
    
    if num == 1:
        return [1]
    elif num == 2:
        return [1, 2]
    else:
        while True:
            curr = f1 + f2
            if curr > num:
                break
            result.append(curr)
            f1 = dc(f2)
            f2 = dc(curr)
        return result

i = 1
fibo_list = fibo(n)
resultstr = ''
for i in range(1,n+1):
    if i in fibo_list:
        resultstr += '+'
    else:
        resultstr += '-'
    
# print(fibo_list)
print(resultstr)