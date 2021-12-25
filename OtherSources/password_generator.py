from random import randint

# We can use password length and restricted symbols as arguments is this function
def generate_password(length = 12, restricted_symbols = ""):
    # Creating variables for symbols (that'll be used in password) and password strings
    symbols = "abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/.';\"[]}{|\\?,!#$%^&*@)(-+="
    password = ""

    # Looping through restricted_symbols to delete such from a symbols string
    for el in restricted_symbols:
        try:
            symbols = symbols[:symbols.find(el)] + symbols[symbols.find(el)+1:]
        except IndexError:
            # That means duplicates in restricted symbols variable
            pass
    
    # Looping length of password times to fill the password string
    for i in range(0, length):
        password = password + symbols[randint(0, len(symbols))]

    # Returning password string
    return password

# Some tests:
if __name__ == "__main__":
    print(generate_password())
    print(generate_password(20))
    print(generate_password(0))
    print(generate_password(10, "abcABCefgEFGhigHIG"))
    print(generate_password(10, "AAAAAaaavvv"))
    print(generate_password(10, ",./?|\\';\""))