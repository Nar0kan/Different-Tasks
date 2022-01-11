def multiply_digits(number: int) -> int:
    """
        Return multiplied digit eqivalent for digits in argument number.
    """
    result = 1
    for el in [int(digit) for digit in str(number) if digit != '0']:
        result = result * el
    return result

if __name__ == '__main__':
    print('Example: ')
    print(multiply_digits(123405))  #120
    print(multiply_digits(999)) #729
    print(multiply_digits(1000))    #1
    print(multiply_digits(1111))    #1