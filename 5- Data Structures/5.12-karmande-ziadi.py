n = int(input())
names = []
for i in range(n):
    names.append(input().split()[0])
names_set = set()
count = 0
names_dict = {}
for name in names:
    if name not in names_dict :
        # names_set.add(name)
        names_dict[name] = 1
    else:
        names_dict[name] += 1

print(max(names_dict.values()))