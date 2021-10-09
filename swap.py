def swap_last_item(items=[]):
    '''
    Returns the swaped list of the origina list.
        Parameters:
            items(list) : A list
        Returns:
            a list with the first and last element swaped
    '''
    t = items[-1]
    items[-1] = items[0]
    items[0] = t
    return items
