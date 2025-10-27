
#Part 1: Basic Hands-on with Tuples
#1. Creating Tuples

# Empty tuple
t1 = ()

# Tuple with values
t2 = (10, 20, 30)

# Tuple without parentheses (Python allows this)
t3 = 40, 50, 60

# Tuple with one element (must use a comma!)
t4 = (100,)  

print(t1, t2, t3, t4)

#2. Accessing and Slicing

nums = (1, 2, 3, 4, 5)

print(nums[0])      # First element
print(nums[-1])     # Last element
print(nums[1:4])    # Slice



#3. Immutability (Tuples cannot be changed)
nums = (1, 2, 3)
##nums[0] = 100  #❌  This will give an error
#TypeError: 'tuple' object does not support item assignment

# But you can create a NEW tuple
print(nums)
nums = nums + (4, 5)
print(nums)  # (1, 2, 3, 4, 5)

#4. Tuple with Mixed Data
person = ("Veera", 30, True, [100, 200])
print(person)


#🔹 Part 2: Advanced / Real-World Uses
#1. Tuple Unpacking
person = ("Veera", 30, "Chennai")

name, age, city = person
print(name, age, city)



#2. Returning Multiple Values from a Function
def get_min_max(nums):
    return (min(nums), max(nums))   # return tuple

result = get_min_max([10, 5, 88, 2])
print(result)         # (2, 88)
min_val, max_val = result
print("Min:", min_val, "Max:", max_val)


#3. Tuples as Dictionary Keys
# Coordinates as keys
locations = {
    (10.5, 20.7): "Restaurant",
    (12.1, 25.4): "Library"
}

print(locations[(10.5, 20.7)])

#4. Sorting with Tuples
students = [
    ("Arun", 85),
    ("Bala", 92),
    ("Chitra", 78)
]
print(students)
# Sort by score (second item)
students.sort(key=lambda x: x[1], reverse=True)
print(students)
students.sort(key=lambda x: x[1], reverse=False)
print(students)



#5. Nested Tuples

student = ("Aadhi", (85, 90, 78))
print(student[1][2])  # 78


#6. Enumerate with Tuples

items = ("Pen", "Book", "Laptop")
for idx, value in enumerate(items):
    print(idx, value)

'''
enumerate()
enumerate(items)


enumerate() is a built-in Python function.

It adds an automatic counter (index) to each item in an iterable (tuple, list, etc.).

So internally it produces something like:

(0, "Pen")
(1, "Book")
(2, "Laptop")
'''





'''() (10, 20, 30) (40, 50, 60) (100,)
1
5
(2, 3, 4)
(1, 2, 3)
(1, 2, 3, 4, 5)
('Veera', 30, True, [100, 200])
Veera 30 Chennai
(2, 88)
Min: 2 Max: 88
Restaurant
[('Arun', 85), ('Bala', 92), ('Chitra', 78)]
[('Bala', 92), ('Arun', 85), ('Chitra', 78)]
[('Chitra', 78), ('Arun', 85), ('Bala', 92)]
78
0 Pen
1 Book
2 Laptop
'''
