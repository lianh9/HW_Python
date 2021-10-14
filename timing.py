import time
def calculate_time(func):
    def wrapper():
        start = time.time()
        start = float(start)
        func()
        end = time.time()
        end = float(end)
        result = end - start
        print(f'Total time {result}')
    return wrapper
