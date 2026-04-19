Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Output Formatting

#Understanding the print() Function in Python
#Before diving into output formatting, it's important to understand the basics of the print()
#function, which is used to display information on the screen.

#Basic Examples of print()
#a) Printing Text

print("Hello, World!")
Hello, World!

#b) Printing Multiple Items

name = "Alice"
age = 25
print("Name:", name, "Age:", age)
SyntaxError: multiple statements found while compiling a single statement

#c) Using sep to Change the Separator

print("2024", "02", "07", sep="-")
2024-02-07

#d) Using end to Control Line Endings

print("Hello,", end=" ")
print("World!")
SyntaxError: multiple statements found while compiling a single statement


print("Hello,", end=" ") print("World!")
SyntaxError: invalid syntax

#Output Formatting
#1️⃣Using Commas (Simple Print Method)
#This is the most basic way to print multiple items. When you separate items with commas in
#the print() function, Python adds a space between them automatically.

name = "Alice"
age = 25
score = 95.5
# Using Commas
print("Name:", name, "Age:", age, "Score:", score)
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> #2️⃣Using Modulo Operator (% Formatting)
... #This is an older method, similar to C-style formatting.
... #You use % followed by format specifiers like %s (string), %d (integer), %f (float), etc.
... 
... name = "Bob"
... age = 30
... score = 88.75
... # Using Modulo Operator
... print("Name: %s | Age: %d | Score: %.2f" % (name, age, score))
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> #3️⃣Using f-strings (Formatted String Literals) — Python 3.6+
... #This is the most modern and recommended method.
... #Add an f before the string and use curly braces {} to insert variables directly.
... 
... name = "Charlie"
... age = 28
... score = 92.389
... # Using f-strings
... print(f"Name: {name} | Age: {age} | Score: {score:.2f}")
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> #4️⃣Using str.format() Method
... #This method works in both Python 2 and 3.
... #You use {} as placeholders and call .format() with the variables you want to insert.
... 
... name = "Diana"
... age = 22
... score = 89.456
... # Using str.format()
... print("Name: {} | Age: {} | Score: {:.1f}".format(name, age, score))
SyntaxError: multiple statements found while compiling a single statement
