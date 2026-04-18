Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #Input Formatting
>>> 
>>> #1. String Input
... #Use case: Entering a name, email, city, etc.
... 
... name = input("Enter your full name: ")
Enter your full name: MEHABOOB
>>> print(name)
MEHABOOB
>>> 
>>> #2. Integer Input
... #Use case: Age, quantity, mobile number, number of items in cart.
... 
... quantity = int(input("Enter the number of items: "))
Enter the number of items: 5
>>> print(quantity)
5
>>> 
>>> #3. Float Input
... #Use case: Price, temperature, discount, rating.
... 
... price = float(input("Enter the product price: "))
Enter the product price: 565.22
>>> print(price)
565.22
>>> 
>>> #4. Input as List (Space-separated)
... #Use case: List of names, marks, or product IDs.
... 
... names = input("Enter employee names (space-separated):").split()
Enter employee names (space-separated):mehaboob dikshit aman
>>> print(names)
['mehaboob', 'dikshit', 'aman']
>>> 
>>> #5. Input as List (Comma-separated)
... #Use case: Tags, emails, product categories.
... 
... tags = input("Enter tags (comma-separated): ").split(',')
Enter tags (comma-separated): sale, discount ,new
print(tags)
['sale', ' discount ', 'new']

#6. List of Integers
#Use case: Marks, product prices, IDs.

marks = list(map(int, input("Enter marks: ").split()))
Enter marks: 55 75 71 61
print(marks)
[55, 75, 71, 61]

#7. List of Floats
#Use case: Sensor readings, weights, product prices.

weights = list(map(float, input("Enter weights: ").split()))
Enter weights: 55.6 77.5 55.9
print(weights)
[55.6, 77.5, 55.9]


#8. Tuple Input
#Use case: Coordinates, dimensions (length, width, height).

dimensions = tuple(map(int, input("Enter length, width, height: ").split()))
Enter length, width, height: 5 20 10
print(dimensioms)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(dimensioms)
NameError: name 'dimensioms' is not defined. Did you mean: 'dimensions'?
print(dimensions)
(5, 20, 10)


#9. Set Input
#Use case: Selected image IDs where duplicates must be removed (e.g., in a photo-sharing
#app).

selected_ids = set(map(int, input("Enter selected image IDs: ").split()))
Enter selected image IDs: 101 102 103 104 105
print(selected_ids)
{101, 102, 103, 104, 105}





#10. Dictionary Input using eval()
#Use case: When entering structured data like configuration settings or user profiles.

profile = eval(input("Enter user profile as a dictionary: "))
Enter user profile as a dictionary: {'name': 'Mehaboob', 'age':23, 'role': 'Developer'}
print(profile)
{'name': 'Mehaboob', 'age': 23, 'role': 'Developer'}


#11. Multiple Inputs with Unpacking
#Use case: Login form or payment details.

username, password = input("Enter username and password: ").split()
Enter username and password: user05 mypassword125
print(username , password)
user05 mypassword125
print("username:",username)
username: user05
("username:",username)
