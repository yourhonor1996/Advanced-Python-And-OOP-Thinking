from copy import deepcopy as dc
n = int(input().strip())
names = []
for i in range(n):
    names.append(input().strip())
    
def char_count(word:str):
    t = ''
    for letter in word:
        if letter not in t:
            t += letter
    return len(t)
    
maxnum = 0
for name in names:
    count = char_count(name)
    if count > maxnum:
        maxnum = dc(count)
print(maxnum)