
def csv_reader(path):
    with open(path) as csv:
        for row in csv.readlines():
            yield row

def process(path:str):
    with open('ans.csv', 'w') as file:
        write_str = ''
        # while True:
        line_list = [item.strip().replace(' ', '') for item in list(csv_reader(path))]
        new_list = []
        for line in line_list:
            sumv = sum([int(item) for item in line.split(',')])
            if line.find(" ") > 0:
                new_list.append(line.strip() + f', {sumv}\n')
            else:
                new_list.append(line.strip() + f',{sumv}\n')
                
        write_str = ''.join(new_list)
        file.seek(0)
        file.write(write_str)
        file.close()
        return file
            
print(process('abc.txt'))            
# print('1, 5, 7 ,8 ,9 ,78'.strip().replace(' ', ''))