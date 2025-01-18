# Inputs
season = input("Enter the season (summer, winter, spring, fall): ").lower()
temperature = int(input("Enter the temperature (F): "))
humidity = int(input("Enter the humidity percentage: ")) if season == "summer" else None
snow = input("Is there snow? (yes/no): ").lower() if season == "winter" else ""

# Nested If/Else
if season == "summer":
    if temperature > 85:
        if humidity < 60:
            print("Suggestion: Go to the beach.")
        else:
            print("Suggestion: Stay indoors with AC.")
    else:
        print("Suggestion: Enjoy an outdoor picnic.")
elif season == "winter":
    if snow == "yes":
        print("Suggestion: Go skiing.")
    else:
        print("Suggestion: Build a snowman.")
else:
    print("Suggestion: Enjoy a walk outside.")

if season != "summer" and season != "winter":
    print("Suggestion: Enjoy a walk outside.")
elif season == "summer" and not temperature > 85:
    print("Suggestion: Enjoy an outdoor picnic.")
elif season == "summer" and temperature > 85 and not humidity < 60:
     print("Suggestion: Stay indoors with AC.")
elif season == "summer" and temperature > 85 and humidity < 60:
    print("Suggestion: Go to the beach.")
elif season == "winter" and snow == "yes":
    print("Suggestion: Go skiing.")
else:
    print("Suggestion: Build a snowman.")
