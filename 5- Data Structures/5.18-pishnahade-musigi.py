

def divs(a:int):
    for i in range(1, a+1):
        if a % i == 0:
            yield i


print(list(divs(20)))            