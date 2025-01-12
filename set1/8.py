
while True:
    try:
        length = int(input("Give me a length for a triangle : "))
        length2 = int(input("Give me a 2nd length for a triangle : "))
        length3 = int(input("Give me a 3rd length for a triangle : "))
        if length > 0 and length2 > 0 and length3 > 0:
           length = int(length)
           length2 = int(length2)
           length3 = int(length3)
           break
    except:
        print("Input a valid number")

if length + length2 > length3 and length2 + length3 > length and  length + length3 > length2:
    print("Is a valid triangle")
else:
    print("Is not a valid triangle")