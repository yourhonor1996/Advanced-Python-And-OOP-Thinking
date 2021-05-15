import requests as req

def process(url:str):
    response = req.get(url)
    if response.status_code != 200:
        return 'Bad Query'
    data = response.json()
    if len(data) == 0:
        return "I can't recognize it"
    if len(data) == 1:
        return data[0]['category']
    else:
        if data[0]['category'] != data[1]['category']:
            return "I can't recognize it"
        else:
            for i in range(len(data)):
                if data[i]['category'] != data[i-1]['category']:
                    return "I can't recognize it"
            return data[0]['category']