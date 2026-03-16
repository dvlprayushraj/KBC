a = str((input("Enter a password: ")))

def check_password(password):

    if len(password) <8:
        print("Password must be at least 8 characters long.")
        return False
    
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return False
    
    if not any (char in "!@#$%^&*()-+" for char in password):
        print("Password must contain at least one special character.")
        return False
    
    return "Password is valid."

   

check_password(a)