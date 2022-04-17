from random import choice, shuffle                                  # Build-in random lib
from pyperclip import copy                                          # External copy to clipboard lib
from tkinter import Tk, Entry, Button, END, E,W,N,S                 # External GUI lib 


def main():
    """Main function for file."""

    def retry() -> None:
        """Function for refreshing password entry (GUI bar with suggested password)."""
        password_entry.delete(0, END)
        password_entry.insert(0, generate_password())

    # Create GUI.
    root = Tk()
    root.title("Password degenerator")

    # Initialize entry for password output.
    password_entry = Entry(root, textvariable=generate_password(), font='arial', bg='#1E2020', fg='white')
    password_entry.grid(row=0, column=1, padx=5, pady=5, sticky=E+W+N+S)
    password_entry.insert(0, generate_password())

    # Initialize retry button to refresh password data.
    message_button = Button(root, text="Try again", command=retry, border=2, bg='#A2C3A8', activebackground='#33DD64')
    message_button.grid(row=0, column=2, padx=5, pady=5, sticky=E+W+N+S)
    
    # Last GUI parameters.
    root.resizable(False, False)
    root.mainloop()


def generate_password() -> str:
    # Initialize some variables for password generator
    old_letters = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper() + "0987654321"
    symbols = "-_=+\\|/.,<>\{\}[]:\"';~`()*&^%$#@!?"
    password = ''

    def add_elements(key: str) -> list:
        """Function that add letters and symbols to password."""
        temp = ""
        
        while True:
            for i in range(2):
                temp += choice(key)
            if temp[0] != temp[1]:
                return temp
            else:
                temp = ""

    letters = [symbol for symbol in old_letters if symbol.isupper()]    # Add uppercase letters
    password += add_elements(letters)

    letters = [symbol for symbol in old_letters if symbol.islower()]    # Add lowercase letters
    password += add_elements(letters)

    letters = [symbol for symbol in old_letters if symbol.isdigit()]    # Add digits
    password += add_elements(letters)

    password = list(password)
    shuffle(password)                                                   # Shuffle passwords' content
    password = ''.join(password)                                        # Convert password to string

    password += add_elements(symbols)                                   # Add symbols

    copy(password)                                                      # Copy password to a clipboard
    return password


if __name__=='__main__':
    main()