import re
def solve(path:str):
    count = 0
    with open(path, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            if line.strip() == '':
                continue
            if (line.strip()[0] != '#'):
                 count += 1
    return count

print(solve('abc.txt'))