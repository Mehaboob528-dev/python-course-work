#Dictionary

#1. Introduction to Dictionary
#A dictionary is defined using curly braces {}, where each key is followed by a colon :, and
#the key-value pairs are separated by commas.
#Syntax of a Dictionary:

dictionary_name = {key1: value1, key2: value2, key3: value3}

#Example of a Dictionary:

student = {
"name": "Alice",
"age": 21,
"course": "Computer Science"
}
print(student)

#Output:

{'name': 'Alice', 'age': 21, 'course': 'Computer Science'}


#2. Dictionary Operations

#2.1 Accessing Values

print(student["name"]) # Output: Alice
print(student.get("age")) # Output: 21


#2.2 Adding and Updating Items
#You can add a new key-value pair or update an existing value by assigning a new value to a
#key.

student["age"] = 22 # Updating existing key
student["city"] = "New York" # Adding a new key-value pair
print(student)

#Output:

{'name': 'Alice', 'age': 22, 'course': 'Computer Science',
'city': 'New York'}

#2.3 Removing Items from a Dictionary
#There are several ways to remove elements from a dictionary.
#Using pop(key)
#Removes the specified key and returns its value.

age = student.pop("age")
print(age) # Output: 22
print(student)

#Using del
#Deletes a specific key-value pair or the entire dictionary.

del student["course"]
print(student)

Using popitem()
Removes and returns the last inserted key-value pair.

student.popitem()
print(student)

#Using clear()
#Removes all key-value pairs, making the dictionary empty.

student.clear()
print(student) # Output: {}


#5. Nested Dictionaries
#A dictionary can contain another dictionary as its value.

students = {
"Alice": {"age": 21, "course": "CS"},
"Bob": {"age": 22, "course": "Math"}
}
print(students["Alice"]["course"]) # Output: CS

#6. Dictionary Comprehension
#You can create dictionaries dynamically using dictionary comprehension.

squares = {x: x*x for x in range(1, 6)}
print(squares) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#7. Real-Time Problems Using Dictionaries
#Problem 1: Count the Frequency of Words in a Sentence

sentence = "hello world hello python"
word_count = {}
for word in sentence.split():
word_count[word] = word_count.get(word, 0) + 1
print(word_count) # Output: {'hello': 2, 'world': 1,
'python': 1}

#Problem 2: Find the Student with the Highest Marks

students = {
"Alice": 85,
"Bob": 92,
"Charlie": 88
}
top_student = max(students, key=students.get)
print(top_student) # Output: Bob





#Sets


#Set Creation Syntax:

# Creating a set with unique elements
my_set = {1, 2, 3, 4}
# Creating an empty set (use set() function, not {})
empty_set = set()
# Set with duplicate elements (duplicates are removed automatically)
set_with_duplicates = {1, 2, 2, 3, 4}
print(set_with_duplicates) # Output: {1, 2, 3, 4}


#Example of an invalid set (due to mutable elements):

# This will raise a TypeError
invalid_set = {[1, 2], 3} # Lists are mutable and cannot be added to a set

#3. Operations on Sets

#a. Membership Testing
#● Check if an element is present using the in or not in keywords.
#● Example:

my_set = {1, 2, 3, 4}
print(3 in my_set) # Output: True
print(5 not in my_set) # Output: True


#b. Union (| or union() method)
#● Combines elements from two sets (removes duplicates).
#● Syntax: set1 | set2 or set1.union(set2)
#● Example:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 | set2 # Output: {1, 2, 3, 4, 5}

#c. Intersection (& or intersection() method)
#● Returns common elements between two sets.
#● Syntax: set1 & set2 or set1.intersection(set2)
#● Example:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 & set2 # Output: {3}

#d. Difference (- or difference() method)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 - set2 # Output: {1, 2}

#e. Symmetric Difference (^ or symmetric_difference() method)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 ^ set2 # Output: {1, 2, 4, 5}

#f. Subset (<= or issubset() method)

set1 = {1, 2}
set2 = {1, 2, 3}
print(set1 <= set2) # Output: True

#g. Superset (>= or issuperset() method)

set1 = {1, 2, 3}
set2 = {1, 2}
print(set1 >= set2) # Output: True

#h. Disjoint Sets (isdisjoint() method)

set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2)) # Output: True


#6. Immutability and Frozensets

# Creating a frozenset
frozen = frozenset([1, 2, 3])
print(frozen)
# Frozenset is immutable
# The following will raise an error
# frozen.add(4)
