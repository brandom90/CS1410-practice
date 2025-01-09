



while True:
    try:
        grades = input("What is your grade 0-100: ")
        grade_value = int(grades)
        if 0 <= grade_value <= 100:  
            break
        else:
            print("Please enter a grade between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")
  
        

    

gradeList = [[90, "A"],[80, "B"],[70, "C"],[60, "D"],[50, "F"]]
grade = "Z"
for i in range(len(gradeList)):
    if int(grades) > gradeList[i][0]:
        grade = gradeList[i][1]
        print(grade)
        break
    else:
        continue
if grade == "Z":
    print("F")

