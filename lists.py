# List Operations and Methods - Day 3 Example

# 1. Basic List Operations
fruits = ['apple', 'banana', 'cherry', 'date']
print('Original:', fruits)

# Adding elements
fruits.append('elderberry')
fruits.insert(2, 'blueberry')
print('After append & insert:', fruits)

# Removing elements
fruits.remove('banana')
popped = fruits.pop()
print('After remove & pop:', fruits, '| Popped:', popped)

# Slicing and indexing
print('First 3:', fruits[:3])
print('Last 2:', fruits[-2:])
print('Reversed:', fruits[::-1])

# List comprehensions
numbers = [x**2 for x in range(10) if x % 2 == 0]
print('Even squares:', numbers)

# Sorting
fruits.sort()
print('Sorted:', fruits)