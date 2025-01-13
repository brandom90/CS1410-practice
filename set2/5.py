

while True:
    try:
        score  = int(input("Students score 0-100: "))
        if score < 0 or score > 100:
            print("Score must be between 0 and 100.")
            continue
        
        participation = input('The student’s participation level ("excellent", "above average", "average", or "poor"')
        if participation not in ["excellent", "above average", "average", "poor"]:
            print("Please choose a valid participation level.")
            continue

        homework_completed = input("Completed all of their hw?: ")
        if homework_completed.lower() == "yes":
            homework_completed = True
        elif homework_completed.lower() == "no":
            homework_completed = False
        else:
            print("Please enter 'yes' or 'no'.")
            continue
        break
    except:
        print("One input isn't a valid number/boolean/str")
    
grade = "F"
if score > 90:
    if participation.lower() == "excellent":
        grade = "A+"
        print(f'Your grade is a/an {grade}')
    else:
        grade = "A"
        print(f'Your grade is a/an {grade}')
elif score >= 80 and score <= 89:
    if participation.lower() == "above average":
        grade = "B+"
        print(f'Your grade is a/an {grade}')
    else:
        grade = "B"
        print(f'Your grade is a/an {grade}')
elif score >= 70 and score <= 79:
    if homework_completed:
        grade = "C+"
        print(f'Your grade is a/an {grade}')
    else:
        grade = "C"
        print(f'Your grade is a/an {grade}')
elif score <= 70:
    if participation.lower() == "poor":
        grade = "F"
        print(f'Your grade is a/an {grade}')
    else:
        grade = "D"
        print(f'Your grade is a/an {grade}')