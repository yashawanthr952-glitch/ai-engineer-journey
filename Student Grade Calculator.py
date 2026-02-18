#Student Grade Calculator
class Student:
    def __init__(self,name,maths,english,science):   #defining fucion
        self.name=name
        self.maths=self.vadlide_marks(maths)
        self.english=self.vadlide_marks(english)
        self.science=self.vadlide_marks(science)

    def vadlide_marks(self,marks):
        if not isinstance(marks,(int,float)):
            raise ValueError ("enter a number")
        if marks<0 or marks>100:
            raise ValueError("marks not in range ")
        return marks

    def grade(self):                                  #defining grade function 
        avg = (self.maths + self.english + self.science) / 3
        if avg >90:
            grade ="A"     # 90+ → A
        elif avg>75:
            grade="B"     #75+ → B
        elif avg>60:
            grade="C"     #60+ → C
        else:
            grade="D"    #Below → D
        return grade
    

try:
    s=Student("jhon",95,59,32)             #calll the fucction
    s2=Student("dia",95,95,80)

    print(f'{s.name} has a grade {s.grade()}')                     #calling the fuction
    print(f'{s2.name} has a grade {s2.grade()}')    

except ValueError as e:
    print("Error:", e)