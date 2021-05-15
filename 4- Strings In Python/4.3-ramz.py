n = int(input())
password = input()
passes = []
for i in range(n):
    passes.append(input())
    
def steps(nums:str , pa:str):
    i = nums.find(pa)
    if i < 5:
        return i
    else:
        return 9-i

count = 0
for j, item in enumerate(passes):
    count += steps(item, password[j])

print(count)