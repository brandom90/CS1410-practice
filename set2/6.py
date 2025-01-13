

while True:
    try:
        distance  = float(input("Distance to travel (in miles) "))
        if distance < 0:
            print("distance must be above 0")
            continue
        
        is_sunny = input('Is it sunny?').strip().lower()

        if is_sunny.lower() == "yes":
            is_sunny = True
        elif is_sunny.lower() == "no":
            is_sunny = False
        else:
            print("Please enter 'yes' or 'no'.")
            continue

        owns_bike = input("Owns a bike?: ").strip().lower()

        if owns_bike.lower() == "yes":
            owns_bike= True
        elif owns_bike.lower() == "no":
            owns_bike  = False
        else:
            print("Please enter 'yes' or 'no'.")
            continue

        is_rush_hour  = input("Rush hour?: ").strip().lower()

        if is_rush_hour.lower() == "yes":
            is_rush_hour = True
        elif is_rush_hour.lower() == "no":
            is_rush_hour = False
        else:
            print("Please enter 'yes' or 'no'.")
            continue
        break
    except:
        print("Invalid input/s")

if distance < 5:
    if is_sunny:
        print("Recommendation: walking")
    else:
         print("Recommendation: driving")
elif distance >=5 and distance <= 20:
    if owns_bike:
        print("Recommendation: cycling")
    else:
         print("Recommendation: bus")
elif distance > 20:
    if not is_rush_hour:
        print("Recommendation: If you own a car, drive.")
    elif is_rush_hour:
        print("Recommendation: train")