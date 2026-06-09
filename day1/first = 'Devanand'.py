name = input("Enter name of student: ")
math = int(input("Enter marks in math: "))
physics = int(input("Enter mark in physics: "))
JAVA = int(input("Enter marks in JAVA:"))
DBMS = int(input("Enter marks in DBMS: "))
OOPS = int(input("Enter marks in OOPS: "))
Average = (math + physics + JAVA + DBMS + OOPS)/5
print (Average)
if Average >= 90:
    print("Grade A")
elif Average >= 80:
    print("Grade B")            
elif Average >= 70:
    print("Grade C")
elif Average >= 60:
    print("Grade D")
else:
    print("Grade F")
