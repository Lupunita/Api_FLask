class UserExistsError(Exception):
    """User already exists in databse"""
    def __init__(self, arg):
        self.arg = arg

class DatabaseError(Exception):
    """Raised when commit to databse failed"""
    def __init__(self, arg): 
        self.strerror = arg      

