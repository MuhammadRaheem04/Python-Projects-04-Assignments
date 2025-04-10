
# Powerfull Passwords Using Hashing

# Solution:

from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.

    email: the email we are checking the password for
    stored_logins: a dictionary pointing from an email to its hashed password
    password_to_check: a password we want to test alongside the email to login with
    """
    return stored_logins.get(email) == hash_password(password_to_check)

# There is no need to edit code beyond this point

def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    
    Inputs:
        password: the password we want
    
    Outputs:
        the hashed form of the input password
    """
    return sha256(password.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": hash_password("password"),
        "code_in_placer@cip.org": hash_password("Karel"),
        "student@stanford.edu": hash_password("123!456?789")
    }
    
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    
    if login(email, stored_logins, password):
        print("Login successful")
    else:
        print("Invalid password or Email")

if __name__ == '__main__':
    main()

