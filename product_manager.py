from product import Product

class ProductManager:
    def __init__(self):
        self.products = []  # Lista svih proizvoda

    def add_product(self, product):
        """Dodaje proizvod u listu"""
        self.products.append(product)

    def display_all_products(self):
        """Prikazuje sve proizvode u listi"""
        if not self.products:
            print("No products available.")
        for product in self.products:
            product.display_product_info()  # Ispravljeno ime metode

    def total_inventory_value(self):
        """Prikazuje ukupnu vrednost svih proizvoda"""
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Total inventory value: ${total_value:.2f}")