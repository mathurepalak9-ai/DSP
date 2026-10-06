# Program 1: Stack Implementation 
Stack = []
# Push Operation
Stack.append(10)
Stack.append(20)
Stack.append(30)
print("Stack: ", Stack)

# Pop Operation
Stack.pop()
print("After Pop: ",Stack)

#Peek Operation
print("Top element:",Stack[-1])

# Program 2: Index to Postfix (Simple)

def precedence(op):
    if op == '+' or op=='-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0
def infix_to_postfix(expresson):
    Stack = []
    result = ''
    for char in expresson:
        if char.isalnum():
            result += char
        elif char == '(':
            Stack.append(char)
        elif char == ')':
            while Stack and Stack[-1] != '(':
                result += Stack.pop()
            Stack.pop()
        else:
            while (Stack and precedence(Stack[-1]) >= precedence(char)):
                result += Stack.pop()
            Stack.append(char)
    while Stack:
        result += Stack.pop()
    return result
expr = "A+B*C"
print("Postfix:", infix_to_postfix(expr))