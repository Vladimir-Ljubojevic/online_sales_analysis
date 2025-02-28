from product_manager import ProductManager
from product import Product

manager = ProductManager()

product1 = Product("Monitor", 100, 50)
product2 = Product("Phone", 70, 105)
product3 = Product("Mouse", 120, 30)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

manager.remove_product_by_name("Laptop")


