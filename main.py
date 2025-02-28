from product_manager import ProductManager
from product import Product
from cart import Cart


manager = ProductManager()


product1 = Product("Monitor", 100, 50)
product2 = Product("Phone", 70, 105)
product3 = Product("Mouse", 120, 30)
product4 = Product("Tablet", 400, 8)
product5 = Product("Smartwatch", 250, 20)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.add_product(product4)
manager.add_product(product5)

cart = Cart()


manager.remove_product_by_name("Phone")

manager.display_all_products()

manager.total_inventory_value()
