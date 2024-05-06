"""
Program: Pickle files working
Lab Work: 4th Lab Work
Title: Working with Files, Classes, Serializers, Regular Expressions, and Standard Libraries
Version: 1
Developer: Kudosh Alexey
Date: 06.05.2024
"""

import pickle

def save_to_pickle(products, filename):
    """
    Saves a list of products to a pickle file.

    Args:
        products (list): List of Product objects to be saved.
        filename (str): Name of the pickle file to save the data.

    Returns:
        None
    """
    with open(filename, 'wb') as file:
        pickle.dump(products, file)


def read_from_pickle(filename):
    """
    Reads product data from a pickle file and returns a list of Product objects.

    Args:
        filename (str): Name of the pickle file to read the data from.

    Returns:
        list: List of Product objects read from the pickle file.
    """
    with open(filename, 'rb') as file:
        products = pickle.load(file)
    return products