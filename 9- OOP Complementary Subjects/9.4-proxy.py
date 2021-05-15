class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self._last_method = ''
        self.calls = {}
    def last_invoked_method(self):
        if self._last_method == '':
            raise Exception('No Method Is Invoked')
        else: 
            return self._last_method

    def count_of_calls(self, method_name):
        if method_name in self.calls:
            return self.calls[method_name]
        else:
            return 0

    def was_called(self, method_name):
        if method_name in self.calls:
            return True
        else: 
            return False
        
    def __getattr__(self, name: str):
        if name in self.calls:
            self.calls[name] += 1
        else:
            self.calls.update({name : 1})

        if name in dir(self._obj):
            self._last_method = name
            return getattr(self._obj)
        else:
            raise Exception('No Such Method')
            

class Radio():   
    def __init__(self):        
        self._channel = None        
        self.is_on = False        
        self.volume = 0        

    def get_channel(self):        
        return self._channel    

    def set_channel(self, value):        
        self._channel = value        

    def power(self):        
        self.is_on = not self.is_on
        
r = Radio()
pro = Proxy(r)

print(pro.wrhn())



