#Functions

#Syntax of a Function in Python:

def function_name(parameters):
"""Docstring explaining the function"""
# Function body
return value # Optional

#Example:

def greet(name):
"""This function returns a greeting message."""
return f"Hello, {name}!"
print(greet("Alice")) # Output: Hello, Alice!


#Types of Functions


#1. Built-in Functions

print(len("Hello")) # Output: 5
print(abs(-10)) # Output: 10
print(max(1, 5, 3)) # Output: 5
print(sorted([3, 1, 4, 2])) # Output: [1, 2, 3, 4]

#2. User-Defined Functions

def add(a, b):
"""This function adds two numbers."""
return a + b

print(add(5, 10)) # Output: 15

#Function Arguments

#1. Positional Arguments

def greet(name, age):
print(f"Hello {name}, you are {age} years old.")
greet("Alice", 25)

#2. Keyword Arguments
greet(age=25, name="Alice")

#3. Default Arguments

def greet(name, age=18):
print(f"Hello {name}, you are {age} years old.")

greet("Bob") # Uses default age=18

#4. Variable-Length Arguments

def add(*numbers):
return sum(numbers)

print(add(1, 2, 3, 4, 5))


#**kwargs (Arbitrary Keyword Arguments)

def user_info(**details):
for key, value in details.items():
print(f"{key}: {value}")

user_info(name="Alice", age=25, city="New York")

#Scope of Variables

#1. Local Scope

def greet():
message = "Hello"
print(message)
greet()
# print(message) # Error: message is not defined outside

#2. Global Scope

x = 10 # Global variable
def show():
print(x) # Accessing global variable
show()

x = 10
def update():
global x
x = 20
update()
print(x) # Output: 20

#3. Enclosing Scope (Nonlocal Scope)

def outer():
msg = "Hi"
def inner():
    print(msg) # Enclosing scope variable
inner()
outer()

#To modify the enclosing variable, use nonlocal:

def outer():
msg = "Hi"
def inner():
nonlocal msg
msg = "Hello"
inner()
print(msg) # Output: Hello
outer()

#4. Built-in Scope

print(len("Python")) # len is a built-in function

#Avoid using built-in names as variable names:

len = 5 # Overrides the built-in len
print(len("test")) # Error

#Example of LEGB Rule

x = "global"
def outer():
x = "enclosing"
def inner():
x = "local"
print(x) # Looks for local, enclosing, global,

built-in
inner()
outer()

#Shadowing Variables

x = 100
def func():
x = 50 # Local variable shadows global x
print(x)
func()
print(x) # Global x remains unaffected



