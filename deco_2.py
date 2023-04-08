def my_decor(func):  # Декоратор
    def wrapper(n): 
        print('start')
        return_val = func(n) #  Вызов декарируемой функции 
        print('end')
        return return_val
    return wrapper


@my_decor
def my_func(number):
    return number ** 2

print(my_func(10))