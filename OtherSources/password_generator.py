# We can use password length and restricted symbols as arguments is this function
from importlib.resources import read_binary


def generate_password(length = 12, restricted_symbols = "") -> str:
    """Creating variables for symbols (that'll be used in password) and password strings."""
    from random import randint
    
    symbols = "abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/.';[]}{|?,!#$%^&*@)(-+="
    password = ""
    
    # Looping through restricted_symbols to delete such from a symbols string
    for el in set(restricted_symbols):
        try:
            symbols = symbols[:symbols.find(el)] + symbols[symbols.find(el)+1:]
        except IndexError:
            # That means duplicates in restricted symbols variable
            print("Duplicates were found in restricted symbols variable.")
    
    # Looping length of password times to fill the password string
    for i in range(0, length):
        password += symbols[randint(0, len(symbols)-1)]

    # Returning password string
    return password


def hash_password(password: str) -> str:
    """Function for hashing password with SHA256 standart and extra salt."""
    from hashlib import sha256

    salt = b"...wibbly-wobbly, timey-wimey... stuff."
    hashed_password = sha256(password.encode() + salt).hexdigest()

    return hashed_password


# Some tests:
if __name__ == "__main__":
    test_a = generate_password(10, "abcABCefgEFGhigHIG")
    test_b = generate_password(15, "AAAAAaaavvv")
    test_c = generate_password(20, ",./?|")
    print("password: ", test_a, "hash: ", hash_password(test_a),\
        "\npassword: ", test_b, "hash: ", hash_password(test_b),\
        "\npassword: ", test_c, "hash: ", hash_password(test_c), sep="\n")