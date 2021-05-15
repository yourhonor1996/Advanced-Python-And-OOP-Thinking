import os 

def explore(ttype:str, address:str):
    results = {}
    alldir = list(os.walk(address))
    for tup in alldir:
        count = 0
        for file in tup[2]:
            if file.lower().endswith(ttype.lower()):
            if os.path.ba
                count += 1
        if count > 0:
            results.update({tup[0]:count})
    return results

print(explore('Py', 'e:\\Pycharm Projects\\Programming_And_ML\\Learning-To-Code-And-ML\\Quera'))            
    
