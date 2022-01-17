class User:
    """Class for users with name and age information."""
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age
    
    def is_adult(self) -> bool:
        """Check if user is adult."""
        return True if self.age >= 18 else False
    
    @staticmethod
    def generate_password(lenght: int) -> str:
        """Static method that generate password with a lenght you choose as an argument."""
        #from ..OtherSources import password_generator
        #return password_generator.generate_password(lenght)
        
        from random import choice
        from string import ascii_lowercase, ascii_uppercase, digits
        return "".join(([str(choice([choice(digits), choice(ascii_lowercase), choice(ascii_uppercase)]))\
            for x in range(0, lenght)]))        
        # This is one-line code and is definetly hard to read.
        # So i will explain it. "".join([]) is for returning string as whole without saving to a variable.
        # With list comprehension we loop through range(0, lenght) and appending choice([]) objects
        # from ascii lower- and uppercase and digits 0-9. choice() method randomly take argument's elements.
    
    def get_name(self):
        return self.name

user_1 = User("Kageyama", 20)

if __name__=="__main__":
    print(f" -Is user_1 adult? \n -{user_1.is_adult()}.")
    print("Generate password: ", user_1.generate_password(20))
    print(f"user_1 name is {user_1.get_name()}.")