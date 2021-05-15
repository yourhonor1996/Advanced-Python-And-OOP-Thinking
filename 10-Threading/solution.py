# import threading, functions
import threading
# from functions import functions 
import functions
from threading import Thread
def solve():
    f1 = Thread(name= 1, target=functions.f[0])
    f2 = Thread(name= 2, target=functions.f[1])
    f3 = Thread(name= 3, target=functions.f[2])
    f4 = Thread(name= 4, target=functions.f[3])

    f1.start()
    f2.start()
    f3.start()
    f4.start()
    f1.join()
    f2.join()
    f3.join()
    f4.join()

    g1 = Thread(name= 1, target=functions.g[0])
    g2 = Thread(name= 2, target=functions.g[1])

    g1.start()
    g2.start()
    g1.join()
    g2.join()

    h1 = Thread(name= 1, target=functions.h[0])

    h1.start()
    h1.join()