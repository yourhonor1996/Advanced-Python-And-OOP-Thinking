import json

alldata = {}
lines = []

n = int(input())
for i in range(n):
    lines.append(input())
    
for line in lines:
    line = str(line)
    # if it starts with print -> print the variable 
    if line.startswith('print'):
        _, call_str = line.split(' ', 1)
        var_name = call_str[:call_str.find('[')]
        call_index = call_str[call_str.find('[')+1 : call_str.find(']')]
        if call_index[0] == '"':
            call_index = call_index[1:len(call_index)-1]
        else:
            call_index = int(call_index)
        print(alldata[var_name][call_index])
    else:
        # else -> assign the variable
        var_name, var_str = [item.strip() for item in line.split(':=', 1)]
        var_real = json.loads(var_str)
        alldata.update({var_name : var_real})
        print(f'{var_name} = {var_real}')

