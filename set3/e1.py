# Inputs
username = input("Enter your username: ")
is_alnum = username.isalnum()
length = len(username)

# Nested If/Else
if not username:
    print("Username cannot be empty.")
if username and not is_alnum:
    print("Username must be alphanumeric.")
if username and is_alnum and not length >= 6:
    print("Username is too short.")
if username and is_alnum and length >= 6 and not length <= 12:
    print("Username is too long.")
if username and is_alnum and length >= 6 and length <= 12:
    print("Username is valid.")

 
       
  