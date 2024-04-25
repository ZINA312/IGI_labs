from .Product import Product
from Checkers import CheckIntNum
 

class Products:

    def __init__(self, products : list):
        self._products = products

    def get_products(self):
        return self._products
    
    def set_products(self, products : list):
        self._products = products

    def print_export_summary(self, target_product):
        export_countries = set()
        total_export_quantity = 0
        for product in self._products:
            if product.name == target_product:
                export_countries.add(product.country)
                total_export_quantity += int(product.quantity)
        print(f"Export countries for {target_product}: {', '.join(export_countries)}")
        print(f"Total export quantity for {target_product}: {total_export_quantity}")

    def sort(self):
        self._products = sorted(self._products, key = lambda x: x.name)
        print(f'Sorted list: {", ".join([product.name for product in self._products])}')

    def add_product(self):
        name = input("Enter the product name: ")
        country = input("Enter the exporting country: ")
        while True:
            quantity = input("Enter the quantity: ")
            if(CheckIntNum(quantity)):
                break
            print("Wrong input, try again!")
        product = Product(name, country, quantity)
        self._products.append(product)
        print(str(product))

    def find_product(self, name : str) -> list:
        res = list()
        for prod in self._products:
            if prod.name == name:
                res.append(prod)
        return res
        
    products = property(get_products, set_products)