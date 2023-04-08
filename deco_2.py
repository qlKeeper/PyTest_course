def my_decor(func):  # Декоратор
    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper


@my_decor
def my_func():
    print("Тут основная функция")

my_func()