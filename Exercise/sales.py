sales = [
    {
        "id": "TRX001",
        "product": "Laptop",
        "category": "Electronics",
        "quantity": 2,
        "price": 7000000
    },
    {
        "id": "TRX002",
        "product": "Mouse",
        "category": "Electronics",
        "quantity": 5,
        "price": 250000
    },
    {
        "id": "TRX003",
        "product": "Chair",
        "category": "Furniture",
        "quantity": 3,
        "price": 1500000
    },
    {
        "id": "TRX004",
        "product": "Desk",
        "category": "Furniture",
        "quantity": 2,
        "price": 2500000
    }
]

class Sale:
    def __init__(self, id, product, category, quantity, price):
        self.id = id
        self.product = product
        self.category = category
        self.quantity = quantity
        self.price = price
    def calculate_total(self):
        return self.quantity * self.price
        
    def display_sale(self):
        print(f"ID: {self.id} | Product: {self.product} | Total: Rp{self.calculate_total():,}".replace(",","."))

class SalesProcessor:
    def __init__(self):
        self.sales = []
    def add_sale(self, sale):
        self.sales.append(sale)
    def calculate_total_revenue(self):
        total = 0
        for sale in self.sales:
            total += sale.calculate_total()
        return total
    def count_transaction(self):
        return len(self.sales)

processor = SalesProcessor()
for sale in sales:
    sales_object = Sale(**sale)
    sales_object.display_sale()
    processor.add_sale(sales_object)

print(f"Total Revenue: Rp{processor.calculate_total_revenue():,}".replace(",","."))
print(f"Total Transaction: {processor.count_transaction()}")
