# Functions - Parameters, Scope & Lambda

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Gourav"))
print(greet("Bro", "Namaste"))

# Lambda
square = lambda x: x ** 2
print("Square of 8:", square(8))

# *args and **kwargs
def total(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
    return sum(args)

print("Total:", total(10, 20, 30, tax=5, discount=2))