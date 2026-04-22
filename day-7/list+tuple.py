#List

#2. Creating Lists
#Lists can be created using square brackets [] or the list() constructor.
#2.1 Empty List

my_list = [] # Empty list
my_list2 = list() # Using list() constructor

#2.2 List with Elements

numbers = [1, 2, 3, 4, 5] # List of integers
fruits = ["apple", "banana", "cherry"] # List of strings
mixed = [10, "Python", 3.14, True] # Mixed data types

#2.3 List with Nested Lists

nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]


#2.4 List using list() Constructor

list_from_tuple = list((1, 2, 3)) # Converting tuple to list
string_to_list = list("Python") # ['P', 'y', 't', 'h', 'o', 'n']

#3. Accessing Elements in a List
#3.1 Using Indexing (Positive & Negative)

my_list = ["Python", "Java", "C++"]
print(my_list[0]) # Python
print(my_list[1]) # Java
print(my_list[-1]) # C++ (Negative Indexing)

#3.2 Using Slicing

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4]) # [20, 30, 40]
print(numbers[:3]) # [10, 20, 30] (from start)
print(numbers[2:]) # [30, 40, 50] (to end)
print(numbers[-3:-1]) # [30, 40]
print(numbers[::-1]) # [50, 40, 30, 20, 10] (Reverse list)

#4. Modifying Lists
#4.1 Changing Elements

numbers = [10, 20, 30, 40]
numbers[2] = 100
print(numbers) # [10, 20, 100, 40]

#4.2 Adding Elements

# Append (adds to the end)
numbers.append(50)
# Insert (adds at a specific position)
numbers.insert(1, 15)
# Extend (adds multiple elements)
numbers.extend([60, 70, 80])
print(numbers) # [10, 15, 20, 100, 40, 50, 60, 70, 80]

#4.3 Removing Elements

numbers.remove(100) # Removes first occurrence of 100
numbers.pop(2) # Removes element at index 2
numbers.pop() # Removes last element
del numbers[1] # Deletes element at index 1
numbers.clear() # Clears the entire list


#5. List Methods

numbers = [3, 1, 4, 1, 5, 9]
print(numbers.count(1)) # 2
print(numbers.index(4)) # 2
numbers.sort()
print(numbers) # [1, 1, 3, 4, 5, 9]
numbers.reverse()
print(numbers) # [9, 5, 4, 3, 1, 1]

#6. Looping Through a List
#6.1 Using for Loop

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
print(fruit)


#6.2 Using while Loop

i = 0
while i < len(fruits):
print(fruits[i])
i += 1

#6.3 Using enumerate()

for index, fruit in enumerate(fruits):
print(index, fruit)

#8. Copying a List

# Shallow Copy
list1 = [1, 2, 3]
list2 = list1.copy()

#9. Sorting and Reversing Lists

numbers = [5, 3, 8, 2]
numbers.sort() # [2, 3, 5, 8]
numbers.sort(reverse=True) # [8, 5, 3, 2]
numbers.reverse() # [2, 3, 5, 8]



#Tuples

#Tuple Creation Syntax:

# Empty Tuple
empty_tuple = ()
# Single-element Tuple (note the trailing comma)
single_tuple = (5,)
# Multi-element Tuple
my_tuple = (1, "apple", 3.5)
# Without parentheses (implicit tuple creation)
implicit_tuple = 1, 2, 3

#2. Accessing Tuple Elements
#a. Indexing
#● Access elements using zero-based indexing.
#● Syntax: tuple[index]
#● Example:

my_tuple = (10, 20, 30, 40)
print(my_tuple[2]) # Output: 30


#b. Negative Indexing
#● Access elements from the end of the tuple using negative indices.
#● Example:

my_tuple = (10, 20, 30, 40)
print(my_tuple[-1]) # Output: 40

#c. Slicing
#● Extract a portion of the tuple using slicing ([start:end:step]).
#● Syntax: tuple[start:end]
#● Example:

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4]) # Output: (20, 30, 40)

#3. Operations on Tuples
#a. Concatenation
#● Combine two or more tuples using the + operator.
#● Example:

tuple1 = (1, 2)
tuple2 = (3, 4)
new_tuple = tuple1 + tuple2 # Output: (1, 2, 3, 4)

#b. Repetition
#● Repeat the elements of a tuple using the * operator.
#● Example:

my_tuple = (1, 2)
print(my_tuple * 3) # Output: (1, 2, 1, 2, 1, 2)



#c. Membership Testing
#● Check if an element is present in the tuple using the in or not in keywords.
#● Example:

my_tuple = (1, 2, 3)
print(2 in my_tuple) # Output: True
print(5 not in my_tuple) # Output: True

#d. Tuple Unpacking
#● Assign tuple elements to multiple variables.
#● Example:

my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c) # Output: 1 2 3


#6. Immutability and Tuple Behavior
#Since tuples are immutable:
#● You cannot modify elements (tuple[0] = 10 will raise an error).
#● However, if a tuple contains mutable objects (e.g., lists), the mutable objects can still
#be changed.
#Example:

nested_tuple = (1, [2, 3])
nested_tuple[1][0] = 100
print(nested_tuple) # Output: (1, [100, 3])




