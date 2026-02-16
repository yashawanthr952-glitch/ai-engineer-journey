#Student Grade Calculator
class student:
    def __init__(self,name,maths,english,science):
        self.name=name
        self.maths=maths
        self.english=english
        self.science=science

    def grade(self):
        marks=[self.maths,self.science,self.english]
        avg =sum(marks)/len(marks) 
        if avg >90:
            grade ="A"     # 90+ → A
        elif avg>75:
            grade="B"     #75+ → B
        elif avg>60:
            grade="C"     #60+ → C
        else:
            grade="D"    #Below → D
        print(f'{self.name} has a {grade} grade')
        return grade
    


s=student("jhon",95,59,32)
s2=student("dia",95,95,80)

a=print(s.grade())
b=print(s2.grade())

    

    
