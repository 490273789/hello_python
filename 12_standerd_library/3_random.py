# random
import random

a = random.random()  # Generates a random float between 0.0 and 1.0
print(f"Random float: {a}")

b = random.randint(1, 10)  # Generates a random integer between 1 and 10
print(f"Random integer between 1 and 10: {b}")

c = random.choice(['apple', 'banana', 'cherry'])  # Randomly selects an item from a list
print(f"Random choice from list: {c}")

d = random.sample(range(1, 100), 5)  # Randomly selects 5 unique items from a range
print(f"Random sample of 5 unique numbers from 1 to 99: {d}")

e = random.shuffle(d)  # Shuffles the list in place
print(f"Shuffled list: {d}")
 