# Let's look at another example of data using lists
first_names = ['Marcus', 'Kristin', 'Adam', 'Kimberly', 'Judith']
last_names = ['Mcguire', 'Cantu', 'Mendez', 'Wolf', 'Johnson']
grades = [3.3, 2.7, 3.7, 2.7, 3.0]

# How do we get Adam's grade?
# Using a for loop:
target_name = 'Adam'
for name, grade in zip(first_names, grades):
    if name == target_name:
        print(f'{name}\'s grade is {grade}')

# Or using the .index method:
target_index = first_names.index(target_name)
print(grades[target_index])

# We can represent a single student using a dictionary;
#  dictionaries are collections of key-value pairs.
student = {
    'first_name': 'Marcus',
    'last_name': 'Mcguire',
    'grade': 3.3
}

# We can access information by key, rather than by index (as in lists).
print(student['last_name'])

# We can combine dictionaries with lists to represent all students:
students = [
    {'first_name': 'Marcus', 'last_name': 'Mcguire', 'grade': 3.3},
    {'first_name': 'Kristin', 'last_name': 'Cantu', 'grade': 2.7},
    {'first_name': 'Adam', 'last_name': 'Mendez', 'grade': 3.7},
    {'first_name': 'Kimberly', 'last_name': 'Wolf', 'grade': 2.7},
    {'first_name': 'Judith', 'last_name': 'Johnson', 'grade': 3.0}
]

# As with nested lists, we can chain the square brackets to get information
print(students[2]['last_name'])

# Now, how do we find Judith's grade?
target_name = 'Judith'
for student in students:
    if student['first_name'] == target_name:
        print(student['grade'])


# Hmm, there must be a better way...
# I've heard pandas are pretty cool animals
import pandas as pd

students_dataframe = pd.DataFrame(students)
print(students_dataframe)  # This looks a bit like a table!

# We can access information from a dataframe in several ways:
print(students_dataframe['first_name'])  # By column name
print(students_dataframe.iloc[3])  # By row index
print(students_dataframe.loc[3, 'first_name'])  # By both

# Unlike with standard lists or dictionaries, we can easily
#  perform operations on a whole column:
target_name = 'Judith'
mask = students_dataframe['first_name'] == target_name

# This results in a 'mask': a series of Boolean (True/False) values,
#  one for each row, indicating whether the condition was met.
#  (In this case, whether first_name == target_name)
print(mask)

# We can then use this mask to get information belonging to this row:
print(students_dataframe.loc[mask, 'grade'])  # Like the grade
print(students_dataframe.loc[mask])  # Or the whole row
print(students_dataframe.loc[mask, ['last_name', 'grade']])  # Or multiple columns!

# We can also do all of this in a single line:
print(students_dataframe.loc[students_dataframe['first_name'] == target_name, 'grade'])

# Pandas, like numpy, has lots of built-in methods to make your life easy. 
# For instance, to get the student with the highest grade:
index = students_dataframe['grade'].argmax()
print(students_dataframe.iloc[index])
