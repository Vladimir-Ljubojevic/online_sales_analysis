class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product_info(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print("-" * 20)

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity