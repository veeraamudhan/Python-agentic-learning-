
## 🔹 **Sets in Python**
'''
* A **set** is an unordered collection of unique elements.
* Defined using `{}` or the `set()` function.
* Useful when:

  * You need to remove duplicates.
  * You want to perform mathematical set operations (union, intersection, difference).

---
'''
### 1. **Creating Sets**


# Creating a set
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Duplicate values are ignored
numbers = {1, 2, 2, 3, 4, 4, 5}
print(numbers)   # Output: {1, 2, 3, 4, 5}

# Empty set (must use set(), not {})
empty_set = set()
print(type(empty_set))



### 2. **Adding & Removing Elements**


fruits = {"apple", "banana"}

# Add
fruits.add("cherry")
print(fruits)  # {"apple", "banana", "cherry"}

# Update with multiple elements
fruits.update(["orange", "grape"])
print(fruits)

# Remove (gives error if not found)
fruits.remove("banana")
print(fruits)
# Discard (no error if not found)
fruits.discard("pineapple")
print(fruits)
# Pop (removes random item)
print(fruits.pop())
print(fruits)



### 3. **Set Operations**


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))        # {1, 2, 3, 4, 5, 6}
print(a.intersection(b)) # {3, 4}
print(a.difference(b))   # {1, 2}
print(b.difference(a))   # {5, 6}
print(a.symmetric_difference(b))  # {1, 2, 5, 6}



### 4. **Set Comprehension**


# Create a set of squares
squares = {x**2 for x in range(6)}
print(squares)  # {0, 1, 4, 9, 16, 25}


