import random\

print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))

l=['java','python','ai','ml']

print(random.choice(l))
print(random.choice(l,k=2))

print("Before:",l)
random.shuffle(l)
print("After:")
