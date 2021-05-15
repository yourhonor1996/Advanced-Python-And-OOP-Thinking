data = []
for i in range(5):
    data.append(input())
indexes = []
for i, dat in enumerate(data):
    if dat.find('MOLANA') != -1 or dat.find('HAFEZ') != -1:
        indexes.append(i+1)
if len(indexes) == 0:
    print('NOT FOUND!')       
else:
    print(*indexes)