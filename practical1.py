#Student Data System
#Demonstrates Python building blocks, data types, and I/O

print("=== Student Data System ===")

#Input section (user provided data)
name = input("Enter student name: ") #str
roll_no = int(input("Enter roll number: ")) #int
age = int(input("Enter age: ")) #int
marks = float(input("Enter marks: ")) #float
is_passed = marks >= 40 #bool (logical expression)

#Processing Section
percentage = (marks / 100) * 100 #float

#Output section 
print("\n=== Student Details ===")
print("Name:", name)
print("Roll Number:", roll_no)
print("Age:", age)
print("Marks:", marks)
print("Percentage:", percentage)
print("Result:", "Passed" if is_passed else "Failed")

#Display data type of each variable
print("\n=== Data Types ===")
print("Name:", type(name))
print("Roll Number:", type(roll_no))
print("Age:", type(age))
print("Marks:", type(marks))
print("Percentage:", type(percentage))
print("Result:", type("Passed" if is_passed else "Failed"))