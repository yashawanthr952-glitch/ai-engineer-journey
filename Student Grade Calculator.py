#Student Grade Calculator

students = {}

n = int(input("How many students? "))  #Allow multiple students

for _ in range(n):
    #Input student name
    name=input("name of student:")    #Input marks of 3 subjects
    maths= int(input("enter maths marks:"))
    science= int(input("enter science marks:"))
    english= int(input("enter english marks:"))#Calculate average
    marks=[maths,english,science]
    average =sum(marks)/len(marks)   #Assign grade:
    if average >90:
        grade ="A"     # 90+ → A
    elif average>75:
        grade="B"     #75+ → B
    elif average>60:
        grade="C"     #60+ → C
    else:
        grade="D"    #Below → D

    students[name] = {
        "maths": maths,
        "science": science,
        "english": english,
        "average": average,
        "grade": grade
     }

print("\nAll Students Data:")
print(students)

