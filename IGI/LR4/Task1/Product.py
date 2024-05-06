"""
Program: Product class
Lab Work: 4th Lab Work
Title: Working with Files, Classes, Serializers, Regular Expressions, and Standard Libraries
Version: 1
Developer: Kudosh Alexey
Date: 06.05.2024
"""

class Product:
    """
    Represents a product with its name, country, and quantity.
    """
    default_quantity = 0
    def __init__(self, name, country, quantity):
        """
        Initializes a new instance of the Product class.

        Args:
            name (str): The name of the product.
            country (str): The country of origin for the product.
            quantity (int): The quantity of the product.

        Returns:
            None
        """
        self._name = name
        self._country = country
        self._quantity = quantity

    def get_name(self):
        """
        Gets the name of the product.

        Returns:
            str: The name of the product.
        """
        return self._name
    
    def set_name(self, name):
        """
        Sets the name of the product.

        Args:
            name (str): The name of the product.

        Returns:
            None
        """
        self._name = name

    def get_country(self):
        """
        Gets the country of origin for the product.

        Returns:
            str: The country of origin for the product.
        """
        return self._country
    
    def set_country(self, country):
        """
        Sets the country of origin for the product.

        Args:
            country (str): The country of origin for the product.

        Returns:
            None
        """
        self._country = country

    def get_quantity(self):
        """
        Gets the quantity of the product.

        Returns:
            int: The quantity of the product.
        """
        return self._quantity
    
    def set_quantity(self, quantity):
        """
        Sets the quantity of the product.

        Args:
            quantity (int): The quantity of the product.

        Returns:
            None
        """
        self._quantity = quantity

    def __str__(self):
        """
        Returns a string representation of the product.

        Returns:
            str: A string representation of the product.
        """
        return f"Product: {self._name}, Country: {self._country}, Quantity: {self._quantity}"
    
    name = property(get_name, set_name)
    country = property(get_country, set_country)
    quantity = property(get_quantity, set_quantity)