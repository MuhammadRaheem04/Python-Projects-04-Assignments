
# In this program we show an example of using dictionaries to keep track of information in a phonebook.

# Solution: 

def read_phone_numbers():
    
    phonebook = {}                   # Create empty phonebook

    while True:
        name = input("Enter the Contact Name: ")
        if name == "":
            break
        number = input("Enter the Contact Number: ")
        phonebook[name] = number
        print(f"Mr {name}'s number added to phonebook!")

    return phonebook


def print_phonebook(phonebook):
 
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))


def lookup_numbers(phonebook):
   
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(f"here is Mr {name}'s phone number: {phonebook[name]}")

def delete_numbers(phonebook):

    while True:
        name = input("Enter name to delete: ")
        if name == "":
            break

        if name in phonebook:
           del phonebook[name]
           print(f"Mr {name}'s number has been deleted from the phonebook")

        else:
           print(name + " is not in the phonebook")
    


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)
    delete_numbers(phonebook)


if __name__ == '__main__':
    main()