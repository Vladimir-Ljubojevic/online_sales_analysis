from product import Product

class ProductManager:
    def __init__(self):
        self.products = []  

    def add_product(self, product):
        self.products.append(product)

    def display_all_products(self):
        if not self.products:
            print("No products available.")
        for product in self.products:
            product.display_product_info()  

    def total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Total inventory value: ${total_value:.2f}")
        
    def remove_product_by_name(self, product_name):
        product_to_remove = next((product for product in self.products if product.name == product_name), None)
        
        if product_to_remove:
            self.products.remove(product_to_remove)
            print(f"Product '{product_name}' has been removed.")
        else:
            print(f"Product '{product_name}' not found.")