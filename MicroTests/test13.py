#!/usr/bin/python3

def zeros(n: int) -> int:
    ''' Calculates the number of trailing zeros in n! ("n-factorial")
    Arguments:
        n [int] -- Natural number
    Returns:
        zeros_num [int] -- Number of trailing zeros in n!
    '''
    zeros_num = 0
    pow_5 = 5
    while pow_5 < n:
        zeros_num += n // pow_5
        pow_5 *= 5
    return zeros_num

''' =====----- MAIN -----===== '''
if __name__ == '__main__':
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
    assert zeros(101) == 24
    assert zeros(1001) == 249

#####=====----- THE END -----=====#########################################