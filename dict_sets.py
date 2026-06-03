# Dictionary and Set Examples

# Dictionary
student = {
    'name': 'Gourav',
    'age': 25,
    'skills': ['Python', 'Django', 'ML'],
    'active': True
}

print('Student:', student)
print('Name:', student['name'])
print('Skills:', student.get('skills'))



# Update and add
student['age'] = 26
student['city'] = 'Baramati'
print('Updated:', student)

# Set examples

unique_nums = {1, 2, 2, 3, 4, 4, 5}
print('Unique set:', unique_nums)

skills1 = {'Python', 'Django'}
skills2 = {'Django', 'FastAPI', 'SQL'}

print('Union:', skills1 | skills2)
print('Intersection:', skills1 & skills2)
