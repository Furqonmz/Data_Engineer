class Order:
  def __init__(self, order_id, customer_name, order_date, total_amount):
    self.order_id = order_id
    self.customer_name = customer_name
    self.order_date = order_date
    self.total_amount = total_amount
  def calculate_tax(self):
    tax_rate =  0.1
    return self.total_amount * tax_rate
  def display_order(self):
    print(f"ID: {self.order_id} | Nama: {self.customer_name} | Total: {self.total_amount}")

class OrderProcessor:
  def __init__(self):
    self.order = []
  def add_order(self, order):
    self.order.append(order)
  def calculate_total_revenue(self):
    total = 0
    for order in self.order:
      total += order.total_amount
    return total
  def calculate_total_tax(self):
    total_tax = 0
    for order in self.order:
      total_tax += order.calculate_tax()
    return total_tax

pesanan1 = Order("001", "Budi", "2024-01-01", 100000)
pesanan2 = Order("002", "Ana", "2024-01-01", 290987)
pesanan3 = Order("003", "Ana", "2024-02-03", 350000)
prosesor = OrderProcessor()
prosesor.add_order(pesanan1)
prosesor.add_order(pesanan2)
prosesor.add_order(pesanan3)
pesanan1.display_order()
pesanan2.display_order()
pesanan3.display_order()
print(f"Total Revenue: Rp. {prosesor.calculate_total_revenue()}")
print(f"Total pajak: Rp. {prosesor.calculate_total_tax()}")