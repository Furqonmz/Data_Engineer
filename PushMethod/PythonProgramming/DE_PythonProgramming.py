class Order:
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount

    def calculate_tax(self):
        tax_rate = 0.1
        return self.total_amount * tax_rate

    def display_order(self):
        print(f"ID: {self.order_id} | Nama: {self.customer_name} | Total: {self.total_amount}")

class OrderProcessor:
    def __init__(self):
        self.orders = []

    def add_order(self,order):
        self.orders.append(order)

    def calculate_total_revenue(self):
        total = 0
        for order in self.orders:
            total += order.total_amount
        return total

    def calculate_total_tax(self):
        total_tax = 0
        for order in self.orders:
            total_tax += order.calculate_tax()
        return total_tax


order1 = Order("001", "Furqon", "2026-09-15", 100000)
order2 = Order("002", "Ahmad", "2026-09-16", 2000000)
order3 = Order("003", "Bayu", "2026-09-17", 500000) 

processor = OrderProcessor()

processor.add_order(order1)
processor.add_order(order2)
processor.add_order(order3)

order1.display_order()
order2.display_order()
order3.display_order()

print(f"Total Revenue: {processor.calculate_total_revenue()}")
print(f"Total Tax : {processor.calculate_total_tax()}")