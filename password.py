password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

if len(password) >= 8:
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print("Password is valid.")
    else:
        print("Password is invalid. It must have at least one uppercase, one lowercase, one digit, and one special character.")
else:
    print("Password must be at least 8 characters long.")
