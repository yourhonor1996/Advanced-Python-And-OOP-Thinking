import re
def check_registration_rules(**kwargs):
    results = []
    for user, passw in kwargs.items():
        cond = [len(passw) >= 6, len(user) >= 4, user not in ['quera', 'codecup'], re.fullmatch('\d+', passw) == None]
        count = 0
        for item in cond:
            if item == False:
                break
            else:
                count += 1
        if count == len(cond):
            results.append(user)
    return results
        
print(check_registration_rules(username='password', sadegh='He3@lsa', quera='kLS45@l$'))