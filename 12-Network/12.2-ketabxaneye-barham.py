import requests as req
import json


def process(book:str):
    math_link = 'http://127.0.0.1:8000/math/' 
    physics_link = 'http://127.0.0.1:8000/physic/'
    chess_link = 'http://127.0.0.1:8000/chess/'
    # math_link = 'https://api.github.com/'
    # physics_link = 'https://api.github.com/'
    # chess_link = 'https://api.github.com/'
    math = req.get(math_link).json()
    physics = req.get(physics_link).json()
    chess = req.get(chess_link).json()
    
    lib = {'math' :[math, math_link], 'physic' : [physics, physics_link], 'chess' : [chess, chess_link]}
    for libname, cat in lib.items():
        if book['category'] == libname:
            names = [item['name'] for item in cat[0]]
            if book['name'] in names:
                return 'bad query'
            else:
                req.post(lib[libname][1], book)