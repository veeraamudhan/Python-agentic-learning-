

### 📘 Dictionaries in Python
'''
* A **dictionary** is a collection of **key-value pairs**.
* Keys must be **unique** (like column names in a database).
* Values can be of any type (like cell values in a table).

---
'''
### 🔑 Basic Example


student = {
    "name": "Arun",
    "age": 21,
    "marks": 85
}

print(student["name"])   # Access by key → Arun
print(student.get("age")) # Safer way → 21


### 🔄 Adding / Updating


student["marks"] = 90     # Update
student["city"] = "Chennai"  # Add new key-value

print(student)
# {'name': 'Arun', 'age': 21, 'marks': 90, 'city': 'Chennai'}


### 🚫 Removing


student.pop("age")   # Remove by key
print(student)


### 📊 Iterating


for key, value in student.items():
    print(key, ":", value)


### ✅ Real-Time Domain Example (Mutual Funds / Clients)

#Think of a **dictionary** like storing client data:

client = {
    "PAN": "ABCDE1234F",
    "Name": "Veera",
    "Funds": ["Equity", "Debt"],
    "Balance": 500000
}
print(client)

for key, value in client.items():
    print(key, ":", value)
'''
* Here, `"PAN"` is like a **primary key** in a database.
* `"Funds"` can be a list (because one client can have multiple funds).
* Dictionary allows **fast lookup** by `PAN`.

---'''
