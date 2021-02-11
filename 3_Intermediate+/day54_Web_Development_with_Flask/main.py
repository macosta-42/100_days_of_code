import time


def speed_calc_decorator(function):
    def wrapper():
        start = time.time()
        function()
        stop = time.time()
        print(f"{function.__name__} run speed: {stop - start}s")
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
