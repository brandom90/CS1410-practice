
while True:
    try:
        num1  = int(input("Give me an age: "))
        
        num2  = int(input("Is it a weekend?: "))
        
        num3  = int(input("Are you a student?: "))
        break
    except:
        print("One input isn't a valid number")

def ascendingOrder():
    if num2 > num1 and num3 > num2:
        return True
def ascendingOrder():
    if num2 < num1 and num3 < num2:
        return True 

if num1 == num2 == num3:
    print("All 3 are equal")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("2 of the 3 numbers are equal to each other")
elif ascendingOrder():
    print("In ascending order")
elif ascendingOrder():
    print("In decending order")
else:
    print("No specific pattern found.")


