# **1. What is a Class in Python?**

"""* A **class** is like a **blueprint** to create objects.
* An **object** is an actual thing created from the blueprint.
  Example:

  * Blueprint = Car design (class)
  * Object = A real Toyota or BMW car

Here,

* `Order` is a class → blueprint for an order.
* `AdminPortal` and `CustomerApp` are also classes.
* `order = Order(...)` creates an object (a real order placed by a customer).

---

# **2. What is Encapsulation?**

Encapsulation means **hiding the details** of how something works and only showing what is necessary.

Think of it like:

* A TV remote – you only see buttons (public).
* Inside circuits (private) are hidden.

In Python, we use naming conventions:

* **Public** → everyone can use (`customer_name`).
* **Protected** (starts with `_`) → should be used only inside the class or subclasses (`_get_admin_view`).
* **Private** (starts with `__`) → hidden from outside (`__total_amount`, `__discount`, `__calculate_final`).

---

# **3. The `Order` Class**

```python"""
class Order:
    def __init__(self, customer_name, items, total_amount, discount):
        self.customer_name = customer_name   # public
        self.items = items                   # public
        self.__total_amount = total_amount   # private
        self.__discount = discount           # private
"""

### **Breakdown:**

* `__init__` is a **constructor** → runs automatically when you create an object.
* `self.customer_name` → public, can be seen outside.
* `self.items` → public.
* `self.__total_amount` → private (hidden).
* `self.__discount` → private (hidden).

👉 Example:

```python"""
order = Order("Veera", ["Shoes", "Socks"], 2000, 200)

print(order.customer_name)  # ✅ Works
print(order.items)          # ✅ Works
#print(order.__total_amount) # ❌ Error (private)


# **4. Private Method**

#```python
def __calculate_final(self):
    return self.__total_amount - self.__discount

amount = __calculate_final(order)
print(amount)
"""

* Starts with `__`, so it’s private.
* Only this class can use it, **not accessible outside**.
* It calculates the **final price** after applying discount.

👉 Example:
If total = ₹2000 and discount = ₹200 → final bill = ₹1800.

---

# **5. Protected Method**

```python"""
def _get_admin_view(self):
    return {
        "Customer": self.customer_name,
        "Items": self.items,
        "Total Amount": f"₹{self.__total_amount}",
        "Discount Applied": f"₹{self.__discount}",
        "Final Bill": f"₹{self.__calculate_final()}"
    }
"""```

* `_` means **protected** (not strict in Python, but by convention).
* Gives a **detailed order summary**:

  * Customer name
  * Items
  * Total amount before discount
  * Discount applied
  * Final bill after discount

This is useful for **admins** who need to see everything.

---

# **6. Public Method**

```python"""
def get_customer_view(self):
    return {
        "Customer": self.customer_name,
        "Items": self.items,
        "Final Bill": f"₹{self.__calculate_final()}"
    }
"""```

* This is **public**.
* Anyone can access it.
* Customers don’t need to see sensitive details like **total amount** and **discount**, they only care about the **final bill**.

---

# **7. AdminPortal Class**

```python"""
class AdminPortal:
    def show_order(self, order):
        return order._get_admin_view()
"""```

* This is like the **Admin’s screen**.
* It calls `_get_admin_view()` from `Order`.
* Shows **complete details** to the admin.

---

# **8. CustomerApp Class**

```python"""
class CustomerApp:
    def show_order(self, order):
        return order.get_customer_view()
"""```

* This is the **Customer’s app screen**.
* It calls `get_customer_view()` from `Order`.
* Shows **only final bill + items**.

---

# **9. Example of How It Works**

```python"""
order = Order("Veera", ["Shoes", "Socks"], 2000, 200)

admin = AdminPortal()
customer = CustomerApp()

print(admin.show_order(order))
# {'Customer': 'Veera', 'Items': ['Shoes', 'Socks'],
#  'Total Amount': '₹2000', 'Discount Applied': '₹200',
#  'Final Bill': '₹1800'}

print(customer.show_order(order))
# {'Customer': 'Veera', 'Items': ['Shoes', 'Socks'],
#  'Final Bill': '₹1800'}
"""```

👉 Admin sees everything (₹2000 total, ₹200 discount, ₹1800 final).
👉 Customer sees only what matters (₹1800 final).

---

# **10. Summary of Key Concepts**

* **Class = Blueprint**, **Object = Real instance**
* **Encapsulation = Hiding details & exposing only necessary parts**
* **Public** → Everyone can see (`customer_name`, `items`, `get_customer_view`)
* **Protected** → For trusted users (`_get_admin_view`)
* **Private** → Hidden, used only inside class (`__total_amount`, `__discount`, `__calculate_final`)
* **Different views for different users** → Admin vs Customer

---
"""
