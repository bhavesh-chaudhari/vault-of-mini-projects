import random
import string


def change_length():
    want_to_change_length = input(
        "Do you want to change the default password length ? (yes/no) : "
    )
    if want_to_change_length == "yes":
        try:
            new_length = int(input("Enter new password length(number): "))
            change_length.new_length = new_length
            print(f"The default password length was changed to {new_length}\n")
        except:
            print("The password length must be numerical")
            change_length()
    elif want_to_change_length == "no":
        change_length.new_length = 8
    else:
        print("Not a valid response, please try again !")
        change_length()
    return


def has_uppercase_letters():
    print("Do you want uppercase letters in the password ? (yes/no)")
    response = input()
    if response == "yes":
        password = []
        uppercase_letters = string.ascii_uppercase
        # print(uppercase_letters)
        password.extend(uppercase_letters)
        has_uppercase_letters.password = password
        # print(password)
    return


def has_lowercase_letters():
    print("Do you want lowercase letters in the password ? (yes/no)")
    response = input()
    if response == "yes":
        if hasattr(has_uppercase_letters, "password"):
            password = has_uppercase_letters.password
            # print(password)
        else:
            password = []
            # print(password)
        lowercase_letters = string.ascii_lowercase
        password.extend(lowercase_letters)
        has_lowercase_letters.password = password
        # print(password)
    return


def has_punctuations():
    print("Do you want punctuations in the password ? (yes/no)")
    response = input()
    if response == "yes":
        if hasattr(has_lowercase_letters, "password"):
            password = has_lowercase_letters.password
            # print(password)
        elif hasattr(has_uppercase_letters, "password"):
            password = has_uppercase_letters.password
            # print(password)
        else:
            password = []
            # print(password)
        punctuations = string.punctuation
        password.extend(punctuations)
        has_punctuations.password = password
        # print(password)
    return


def has_digits():
    print("Do you want numbers in the password ? (yes/no)")
    response = input()
    if response == "yes":
        if hasattr(has_punctuations, "password"):
            password = has_punctuations.password
        elif hasattr(has_lowercase_letters, "password"):
            password = has_lowercase_letters.password
            # print(password)
        elif hasattr(has_uppercase_letters, "password"):
            password = has_uppercase_letters.password
            # print(password)
        else:
            password = []
        digits = string.digits
        password.extend(digits)    
        has_digits.password = password
    return    


def set_random_password():
    password = []
    password.extend(
        list(string.ascii_uppercase)
        + list(string.ascii_lowercase)
        + list(string.punctuation)
        + list(string.digits)
    )
    password_string = "".join(random.sample(password, 8))
    print(f"\nThis is a random strong password generated for you : {password_string}\n")
    return


def set_custom_password():
    print("\n<= Default password length is 8 =>\n")
    # The order of calling the function is important
    change_length()
    has_uppercase_letters()
    has_lowercase_letters()
    has_punctuations()
    has_digits()
    password_length = change_length.new_length
    if hasattr(has_digits, "password"):
        password = has_digits.password
        try:
            password_string = "".join(random.sample(password, password_length))
        except:
            password_string = "".join(random.choices(password,k = password_length))    
        print(f"Your custom password is as follows: \n{password_string}")
    elif hasattr(has_punctuations, "password"):
        password = has_punctuations.password
        try:
            password_string = "".join(random.sample(password, password_length))
        except:
            password_string = "".join(random.choices(password,k = password_length))    
        print(f"Your custom password is as follows: \n{password_string}")
    elif hasattr(has_lowercase_letters, "password"):
        password = has_lowercase_letters.password
        try:
            password_string = "".join(random.sample(password, password_length))
        except:
            password_string = "".join(random.choices(password,k = password_length))    
        print(f"Your custom password is as follows: \n{password_string}")
    elif hasattr(has_uppercase_letters, "password"):
        password = has_uppercase_letters.password
        try:
            password_string = "".join(random.sample(password, password_length))
        except:
            password_string = "".join(random.choices(password,k = password_length))    
        print(f"Your custom password is as follows: \n{password_string}")
    else:
        print("You haven't customized anything...")
        set_random_password()
    return


def check_password_type():
    print(
        "Type `csp` to set a custom password or type `rsp` for a random strong password generated by us."
    )
    response = input("Enter Response(csp/rsp) : ")
    if response == "csp":
        set_custom_password()
    elif response == "rsp":
        set_random_password()
    else:
        print("Not a valid response ! please try again")
        check_password_type()


if __name__ == "__main__":
    check_password_type()
