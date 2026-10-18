'''Our first Python source file.'''

from operator import floordiv, mod, truediv 

def divide_exact(n, d):
    '''Divide n by d, returning the quotient and remainder.
    
    >>> p, q, r = divide_exact(2013, 10)
    >>> p
    201.3
    >>> q
    201
    >>> r
    3
    '''
    return truediv(n, d), floordiv(n, d), mod(n, d)

def absolute_value(x):
    '''Return the absolute value of x.
    
    >>> absolute_value(-3)
    3
    >>> absolute_value(3)
    3
    '''
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x