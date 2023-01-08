#!/usr/bin/python3

def int32_to_ip(int32_: int) -> str:
    ''' Converts integer number (< 2**32) to an IP-address string
    Arguments:
        int32_n [int] -- Decimal integer number
    Returns:
        ip_str [str] -- IP-address in dotted-decimal notation
    '''
    ip_str = ''
    for pow_ in range(3, 0, -1):
        ip_str += str(int32_ // (256**pow_)) + '.'
        int32_ %= 256 ** pow_
    return ip_str + str(int32_)

''' =====----- MAIN -----===== '''
if __name__ == '__main__':
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"

#####=====----- THE END -----=====#########################################