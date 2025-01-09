
while True:
    while True:
        try:
            year = input("Give me a year: ")
            if int(year) and len(year) <= 4 and len(year) > 0:
                break
        except:
            print("Type a valid lengthed number")


    if int(year) % 4 == 0:
        if int(year) % 400 == 0:
            print("Inputted year is a leap year")
        elif int(year) % 100 == 0:
            print("Inputted year is not a leap year")
        else:
            print("Leap year")
    elif int(year) % 100 != 0:
        print("Not a Leap Year")
    else:
        print("Not a Leap Year")