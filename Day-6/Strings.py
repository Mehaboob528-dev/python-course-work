Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
str1 = "hello"
str2 = "world"
str3 = '''this is multi-line string example'''
print(str1)
hello
print(str2)
world
print(str3)
this is multi-line string example

# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
SyntaxError: multiple statements found while compiling a single statement
# Concatenation
str1 = "Hello"
str2 = "Worlld"
result = str1 + " " + str2
print(result)
SyntaxError: multiple statements found while compiling a single statement


# Concatenation
str1 = "hello"
str2 = "world"
result = str1+" " + str2
print(result)
hello world
hello world
SyntaxError: invalid syntax

# Repetition
print("Python! " * 3)
Python! Python! Python! 

# Indexing
text = "python"
print(text[0])
p
print(text[-1])
n

# Slicing
print(text[0:3])
pyt
print(text[:4])
pyth
>>> print(text[2:])
thon
>>> 
>>> 
>>> # Membership
>>> print("Pyt in text")
Pyt in text
>>> print("java" not in text)
True
>>> '''1. len() - Returns the length of the string.
... 2. max() / min() - Returns the maximum or minimum character (based on ASCII
... values).
... 3. sorted() - Returns a sorted list of characters.
... 4. chr() / ord() - Converts between characters and their ASCII codes.'''
'1. len() - Returns the length of the string.\n2. max() / min() - Returns the maximum or minimum character (based on ASCII\nvalues).\n3. sorted() - Returns a sorted list of characters.\n4. chr() / ord() - Converts between characters and their ASCII codes.'
>>> 
>>> # 1. len()
>>> text = "hello world"
>>> print(len(text))
11
>>> 
>>> # 2. max() and min()
>>> print(max("abcXYZ"))
c
>>> print(min("abcXYZ"))
X
>>> 
>>> # 3. sorted()
>>> print(sorted("python"))
['h', 'n', 'o', 'p', 't', 'y']
>>> 
>>> # 4. chr() and ord()
>>> print(ord('A'))
65
>>> print(chr(97))
a
