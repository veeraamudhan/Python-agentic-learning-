class Order:
    def __init__(self, customer_name, items, total_amount, discount):
        self.customer_name = customer_name   # public
        self.items = items                   # public
        self.__total_amount = total_amount   # private
        self.__discount = discount           # private

    # private method
    def __calculate_final(self):
        return self.__total_amount - self.__discount

    # protected method
    def _get_admin_view(self):
        return {
            "Customer": self.customer_name,
            "Items": self.items,
            "Total Amount": f"₹{self.__total_amount}",
            "Discount Applied": f"₹{self.__discount}",
            "Final Bill": f"₹{self.__calculate_final()}"
        }

    # public method
    def get_customer_view(self):
        return {
            "Customer": self.customer_name,
            "Items": self.items,
            "Final Bill": f"₹{self.__calculate_final()}"
        }


class AdminPortal:
    def show_order(self, order):
        print('ADMIN BILL VIEW')
        return order._get_admin_view()


class CustomerApp:
    def show_order(self, order):
        print('CUSTOMER BILL VIEW')
        return order.get_customer_view()


order = Order("Veera", ["Shoes", "Socks"], 2000, 200)


admin = AdminPortal()


customer = CustomerApp()


print(admin.show_order(order))


print(customer.show_order(order))



#---------------------------------------------------------------------------


class Order:
    def __init__(self, customer_name, total_amount):
        self.customer_name = customer_name
        self.total_amount = total_amount

    def get_bill(self):
        return self.total_amount

order = Order("Veera", 2000)
print(order.get_bill())

class Order:
    def __init__(self, customer_name, total_amount, discount):
        self.customer_name = customer_name
        self.__total_amount = total_amount   # private
        self.__discount = discount           # private

    def get_final_bill(self):   # public method
        return self.__total_amount - self.__discount


order = Order("Veera", 2000, 200)

print(order.customer_name)        # ✅ allowed
print(order.get_final_bill())     # ✅ allowed

# print(order.__total_amount)     # ❌ ERROR


class Order:
    def __init__(self, customer_name, total_amount, discount):
        self.customer_name = customer_name
        self.__total_amount = total_amount
        self.__discount = discount

    def __calculate_final(self):   # private method
        return self.__total_amount - self.__discount

    def get_final_bill(self):      # public method
        return self.__calculate_final()



order = Order("Veera", 2000, 200)

print(order.get_final_bill())      # ✅ works

# order.__calculate_final()        # ❌ ERROR



#__calculate_final  →  _Order__calculate_final

#order.__calculate_final()

class Order:
    def __init__(self, customer_name, items, total_amount, discount):
        self.customer_name = customer_name
        self.items = items
        self.__total_amount = total_amount
        self.__discount = discount

    def __calculate_final(self):
        return self.__total_amount - self.__discount

    def _get_admin_view(self):   # protected
        return {
            "Customer": self.customer_name,
            "Items": self.items,
            "Total": self.__total_amount,
            "Discount": self.__discount,
            "Final": self.__calculate_final()
        }

    def get_customer_view(self):  # public
        return {
            "Customer": self.customer_name,
            "Items": self.items,
            "Final": self.__calculate_final()
        }
order = Order("Veera", ["Shoes", "Socks"], 2000, 200)

print(order._get_admin_view())
print(order.get_customer_view())

