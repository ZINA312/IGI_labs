"""
Program: Task 1
Lab Work: 4th Lab Work
Title: Working with Files, Classes, Serializers, Regular Expressions, and Standard Libraries
Version: 1
Developer: Kudosh Alexey
Date: 06.05.2024
"""

from .Product import Product
from .Products import Products
from .CSVFuncs import *
from .PickleFuncs import *
import os

productsList = [
        Product("Product 1", "Country 1", 100),
        Product("Product 2", "Country 2", 200),
        Product("Product 1", "Country 3", 150),
        Product("Product 3", "Country 1", 300),
    ]

def show_menu():
    """
    Displays the menu options for the program.
    """
    print("===== Product Export Program =====")
    print("1. Save products to CSV")
    print("2. Save products to pickle")
    print("3. Read products from CSV")
    print("4. Read products from pickle")
    print("5. Add a product")
    print("6. Export countries and total quantity for a product")
    print("7. Sort list")
    print("8. Find product")
    print("0. Exit")
    print("----------------------------------")

def Task1():
    """
    Main function that handles user input and performs actions based on the chosen menu option.
    """
    products = Products(productsList)
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        os.system('cls')
        if choice == "1":
            filename = input("Enter the CSV filename to save: ")
            save_to_csv(products.get_products(), filename)
            print("Products saved to CSV successfully!")
        elif choice == "2":
            filename = input("Enter the pickle filename to save: ")
            save_to_pickle(products.get_products(), filename)
            print("Products saved to pickle successfully!")
        elif choice == "3":
            filename = input("Enter the CSV filename to read: ")
            products.set_products = read_from_csv(filename)
            print("Products read from CSV successfully!")
        elif choice == "4":
            filename = input("Enter the pickle filename to read: ")
            products = read_from_pickle(filename)
            print("Products read from pickle successfully!")
        elif choice == "5":
            products.add_product()
        elif choice == "6":
            target_product = input("Enter the product name: ")
            products.print_export_summary(target_product)
        elif choice == "7":
            products.sort()
        elif choice == "8":
            target_product = input("Enter the product name: ")
            resProd = products.find_product(target_product)
            if(resProd == []):
                print("Product not found!")
            else:
                print('\n'.join(map(str, resProd)))
        elif choice == "0":
            print("Exiting the task1...")
            break
        else:
            print("Invalid choice! Please try again.")