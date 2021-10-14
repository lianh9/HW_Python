import time
def calculate_time(func):
    '''
    Calculate_time decorator
        Parameters:
            func: some function
    '''
    def wrapper():
        '''
        Wrapper function access outer local func.
        Calculate the time needed to run func.
            Returns:
                wrapper function
        '''
        start = time.time()
        start = float(start)
        func()
        end = time.time()
        end = float(end)
        result = end - start
        print(f'Total time {result}')
    return wrapper
