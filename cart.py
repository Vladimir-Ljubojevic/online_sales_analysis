class Cart:
    def __init__(self):
        self.cart_items = []  

    def add_product_to_cart(self, product):
        self.cart_items.append(product)

    def calculate_total(self):
        total = sum(product.price * product.quantity for product in self.cart_items)
        return total

    def display_cart(self):
        if not self.cart_items:
            print("Your cart is empty.")
        else:
            for product in self.cart_items:
                print(f"Product: {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
            print("-" * 20)