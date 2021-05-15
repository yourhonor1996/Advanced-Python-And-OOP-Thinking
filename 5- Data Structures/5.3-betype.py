word = input()
results = []
for letter in word:
    if letter == '=' and len(results) != 0:
        results.pop(len(results)-1)
    elif letter == '=' and len(results) == 0:
        continue
    else:
        results.append(letter)
        
print(''.join(results))