
while True:
    try:
        grades = input("Give me an integer: ")
        if int(grades):
            break
    except:
        print("Type a number")

if int(grades) >= 1 and int(grades) <= 10:
    print("Falls within the range 1,10")
elif int(grades) >= 11 and int(grades) <= 20:
    print("Falls within the range 11,20")
else:
    print("Falls within outside of num range")