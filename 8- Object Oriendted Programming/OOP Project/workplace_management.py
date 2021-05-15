# YOUR IMPORTS GOES HERE
from .workplace import *
# from work_place import *

# TODO how to import all classes from another file

import math

class Mine(WorkPlace):
    def __init__(self, name):
        super().__init__(name)
        self.expertise = 'mine'
        

    def calc_capacity(self):
        self.capacity = int(self.level ** 2)

    def calc_costs(self):
        return Consts.BASE_PLACE_COST + Consts.LEVEL_MUL*self.level 
   
    
class School(WorkPlace):
    def __init__(self, name):
        super().__init__(name)
        self.expertise = 'school'

    def calc_capacity(self):
        self.capacity = math.floor(math.sqrt(self.level))

    def calc_costs(self):
        return Consts.BASE_PLACE_COST * math.floor(math.sqrt(self.level))


class Company(WorkPlace):
    def __init__(self, name):
        super().__init__(name)
        self.expertise = 'company'

    def calc_capacity(self):
        self.capacity = int(self.level)

    def calc_costs(self):
        return Consts.BASE_PLACE_COST * self.level
