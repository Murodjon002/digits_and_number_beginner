#get number of digits in an int?
def get_length(num):
    a=num//1
    b=num//10
    c=num//100
    d=num//1000
    e=num//10000
    """
    Get length of integer

    Args:
        num (int): integer to get length of

    Returns:
        int: length of integer
    """
    # return number of digits in integer
    return a+b+c+d+e

 
