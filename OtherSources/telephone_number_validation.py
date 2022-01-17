# Look on phone number and validate if it's the right format.
# Format: dddd-dddd-dddd.


# w/o RegEx
def check_phone(number):
    if len(number) != 14:
        return False
    
    for i in range(0, 4):
        if not number[i].isdecimal() or not number[i+5].isdecimal() or not number[i+10].isdecimal():
            return False
    
    return True if number[4] == number[9] and number[9] == "-" else False


# with RegEx
def check_phone_regex(number):
    from re import findall
    return True if findall("\d{4}-\d{4}-\d{4}", number) else False


# Some tests:
def test_check_phone_regex():
    print("Test check phone number with regex: ")
    print(check_phone_regex("9999-2222-1111"))
    print(check_phone_regex("9999-2222-111"))
    print(check_phone_regex("9999-2222-11s1"))
    print(check_phone_regex("9999-222201111"), end="\n"*2)

def test_check_phone():
    print("Test check phone number no libs: ")
    print(check_phone("9999-2222-1111"))
    print(check_phone("9999-2222-111"))
    print(check_phone("9999-2222-11s1"))
    print(check_phone("9999-222201111"), end="\n"*2)

if __name__ == "__main__":
    test_check_phone()
    test_check_phone_regex()