class Reverse:
    def __init__(self, inputl:list):
        self.inputl = inputl
        self.lasti = len(inputl) 
        self.outputl = []
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.lasti == 0:
            raise StopIteration
        # self.outputl.append(self.inputl[self.lasti])
        self.lasti -= 1
        return self.inputl[self.lasti]
    
    
a = [1,2,3,4,5,6,7]
rev = Reverse(a)
print(next(rev))
print(*rev)

for item in Reverse(a):
    print (item)
        
