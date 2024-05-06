"""
Program: CSV files working
Lab Work: 4th Lab Work
Title: Working with Files, Classes, Serializers, Regular Expressions, and Standard Libraries
Version: 1
Developer: Kudosh Alexey
Date: 06.05.2024
"""

import csv
from .Product import Product

def save_to_csv(products, filename):
    """
    Saves a list of products to a CSV file.

    Args:
        products (list): List of Product objects to be saved.
        filename (str): Name of the CSV file to save the data.

    Returns:
        None
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Country', 'Quantity'])
        for product in products:
            writer.writerow([product.name, product.country, product.quantity])


def read_from_csv(filename):
    """
    Reads product data from a CSV file and returns a list of Product objects.

    Args:
        filename (str): Name of the CSV file to read the data from.

    Returns:
        list: List of Product objects read from the CSV file.
    """
    products = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            name, country, quantity = row
            product = Product(name, country, quantity)
            products.append(product)
    return products