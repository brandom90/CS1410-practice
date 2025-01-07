



while True:
    try:
        grades = input("What is your grade 0-100: ")
        if grades >= 0:
            break
    except:
        print("do a number")
  
        

    

gradeList = [[90, "A"],[80, "B"],[70, "C"],[60, "D"],[50, "F"]]


for i in range(len(gradeList)):
    if int(grades) > gradeList[i][0]:
        print(gradeList[i][1])
        break
    else:
        continue

