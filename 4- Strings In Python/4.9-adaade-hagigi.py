import re

def real_numbers(numbers:list):
    results = []
    for item in numbers:
        match = re.fullmatch('[+-]?\d+((\.\d+)?([eE][-+]?\d+)?)?', item)
        if match != None:
            results.append('LEGAL')
        else:
            results.append('ILLEGAL')
    return results

print(real_numbers(['1.0', '1.']))
print(real_numbers(['1.0', '1.']))