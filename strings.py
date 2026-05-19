# String Manipulation Examples

name = "Gourav Patil"
print("Original:", name)
print("Upper:", name.upper())
print("Lower:", name.lower())
print("Title:", name.title())

# Splitting and joining
sentence = "Python is awesome for data science"
words = sentence.split()
print("Words:", words)
print("Joined:", "-".join(words))

# Formatting
age = 25
print(f"My name is {name} and I am {age} years old.")
print("Format method:", "Hello, {}!".format(name))

# String methods
print("Contains 'Python':", "Python" in sentence)
print("Starts with 'Py':", sentence.startswith("Py"))
print("Replace:", sentence.replace("awesome", "powerful"))