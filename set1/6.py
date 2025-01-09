while True:
    try:
        age = input("Give me an age: ")
        if int(age) and len(age) > 0:
           break
    except:
        print("Type a valid age")

if int(age) >= 18:
    print("you can vote!")
else:
    print("Too young")

