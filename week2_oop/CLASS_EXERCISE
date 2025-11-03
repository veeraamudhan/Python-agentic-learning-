class Order:
    def __init__(self, customer_name, items, total_amount, discount):
        self.customer_name = customer_name   # public
        self.items = items                   # public
        self.__total_amount = total_amount   # private
        self.__discount = discount           # private

    def __calculate_final(self):
        return self.__total_amount - self.__discount

    def _get_admin_view(self):
        return {
        "Customer": self.customer_name,
        "Items": self.items,
        "Total Amount": f"₹{self.__total_amount}",
        "Discount Applied": f"₹{self.__discount}",
        "Final Bill": f"₹{self.__calculate_final()}"
    }
    def get_customer_view(self):
        return {
        "Customer": self.customer_name,
        "Items": self.items,
        "Final Bill": f"₹{self.__calculate_final()}"
    }
class AdminPortal:
    def show_order(self, order):
        return order._get_admin_view()
class CustomerApp:
    def show_order(self, order):
        return order.get_customer_view()
order = Order("Veera", ["Shoes", "Socks"], 2000, 200)

admin = AdminPortal()
customer = CustomerApp()

print(order.customer_name)
print(order.items)
print(admin.show_order(order))
# {'Customer': 'Veera', 'Items': ['Shoes', 'Socks'],
#  'Total Amount': '₹2000', 'Discount Applied': '₹200',
#  'Final Bill': '₹1800'}

print(customer.show_order(order))
# {'Customer': 'Veera', 'Items': ['Shoes', 'Socks'],
#  'Final Bill': '₹1800'}

