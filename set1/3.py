
while True:
    try:
        grades = input("Give me an integer: ")
        if int(grades):
            break
    except:
        print("Type a number")

if int(grades) > 0:
    print("Positive")
elif int(grades) < 0:
    print("Negative")
elif int(grades) == 0:
    print("Zero")