class User:
    """Class for user account operations."""
    def __init__(self, login="user", password="password", name="Default", surname="User", age="Unknown"):
        """Initialize user's login, password, name, surname, age, info."""
        self.__login = login
        self.__password = password
        
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__info = ''
    
    # Operations with user in database
    @staticmethod
    def check_user_in_database(login: str, password: str) -> bool:
        """Check if user is currently in database."""
        if login.lower() == "admin" and password.lower() == "admin":
            return True
        else:
            return False

    @staticmethod
    def is_login_available(login: str) -> bool:
        """Check if entered login is available"""
        if login == "admin":
            return False
        
        return True

    def register_in_database(self) -> str('success', 'error'):
        """Register user in database."""
        print("The user is registered in database successfully")

    def delete_from_database(self) -> str('success', 'error'):
        """Delete all user data from database."""
        pass
    

    # Functions for writing additional data in database feature
    def get_user_info(self) -> str:
        """Get user info (additional) from database."""
        return self.__info

    def write_user_info(self) -> str('success', 'error'):
        """Let the user write (additional) info."""
        pass