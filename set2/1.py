
while True:
    try:
        age = int(input("Give me an age: "))
        if age > 0:
           age = int(age)
        is_weekend = bool(input("Is it a weekend?: "))
        
        is_student = bool(input("Are you a student?: "))
        if is_student.lower() == "yes":
            is_student = True
        elif is_student.lower() == "no":
            is_student = False
        break
    except:
        print("One input isn't a valid number or boolean")
price = 0
if age < 12:
    price = 8
    print(f'The price for 12 and under is {price}')
elif age >= 12 and age <= 17:
    if is_weekend:
        price = 12
        print(f'The price for 12-17 on a weekend is {price}')
    else:
        price = 10
        print(f'The price for 12-17 on a weekday is {price}')
elif age >= 18 and age <= 64:
    if not is_weekend and is_student:
        price = 12
        print(f'The price for 18-64 on a weekday and student is {price}')
    else:
        price = 15
        print(f'The price is {price}')
elif age >= 65:
    price = 10
    print(f'Price for elders are {price}')