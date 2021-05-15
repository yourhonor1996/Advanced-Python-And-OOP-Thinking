import datetime as dt


def day_calculator(date:str):
    yr, mnth, dy = [int(item) for item in date.split('-')]
    curr = dt.date(yr, mnth, dy)
    start = dt.date(1999, 1, 14)
    diff = (curr - start).days
    if (diff >=0):
        return diff
    else:
        return 'Not yet born'


print(day_calculator('1118-10-13'))
