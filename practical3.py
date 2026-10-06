#Createing a list
numbers = [10, 20, 30, 40, 50]

#Accessing values
print("First element:", numbers[0])  # Accessing the first element
print("Last element:", numbers[-1])  # Accessing the last element

#Updating values
numbers[2] = 35  # Updating the third element
print("Updated list:", numbers)

#Adding values
numbers.append(60)  # Adding an element at the end
print("List after appending:", numbers)
numbers.insert(2, 15)  # Inserting an element at index 2
print("List after inserting 15 at index 2:", numbers)

#Removing values
numbers.remove(20)  # Removing a specific element
print("List after removing 20:", numbers)

#Built-in functions
print("Length of the list:", len(numbers))  # Length of the list
print("Max:", max(numbers))  # Maximum value in the list
print("Min:", min(numbers))  # Minimum value in the list
numbers.sort()  # Sorting the list
print("Sorted list:", numbers)
print("Sum:", sum(numbers))  # Sum of all elements in the list

