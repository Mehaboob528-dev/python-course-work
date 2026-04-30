#Recursive Functions

#Example 1: Factorial of a Number

n! = n × (n - 1) × (n - 2) × ... × 1

#Factorial using recursion:

def factorial(n):
if n == 0 or n == 1: # Base case
return 1
else:
return n * factorial(n - 1) # Recursive case

print(factorial(5)) # Output: 120

#How it works for factorial(5):

factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1
= 120

#Example 2: Fibonacci Series

0, 1, 1, 2, 3, 5, 8, ...

#Where:

F(0) = 0, F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1


def fibonacci(n):
if n == 0:
return 0
elif n == 1:
return 1
else:
return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6)) # Output: 8

#How it works:

fibonacci(4)
= fibonacci(3) + fibonacci(2)
= (fibonacci(2) + fibonacci(1)) + (fibonacci(1) +
fibonacci(0))
= ((fibonacci(1) + fibonacci(0)) + 1) + (1 + 0)
= ((1 + 0) + 1) + 1 = 3


#Example 3: Sum of Natural Numbers


def sum_natural(n):
if n == 1:
return 1
else:
return n + sum_natural(n - 1)

print(sum_natural(5)) # Output: 15 (5 + 4 + 3 + 2 + 1)


#Pass by Value and Pass by Reference

#Example: Pass by Value (Immutable Objects)


def modify_value(num):
num += 10 # This creates a new local variable
print("Inside function:", num)

x = 5
modify_value(x)
print("Outside function:", x) # x remains unchanged

#Output:


Inside function: 15
Outside function: 5

#Example: Pass by Reference (Mutable Objects)

def modify_list(lst):
lst.append(4) # Modifies the original list

numbers = [1, 2, 3]
Python
modify_list(numbers)
print(numbers) # Output: [1, 2, 3, 4]

#How to Prevent Unintended Modifications?

def modify_list_copy(lst):
lst = lst[:] # Creates a copy
lst.append(5)
print("Inside function:", lst)

numbers = [1, 2, 3]
modify_list_copy(numbers)
print("Outside function:", numbers) # Original list remains unchanged
