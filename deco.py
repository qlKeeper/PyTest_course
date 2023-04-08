def log(f):
    
    def wrapper(arg):
        print("Выполнялось до инкремента")
        return_value = f(arg)
        print(return_value)
        print("Выполнялось после инкремента")
        return return_value
    
    return wrapper

def func(a):
    a += 1
    return a

func = log(func)
b = func(2)
