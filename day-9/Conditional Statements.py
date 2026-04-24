#Conditional Statements

#1. if Statement

if condition:
# Code to execute if the condition is True

#Example: Checking Amazon Stock Availability

amazon_stock = 20 # Number of items in stock
if amazon_stock > 0:
print("Amazon stock is available!")


#2. if-else Statement

if condition:
# Code to execute if the condition is True
else:
# Code to execute if the condition is False

#Example: Checking If Amazon Stock is Out of Stock

amazon_stock = 0 # No stock available
if amazon_stock > 0:
print("Amazon stock is available!")
else:
print("Sorry, Amazon stock is out of stock.")

#3. if-elif-else Statement


if condition1:
# Code if condition1 is True
elif condition2:
# Code if condition2 is True
elif condition3:
# Code if condition3 is True
else:
# Code if none of the conditions are True

#Example: Amazon Stock with Different Stock Levels

amazon_stock = 5 # Limited stock available
if amazon_stock > 20:
print("Amazon stock is fully available.")
elif amazon_stock > 0:
print("Amazon stock is low, hurry up!")
else:
print("Sorry, Amazon stock is out of stock.")

#4. Nested Conditional Statements

if condition1:
# Code if condition1 is True
if condition2:
# Code if both condition1 and condition2 are True
else:
# Code if condition1 is True but condition2 is False

else:
# Code if condition1 is False

#Example: Amazon Stock with Prime Customer Priority

amazon_stock = 3
is_prime_customer = True
if amazon_stock > 0:
print("Amazon stock is available!")
if is_prime_customer:
print("Prime customer gets priority shipping!")
else:
print("Standard shipping will apply.")

else:
print("Sorry, Amazon stock is out of stock.")
