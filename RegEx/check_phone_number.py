import re

"""Ukrainian phone numbers starts with 380 and contain 9 other digits. The task is to create a function
which will tell you if the number is valid. Also I thought that stored boolean data and phone
numbers should be represented as {} - dictionary, so it will be less checker function calls"""

# Old function without using re
def check_phone_number_old(n:list):
    res = {}

    # Looping throughout each phone number in n list
    for el in n:
        
        # Extracting '+' and '-' symbols from the string first position, if it is there
        if el[0] == "+" or el[0] == "-":
            el = el[1:]
        
        # Using isnumeric() method to check if number consists of digits only
        if len(el) == 12 and el[0:3] == "380" and el.isnumeric() == True:
            res[el] = True
        else:
            res[el] = False
    
    # Returning res as a dictionary, containing 'key: value' pairs in 'phone_number: True' form
    return res

# New function with implementing findall() function
def check_phone_number(n:list):
    res = {}
    for el in n:
        if el[0] == "+" or el[0] == "-":
            el = el[1:]
        
        # re.match here is for the same purpose as isnumeric() function in old function
        if re.match(r"380[0-9]{9}", el):
            res[el] = True
        else:
            res[el] = False
    return res

# Some tests:
if __name__ == "__main__":
    print("test 1: ")
    print(check_phone_number_old(["+380717083891", "38000000", "22219993152"]), \
        check_phone_number(["380717283891", "38000000", "22219993152"]), sep = "\n") # True False False
    
    print("test 2: ")
    print(check_phone_number_old(["380090990s", "00000000000", "380380380383"]), \
        check_phone_number(["380090990s", "00000000000", "-380380380383"]), sep = "\n") # False, False, True