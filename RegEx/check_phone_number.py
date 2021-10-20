import re

"""Ukrainian phone numbers starts with 380 and contain 8 other digits. The task is to create a function
which will tell (return) you if the number is valid. Also I thought that stored boolean data and phone
numbers should be represented as {} - dictionary."""

# old function without using re
def check_phone_number_old(n:list):
    res = {}
    for el in n:
        if el[0] == "+" or el[0] == "-":
            el = el[1:]
        if len(el) == 12 and el[0:3] == "380" and el.isnumeric() == True:
            res[el] = True
        else:
            res[el] = False
    return res

# new function with implementing findall() function
def check_phone_number(n:list):
    res = {}
    for el in n:
        if el[0] == "+" or el[0] == "-":
            el = el[1:]
        if re.findall(r"380[0-9]{9}", el) and len(el) == 12:
            res[el] = True
        else:
            res[el] = False
    return res
    
if __name__ == "__main__":
    print("test 1: ")
    print(check_phone_number_old(["+380717083891", "38000000", "22219993152"]), \
        check_phone_number(["380717283891", "38000000", "22219993152"]), sep = "\n") # True False False
    print("test 2: ")
    print(check_phone_number_old(["380090990s", "00000000000", "380380380383"]), \
        check_phone_number(["380090990s", "00000000000", "-380380380383"]), sep = "\n") # False, False, True