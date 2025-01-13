

while True:
    try:
        age  = int(input("Your age: "))
        if age < 1:
            print("age must be above 1")
            continue
        
        fitness_level = input('What is your fitness level ("beginner", "intermediate", or "advanced") ').strip().lower()
        if fitness_level not in ["beginner", "intermediate", "advanced"]:
            print("Please choose a valid fitness level.")
            continue

        goal = input('What is your fitness goal ("strength", "cardio", or "weight loss")').strip().lower()
        if goal not in ["strength", "cardio", "weight loss"]:
            print("Please choose a valid goal.")
            continue

        
        has_health_concerns = input("Do you have health concerns?: ").strip().lower()

        if has_health_concerns == "yes":
            has_health_concerns = True
        elif has_health_concerns == "no":
            has_health_concerns = False
        else:
            print("Please enter 'yes' or 'no'.")
            continue
        break
    except:
        print("Invalid input/s")

if age < 18:
    if goal == "strength":
        print('We Recommend to you the "Youth Strength Program" ')
    elif goal == "cardio":
        print('We Recommend to you the "Youth Cardio Program" ')
elif 18 <= age <= 50:
    if fitness_level == "beginner":
        print('We Recommend to you the "Beginner Strength and Cardio" ')
    elif fitness_level == "intermediate" or  fitness_level == "advanced":
        if goal == "weight loss":
            print('We Recommend to you the "HIIT and Strength Plan" ')
        elif goal == "strength":
            print('We Recommend to you the "Advanced Strength Program" ')
elif age > 50:
    if has_health_concerns:
          print('We Recommend to you the "Gentle Mobility Program" ')
    else:
        print('We Recommend to you the "Active Aging Plan" ')