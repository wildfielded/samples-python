#!/usr/bin/python3

def count_find_num(primesL_: list, limit_: int) -> list:
    ''' Returns the total number of results obtained from the given factors and
    the largest result within the limit
    Arguments:
        primesL_ [list] -- List of prime factors
        limit_ [int] -- Upper limit
    Returns:
        [list] -- List with total value and the largest result
    '''

''' =====----- MAIN -----===== '''
if __name__ == '__main__':
    primesL_1 = [2, 3]
    limit_1 = 200
    assert count_find_num(primesL_1, limit_1) == [13, 192]

    primesL_2 = [2, 5]
    limit_2 = 200
    assert count_find_num(primesL_2, limit_2) == [8, 200]

    primesL_3 = [2, 3, 5]
    limit_3 = 500
    assert count_find_num(primesL_3, limit_3) == [12, 480]

    primesL_4 = [2, 3, 5]
    limit_4 = 1000
    assert count_find_num(primesL_4, limit_4) == [19, 960]

    primesL_5 = [2, 3, 47]
    limit_5 = 200
    assert count_find_num(primesL_5, limit_5) == []

#####=====----- THE END -----=====#########################################