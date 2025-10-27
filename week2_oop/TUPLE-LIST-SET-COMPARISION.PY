**real-time relatable example in the domain (SQL/PLSQL / data handling)**:

---
### 1. **List** → Think of it as a **table with duplicate rows allowed**

* Example: Raw transaction data where the same PAN number can appear multiple times.

```python
transactions_list = ["PAN123", "PAN234", "PAN123", "PAN456"]
print(transactions_list)
# ['PAN123', 'PAN234', 'PAN123', 'PAN456']
```

🔹 Duplicates allowed.
🔹 Order is preserved (like reading rows in order of insertion).

---

### 2. **Set** → Think of it as a **DISTINCT query result**

* Example: When you run `SELECT DISTINCT PAN_NO FROM transactions;`

```python
transactions_set = {"PAN123", "PAN234", "PAN123", "PAN456"}
print(transactions_set)
# {'PAN123', 'PAN456', 'PAN234'}
```

🔹 Duplicates removed automatically.
🔹 No guaranteed order (like Oracle doesn’t guarantee row order unless you use `ORDER BY`).

---

### 3. **Tuple** → Think of it as a **single row with multiple columns**

* Example: A record from the client master table.

```python
client = ("PAN123", "Ezhil", "Active")
print(client)
# ('PAN123', 'Ezhil', 'Active')
```

🔹 Immutable (like a fixed snapshot of a row – you don’t alter it directly).
🔹 Preserves order of elements (like column order in a table row).

---

✅ In short:

* **List** → All raw rows (duplicates allowed).
* **Set** → Distinct values only.
* **Tuple** → One fixed row.
