

while True:
    try:
        temperature  = float(input("Today's temperature(F): "))
        
        is_raining  = input("Is it raining?: ").strip().lower()

        if is_raining  == "yes":
            is_raining  = True
        elif is_raining  == "no":
            is_raining  = False
        else:
            print("Please enter 'yes' or 'no'.")
            continue

        is_windy = input("Is it windy?: ").strip().lower()

        if is_windy == "yes":
            is_windy = True
        elif is_windy == "no":
            is_windy = False
        else:
            print("Please enter 'yes' or 'no'.")
            continue
            

        time_of_day  = input('What is your fitness level ("morning", "afternoon", or "evening") ').strip().lower()
        if time_of_day  not in ["morning", "afternoon", "evening"]:
            print("Please choose a valid time of day.")
            continue
    
        break
    except:
        print("Invalid input/s")

if temperature < 50:
    if is_raining:
        print("We suggest heavy coat and umbrella")
    elif is_windy:
        print("We suggest windbreaker and gloves")
    else:
        print('We suggest jacket and scarf')
elif 50 <= temperature <= 70:
    if time_of_day == "morning":
        print("We suggest light jacket")
    elif time_of_day == "afternoon":
        print("We suggest long-sleeve shirt")
    elif time_of_day == "evening":
        print("We suggest sweater and scarf")
elif temperature > 70:
    if is_raining:
        print("We suggest raincoat and breathable clothes")
    else:
        print("We suggest T-shirt and shorts")