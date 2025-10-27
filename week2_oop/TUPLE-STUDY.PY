# 1. What is a Tuple?

* A **tuple** is a **collection** in Python, similar to a list.
* But **tuples are immutable** → once created, you cannot change, add, or remove items.
* Defined using **round brackets `()`**.

Example:

```python
# Creating a tuple
numbers = (10, 20, 30, 40)

print(numbers)       # (10, 20, 30, 40)
print(type(numbers)) # <class 'tuple'>
```

---

## 2. Why use Tuples?

✅ Tuples are **faster** than lists.
✅ Useful for **fixed data** (like coordinates, database records, constant values).
✅ Can be used as **dictionary keys** (since immutable).

---

## 3. Accessing Tuple Elements

```python
fruits = ("apple", "banana", "cherry")

print(fruits[0])   # apple
print(fruits[-1])  # cherry
```

---

## 4. Tuple Operations

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation
print(t1 + t2)   # (1, 2, 3, 4, 5, 6)

# Repetition
print(t1 * 2)    # (1, 2, 3, 1, 2, 3)

# Membership
print(2 in t1)   # True
print(7 not in t1) # True
```

---

## 5. Tuple Packing and Unpacking

```python
# Packing
person = ("Veera", 30, "Chennai")

# Unpacking
name, age, city = person
print(name)  # Veera
print(age)   # 30
print(city)  # Chennai
```

---

## 6. Special Case: Single-Element Tuple

⚠️ Without a comma, Python treats it as just a value, not a tuple.

```python
x = (5)
print(type(x))  # int

x = (5,)
print(type(x))  # tuple
```

---

## 7. Functions with Tuples

Tuples are often used as return values:

```python
def get_min_max(numbers):
    return (min(numbers), max(numbers))  # returning tuple

result = get_min_max([3, 7, 2, 9, 5])
print(result)      # (2, 9)

low, high = result
print(low, high)   # 2 9
```
