"""
Program: Products class
Lab Work: 4th Lab Work
Title: Working with Files, Classes, Serializers, Regular Expressions, and Standard Libraries
Version: 1
Developer: Kudosh Alexey
Date: 06.05.2024
"""

from .Product import Product
from Checkers import CheckIntNum

class Products:
    """
    Represents a collection of products.
    """

    def __init__(self, products: list):
        """
        Initializes a new instance of the Products class.

        Args:
            products (list): List of Product objects.

        Returns:
            None
        """
        self._products = products

    def get_products(self):
        """
        Gets the list of products.

        Returns:
            list: List of Product objects.
        """
        return self._products
    
    def set_products(self, products: list):
        """
        Sets the list of products.

        Args:
            products (list): List of Product objects.

        Returns:
            None
        """
        self._products = products

    def print_export_summary(self, target_product):
        """
        Prints the export summary for a specific product.

        Args:
            target_product (str): The name of the product.

        Returns:
            None
        """
        export_countries = set()
        total_export_quantity = 0
        for product in self._products:
            if product.name == target_product:
                export_countries.add(product.country)
                total_export_quantity += int(product.quantity)
        print(f"Export countries for {target_product}: {', '.join(export_countries)}")
        print(f"Total export quantity for {target_product}: {total_export_quantity}")

    def sort(self):
        """
        Sorts the list of products by name.

        Returns:
            None
        """
        self._products = sorted(self._products, key=lambda x: x.name)
        print(f'Sorted list: {", ".join([product.name for product in self._products])}')

    def add_product(self):
        """
        Adds a new product to the list.

        Returns:
            None
        """
        name = input("Enter the product name: ")
        country = input("Enter the exporting country: ")
        while True:
            quantity = input("Enter the quantity: ")
            if CheckIntNum(quantity):
                break
            print("Wrong input, try again!")
        product = Product(name, country, quantity)
        self._products.append(product)
        print(str(product))

    def find_product(self, name: str) -> list:
        """
        Finds products with a given name.

        Args:
            name (str): The name of the product to search for.

        Returns:
            list: List of Product objects matching the provided name.
        """
        res = []
        for prod in self._products:
            if prod.name == name:
                res.append(prod)
        return res
        
    products = property(get_products, set_products)