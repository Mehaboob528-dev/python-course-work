Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Type Conversion (Type Casting)
#1. Converting from int
#Given:
int_a = 2

#2. Converting from float
#Given:

float_n = 3.1

#3. Converting from str
#Given:

string_c = 'power'

#4. Converting from list
#Given:

list_d = [1, 2, 3, 4]


#5. Converting from tuple
#Given:

tuple_f = (1, 2, 3, 4)

#6. Converting from set
#Given:

set_e = {3, 4, 5, 6}

#7. Converting from dict
#Given:

dict_g = {1: 1, 2: 4, 3: 9}

#8. Converting from bool
#Given:

boolean = False

#9. Dictionary Conversion
#To convert a list to a dictionary, it must be a list of key-value tuples.

d = [('name', 'teja'), ('batch', '22'), ('subject', 'python')]
dict(d)
# Output: {'name': 'teja', 'batch': '22', 'subject': 'python'}
SyntaxError: multiple statements found while compiling a single statement

#Python Operators

#1. Arithmetic Operators

#Example:

a = 10
b = 3
print(a + b) # Output: 13
print(a - b) # Output: 7
print(a * b) # Output: 30
print(a / b) # Output: 3.3333
print(a // b) # Output: 3
print(a % b) # Output: 1
print(a ** b) # Output: 1000
SyntaxError: multiple statements found while compiling a single statement

#2. Comparison Operators

Example:

x = 10 y = 5
print(x == y) # Output: False
print(x != y) # Output: True
print(x > y) # Output: True
print(x < y) # Output: False
print(x >= 10) # Output: True
print(y <= 5) # Output: True
SyntaxError: invalid syntax

#3. Assignment Operators

#Example:

x = 10
x += 5 # x = x + 5 → 15
x *= 2 # x = x * 2 → 30
x -= 10 # x = x - 10 → 20
print(x) # Output: 20
SyntaxError: multiple statements found while compiling a single statement

#4. Logical Operators (Using Logic Gates)

>>> #Example:
... 
... x = 10 y = 20
... print(x > 5 and y < 30) # Output: True (Both conditions are
... True)
... print(x > 15 or y < 30) # Output: True (At least one
... condition is True)
... print(not (x > 5)) # Output: False (Reverses the Truecondition)
... 
... #5. Membership Operators
SyntaxError: unmatched ')'
>>> 
>>> #Example:
... 
... fruits = ["apple", "banana", "cherry"]
... print("apple" in fruits) # Output: True
... print("grape" not in fruits) # Output: True
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> #6. Identity Operators
>>> 
>>> #Example:
... 
... a = [1, 2, 3] b = a c = [1, 2, 3]
... print(a is b) # Output: True (Both refer to the same object)
... print(a is c) # Output: False (Different objects with the same content)
... print(a is not c) # Output: True
SyntaxError: invalid syntax
>>> 
>>> #7. Bitwise Operators (With Binary Representation)
>>> 
>>> x = 5 # Binary: 0101
... y = 3 # Binary: 0011
... print(x & y) # Output: 1 (Binary: 0001 → AND operation)
... print(x | y) # Output: 7 (Binary: 0111 → OR operation)
... print(x ^ y) # Output: 6 (Binary: 0110 → XOR operation)
... print(~x) # Output: -6 (Binary: Inverts bits of 5)
... print(x << 1) # Output: 10 (Binary: 1010 → Shifts left by 1)
... print(x >> 1) # Output: 2 (Binary: 0010 → Shifts right by 1)
SyntaxError: multiple statements found while compiling a single statement
