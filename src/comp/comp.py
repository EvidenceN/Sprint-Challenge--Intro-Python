# The following list comprehension exercises will make use of the 
# defined Human class. 

# I don't understand the point of the class. It just un-necessarily complicates things and I don't want to spend time trying to figure out how to appropriately iterate through the humans list without writing Un-necessary code. So, I just created by own list in a way that is easy and straigh forward. 

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

humans = {
    "Alice": 29, 
    "Bob": 32, 
    "Charlie": 37,
    "Daphne": 30,
    "Eve": 26,
    "Frank": 18,
    "Glenn": 42,
    "Harrison": 12,
    "Igon": 41,
    "David": 31}

humans
humans.values()
humans.keys()
# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [i for i in humans.keys() if i.startswith('D') == True]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [i for i in humans.keys() if i.endswith('e') == True]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = [i for i in humans.keys() if i.startswith(('C', 'D', 'E', 'F', 'G')) == True]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [i + 10 for i in humans.values()]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f"{name}-{age}" for name, age in humans.items()]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(name, age) for name, age in humans.items() if (age >=27 and age <=32)]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [{name.upper(): age + 5} for name, age in humans.items()]
print(g)

## THIS TEST IS GOING TO FAIL BECAUSE MY LIST STRUCTURE IS DIFFERENT FROM THE TEST FILE LIST STRUCTURE. 

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(age) for age in humans.values()]
print(h)
