def tripler(func):
    '''
    tripler decorator.
        Parameters:
            func : some function
    '''
    def wrapper():
        '''
        wrapper function access outer local func.
            Returns:
                return wrapper()
        '''
        func()
        func()
        func()
    return wrapper
