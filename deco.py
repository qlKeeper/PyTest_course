def log(f):
    pass
    def wrapper(arg):
        pass



def func(a):
    print("Выполнялось до инкремента") # Логи
    a += 1
    print(a)
    print("Выполнялось после инкремента")
    return a

b = func(2)
