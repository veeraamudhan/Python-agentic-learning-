# 📘 Python Lists

## **1. What is a List?**

* Ordered collection of elements.
* **Mutable** → you can change elements after creation.
* Can contain **different data types**: `int`, `str`, `float`, even other lists.
* Allows **duplicates**.

---

## **2. Creating a List**

```python
# Empty list
my_list = []

# List with values
fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30, 40]
mixed = [1, "Veera", 3.14, True]

print(fruits)
print(numbers)
print(mixed)
```

---

## **3. Accessing Elements**

```python
fruits = ["apple", "banana", "mango"]

print(fruits[0])   # first element
print(fruits[-1])  # last element
print(fruits[0:2]) # slice (first two elements)
```

---

## **4. Adding Elements**

```python
fruits = ["apple", "banana"]

fruits.append("mango")        # add at end
fruits.insert(1, "orange")    # insert at index 1
fruits.extend(["grapes", "kiwi"]) # add multiple

print(fruits)
```

---

## **5. Removing Elements**

```python
fruits = ["apple", "banana", "mango", "orange"]

fruits.remove("banana")   # remove by value
popped = fruits.pop()     # remove last element
del fruits[0]             # remove by index

print(fruits, popped)
```

---

## **6. Useful Methods**

```python
numbers = [10, 20, 30, 10, 40]

print(numbers.count(10))  # count occurrences
print(numbers.index(30))  # index of element
numbers.sort()            # sort ascending
numbers.reverse()         # reverse order
print(numbers)
```

---

## **7. Iterating Through a List**

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

# Using index
for i in range(len(fruits)):
    print(i, fruits[i])
```

---

## ✅ Mini Challenge

1. Create a list of **5 clients’ names**.
2. Add 2 more clients.
3. Remove the first client.
4. Print all clients using a **for loop**.

