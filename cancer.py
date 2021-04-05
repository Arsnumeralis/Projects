from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} seconds to run this program')
        return result
    return wrapper

report = open('C:/Users/pmick/OneDrive/Pulpit/Python/numbers_mason', 'r')
report = report.read().splitlines()
report = [int(x) for x in report]

@performance
def long_time():
    for x in report:
        for y in report:
            for z in report:
                x_index = report.index(x)
                y_index = report.index(y)
                z_index = report.index(z)
                if x_index != y_index and y_index != z_index and z_index != x_index:
                    sum = x + y + z
                    if sum == 2020:
                        prod = x * y * z
                        return prod

long_time()
