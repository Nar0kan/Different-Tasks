"""Libraries import."""
from random import choice, shuffle


class Password:
    """Class to operate with passwords (generate, check how strong it is and etc.)"""
    DEFAULT_ARGS = {'len': 16, 'alp': "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:\"'/?>,.<][}{|\\", \
                    'dig': "0123456789", 'req': ""}
    
    def __init__(self, args: dict = {}) -> None:
        """The function that initializes arguments of the current password object."""
        self.args = args
        
        try:
            self.length = int(self.args['len'])
            self.alphabet = str(self.args['alp']) + str(self.args['dig'])
            self.req_symbols = str(self.args['req'])
        except ValueError:
            exit("Make sure the arguments you put in dictionary are correct.")
        
    
    def __str__(self) -> str:
        return self.password if self.password else self.generate()


    def generate(self) -> str:
        new_password = []

        for i in range(self.length - len(self.req_symbols)):
            new_password.append(choice(self.alphabet))
        
        for j in range(len(self.req_symbols)):
            new_password.append(self.req_symbols[j])
        
        shuffle(new_password)

        self.password = ''.join(new_password)

        try:
            while not self.check_password():
                print("""Some of the arguments are incorrect.
                        Default arguments loaded.""")
                self.__init__(Password.DEFAULT_ARGS)
                self.generate()
        except RecursionError:
            exit("""Please make sure that the password length, req_symbols
                    and other arguments are valid to be used.""")

        return self.password
    

    def check_password(self):
        if len(self.password) >=8 \
            and any([i for i in self.password if i.isdigit()]) \
            and any([i for i in self.password if i.isupper()]) \
            and any([i for i in self.password if i.islower()]) \
            and all([i for i in self.req_symbols if self.req_symbols in self.password]):
                return True
            
        else:
            return False


    def change_length(self, new_length: int):
        self.length = new_length


def main():
    """The main function is called when the script starts."""
    PASSWORD = Password({'len': 10, 'alp': "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:\"'/?>,.<][}{|\\", 'dig': "0123456789",'req': '2022'})
    PASSWORD.generate()
    print(PASSWORD)
    PASSWORD.change_length(20)
    PASSWORD.generate()
    print(PASSWORD)
    PASSWORD.change_length(2)
    PASSWORD.generate()
    print(PASSWORD)


if __name__=='__main__':
    main()