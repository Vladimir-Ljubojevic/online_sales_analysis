from product_manager import ProductManager
from product import Product

manager = ProductManager()

product1 = Product("Laptop", 1000, 5)
product2 = Product("Smartphone", 700, 10)
product3 = Product("Headphones", 150, 15)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

manager.remove_product_by_name("Laptop")

manager.display_all_products()

manager.total_inventory_value()
