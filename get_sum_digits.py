#Find the sum of digits in an integer
def get_sum_digits(num):
    a = num%10
    b = (num//10)%10
    c = (num//100)%10
    d = (num//1000)%10
    e = num//10000

    """
    Get sum of digits in integer
    
    Args:
        num (int): integer to get sum of digits of
    
    Returns:
        int: sum of digits in integer
    """
    # return sum of digits in integer
    return  a+b+c+d+e
