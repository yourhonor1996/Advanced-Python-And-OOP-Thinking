import re
def solve(input:str):
    inputs = input.split()
    nums = []
    nums.append(inputs[0]) 
    nums.append(inputs[2]) 
    nums.append(inputs[4]) 
    reals = [0,0,0]
    index = 0
    for i, item in enumerate(nums):
        if '#' in item:
            index = i
            pattern = item.replace('#', '\d+')
            if i == 2:
                reals[2] = int(nums[0]) + int(nums[1])
                reals[0] = nums[0]       
                reals[1] = nums[1]       
            elif i == 1:
                reals[1] = int(nums[2]) - int(nums[0])
                reals[0] = nums[0]       
                reals[2] = nums[2]       
            elif i == 0:
                reals[0] = int(nums[2]) - int(nums[1])
                reals[2] = nums[2]       
                reals[1] = nums[1]       
            break
    match = re.search(pattern,str(reals[index]))
    if (match != None):
        return f'{reals[0]} + {reals[1]} = {reals[2]}'
    else: 
        return '-1'

# print(solve('12 + 13 = #6'))
print(solve('10# + 50 = 10052'))
# print(re.search())
# match = re.search('\d+','so in the late 1190\'s the government decided to complete the 901 mission.')  
# print(match.group())
# a = ''.re

