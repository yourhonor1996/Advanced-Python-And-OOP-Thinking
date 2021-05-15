

def decorator(decor_input:function):
    def type_checker(func:function):
        def ret(*args, **kwargs):
            if decor_input(*args, **kwargs) == True:
                return func(*args, **kwargs)
            else:
                return 'error'
        return ret
    return type_checker
        