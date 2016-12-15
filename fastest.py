def fastPower(b, n, e):
    '''
    x = 1
    power = b mod n
    n = p1p2
    e = exponent
'''
    x = 1
    m = '{0:08b}'.format(e)
    m = m[::-1]
    power = b % n
    for i in m:
        if i == '1':
            x = (x * power) % n
        power = (power*power) % n
    return x
        
