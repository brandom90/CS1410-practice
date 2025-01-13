

while True:
    try:
        nights = int(input("Number of nights staying: "))
        
        is_weekend   = input("Is it the weekend?: ").strip().lower()

        if is_weekend  == "yes":
            is_weekend  = True
        elif is_weekend  == "no":
            is_weekend  = False
        else:
            print("Please enter 'yes' or 'no'.")
            continue
        room_type = input('What is your fitness level ("standard", "deluxe", or "suite") ').strip().lower()
        if room_type not in ["standard", "deluxe", "suite"]:
            print("Please choose a valid room type.")
            continue
            
        has_membership    = input("Do you have a membership?: ").strip().lower()

        if has_membership == "yes":
            has_membership = True
        elif has_membership == "no":
            has_membership = False
        else:
            print("Please enter 'yes' or 'no'.")
            continue
        break
    except:
        print("Invalid input/s")
price = 0
if room_type == "standard":
    price = 100
elif room_type == "deluxe":
    price = 150
elif room_type == "suite":
    price = 250
if is_weekend:
    if room_type == "standard" or room_type == "deluxe":
        price += 20
    else:
        price += 50
if has_membership:
    price = price - (price * .1)
if nights > 5:
    price = price - (price * .05)

print(f"Your price is {price} dollars.")
