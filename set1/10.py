
password = "PythonRocks"

while True:
    try:
        newPassword = input("Input password: ")
        
        if len(newPassword) > 0:
           break
    except:
        print("Input a valid price")

if newPassword == password:
    print("Access Granted")
else:
    print("Access Denied")