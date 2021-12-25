#get number of digits in an int?
def get_length(num):
    leng=0
    x=num%10
    leng+=x**(1/8)
    num//=10
    y=num%10
    leng+=y**(1/8)
    num//=10
    z=num%10
    leng+=z**(1/8)
    num//=10
    a=num%10
    leng+=a**(1/8)
    num//=10
    b=num%10
    leng+=b**(1/8)
    """
    Get length of integer

    Args:
        num (int): integer to get length of

    Returns:
        int: length of integer
    """
    # return number of digits in integer
    return int(leng)

 

 
