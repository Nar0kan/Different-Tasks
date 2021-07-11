def dig_mul(number: int) -> int:
    res = 1
    for el in [int(d) for d in str(number) if d != '0']:
        res = res*el
    return res
    
if __name__ == '__main__':
    print('Example:')
    print(dig_mul(123405), '\n',
        dig_mul(123405), '\n',      #120
        dig_mul(999), '\n',         #729
        dig_mul(1000), '\n',        #1
        dig_mul(1111))              #1
