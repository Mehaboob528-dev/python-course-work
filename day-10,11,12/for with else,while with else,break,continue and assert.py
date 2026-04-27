#Control Statements

#FOR LOOP


# User's workout record over a week
workout_log = [1, 1, 1, 0, 1, 1, 0]
current_streak = 0
longest_streak = 0
for day in workout_log:
if day == 1:
current_streak += 1
if current_streak > longest_streak:
longest_streak = current_streak

else:
current_streak = 0 # Streak breaks
print("Longest workout streak:", longest_streak)




#WHILE LOOP



# Simulating incorrect login attempts
correct_pin = "1234"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
entered_pin = input("Enter your PIN: ")
if entered_pin == correct_pin:
print("Login successful!")
break
else:
print("Incorrect PIN. Try again.")
attempts += 1

else:
print("Account locked due to too many failed attempts.")


#Sample Input/Output:
'''Enter your PIN: 1111
Incorrect PIN. Try again.
Enter your PIN: 2222
Incorrect PIN. Try again.
Enter your PIN: 3333
Incorrect PIN. Try again.
Account locked due to too many failed attempts.'''


#FOR LOOP WITH ELSE


# 1 = Unread, 0 = Read
notifications = [0, 0, 0, 0]
for notification in notifications:
if notification == 1:
print("You have unread notifications!")
break

else:
print("All caught up!")


#WHILE LOOP WITH ELSE


# Simulating OTP verification
correct_otp = "7890"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
entered_otp = input("Enter OTP: ")
if entered_otp == correct_otp:
print("OTP Verified Successfully!")
break
else:
print("Incorrect OTP. Try again.")
attempts += 1

else:
print("OTP expired. Request a new one.")


#Sample Input/Output:
'''Enter OTP: 1111
Incorrect OTP. Try again.
Enter OTP: 2222
Incorrect OTP. Try again.
Enter OTP: 3333
Incorrect OTP. Try again.
OTP expired. Request a new one.'''

#break Statement in Python


for item in iterable:
if condition:
break

#or

while condition:
if exit_condition:
break


# Search for a number in a list
numbers = [1, 3, 5, 7, 9, 11]
target = 7
for num in numbers:
if num == target:
print("Target found:", num)
break


#continue Statement in Python

for item in iterable:
if condition:
continue
# rest of the loop

#OR

while condition:
if skip_condition:
continue
# rest of the loop


# Print odd numbers only
for num in range(1, 10):
if num % 2 == 0:
continue
print(num)


#assert Keyword in Python

assert condition

#OR

assert condition, "Error message"

#Example:

x = 10
assert x > 0, "x must be positive"


