#Tuple Operations
t = (10, 20, 30, 40, 50)
print("Tuple elements:", t[1])

#Set Operations
s = {1, 2, 3, 4}
print("Set elements:", s)
s.add(5)
print("Set:", s)

#Dictionary Operations
student = {"name": "Arun", "age": 15, "marks": 85}

#Accessing values
print("Name:", student["name"])

#Updating values
student["marks"] = 90

#Adding values
student["city"] = "Nagpur"

#Deleting values
del student["age"]
print("Updated student dictionary:", student)


#Built-in functions
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
