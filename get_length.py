#get number of digits in an int?
def get_length(num):
    x=num%10

    num//=10
    y=num%10

    num//=10
    z=num%10

    num//=10
    a=num%10

    num//=10
    b=num%10
    """
    Get length of integer

    Args:
        num (int): integer to get length of

    Returns:
        int: length of integer
    """
    # return number of digits in integer
    return int(x**(1/8)+y**(1/8)+z**(1/8)+a**(1/8)+b**(1/8))

 

 
