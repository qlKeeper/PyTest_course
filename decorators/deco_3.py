import time

def my_decor(func):
    def wrapper():
        start_time = time.time()
        func()
        print(f"{(time.time() - start_time):.2f}")
    return wrapper


@my_decor
def sp():
    my_list = [i ** 2 for i in range(100000) if i % 2 == 0]
    print(my_list)


sp()