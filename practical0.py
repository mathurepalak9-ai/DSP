# Assignment Operators
x = 5
print(x)
x += 2
print(x)
x -= 3
print(x)
x *= 4
print(x)

#if statements
x = 10 
if x > 5:
    print("x is greater than 5")    

#if-else statements
x = 3
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")
    
#if-elif-else statements
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C")

#loops
#for loop
for i in range(5):
    print(i)

#while loop
i = 0
while i < 5:
    print(i)
    i += 1

#Loop Control Statements
#Break
for i in range(5):
    if i == 3:
        break
    print(i)

#Continue
for i in range(5):
    if i == 3:
        continue
    print(i)

#pass
for i in range(5):
    if i == 3:
        pass
    else:
        print(i)