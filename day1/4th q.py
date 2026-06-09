class Student:
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks
    def grade_calc(self, marks):
        if marks>=90:
            return 'A'
        elif self.marks>=80:
            return 'B'
        elif self.marks>=70:
            return 'C'
        elif self.marks>=60:
            return 'D'
        else:
            return 'F'
    
    def display(self):
        print("ID: ",self.id)
        print("Name: ",self.name)
        print("Grade: ",self.grade_calc(self.marks))

n=int(input("Enter Number of students: "))

std=[]
for i in range(n):
    id=int(input("Enter Student ID of " + str(i+1) + ": "))
    name=input("Enter Student Name of " + str(i+1) + ": ")
    marks=int(input("Enter Student Marks of " + str(i+1) + ": "))
    stdnt=Student(id,name,marks)
    std.append(stdnt)
for s in std: 
    s.display()
    grade=s.grade_calc(s.marks)

