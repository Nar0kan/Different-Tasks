# the length should be bigger than 6;
# should contain at least one digit.

def is_acceptable_password_2(password: str) -> bool:
    # your code here
    return True if len(password)>6 and any([x.isdigit() for x in password]) else False


if __name__ == '__main__':
    print("Example 1:")
    print(is_acceptable_password_2('short'))           #== False
    print(is_acceptable_password_2('muchlonger'))      #== False
    print(is_acceptable_password_2('ashort'))          #== False
    print(is_acceptable_password_2('muchlonger5'))     # == True
    print(is_acceptable_password_2('sh5'))             #== False


# the length should be bigger than 6;
# should contain at least one digit, but cannot consist of just digits.
def is_acceptable_password_3(password: str) -> bool:
    # your code here
    return True if len(password)>6 and not(password.isnumeric()) and any([x.isdigit() for x in password]) else False


if __name__ == '__main__':
    print("\nExample 2:")
    print(is_acceptable_password_3('short'))          # == False
    print(is_acceptable_password_3('muchlonger'))     # == False
    print(is_acceptable_password_3('ashort'))         # == False
    print(is_acceptable_password_3('muchlonger5'))    # == True
    print(is_acceptable_password_3('sh5'))            # == False
    print(is_acceptable_password_3('1234567'))        # == False
