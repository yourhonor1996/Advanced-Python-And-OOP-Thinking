class ExceptionProxy(Exception):
    def __init__(self):
        self.msg = 'ok!'
        self.function = None


def transform_exceptions(func_ls:list) -> tuple:
    results = []
    for func in func_ls:
        exep = ExceptionProxy()
        exep.function = func
        try: 
            func()
            
        except Exception as e:
            exep.msg = str(e)
        
        finally:
            results.append(exep)
    return results
    

def f():
    1 / 0

def g():
    int("salam")

def h():
    "salam" + 1
            

a = [f, g, h]            
tr_ls = transform_exceptions(a)
for tr in tr_ls:
    print("msg: " + tr.msg + "\nfunction name: " + tr.function.__name__)