import random
import string

def generate_password(length):
    """Generate a random password of given length."""
    charectors = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(charectors) for _ in range(length))
    return password

length = int(input("Enter the length of the password: "))

if __name__ == "__main__":
     
        # Check if the length is less than 6
    while True:
         if length < 6:
             print("Password length should be at least 6 characters.")
             length = int(input("Enter the length of the password: "))
         else:
             break
     # Generate the password
    password = generate_password(length)
    print(f"Generated password: {password}")
    
     
    