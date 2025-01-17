# Inputs
username = input("Enter your username: ")
is_alnum = username.isalnum()
length = len(username)

# Nested If/Else
if username:
    if is_alnum:
        if length >= 6:
            if length <= 12:
                print("Username is valid.")
            else:
                print("Username is too long.")
        else:
            print("Username is too short.")
    else:
        print("Username must be alphanumeric.")
else:
    print("Username cannot be empty.")
