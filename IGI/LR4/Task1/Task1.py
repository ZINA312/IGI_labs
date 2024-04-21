from .Product import Product
from .CSVFuncs import *
from .PickleFuncs import *
from Checkers import CheckIntNum
products = [
        Product("Product 1", "Country 1", 100),
        Product("Product 2", "Country 2", 200),
        Product("Product 1", "Country 3", 150),
        Product("Product 3", "Country 1", 300),
    ]

# Функция вывода списка стран и общего объема экспорта для заданного товара
def print_export_summary(products, target_product):
    export_countries = set()
    total_export_quantity = 0
    for product in products:
        if product.name == target_product:
            export_countries.append(product.country)
            total_export_quantity += int(product.quantity)
    print(f"Export countries for {target_product}: {', '.join(export_countries)}")
    print(f"Total export quantity for {target_product}: {total_export_quantity}")

def show_menu():
    print("===== Product Export Program =====")
    print("1. Save products to CSV")
    print("2. Save products to pickle")
    print("3. Read products from CSV")
    print("4. Read products from pickle")
    print("5. Add a product")
    print("6. Export countries and total quantity for a product")
    print("0. Exit")
    print("----------------------------------")

def add_product():
    global products
    name = input("Enter the product name: ")
    country = input("Enter the exporting country: ")
    while True:
        quantity = input("Enter the quantity: ")
        if(CheckIntNum(quantity)):
            break
        print("Wrong input, try again!")
    product = Product(name, country, quantity)
    products.append(product)
    print("Product added successfully!")

def Task1():
    global products
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter the CSV filename to save: ")
            save_to_csv(products, filename)
            print("Products saved to CSV successfully!")
        elif choice == "2":
            filename = input("Enter the pickle filename to save: ")
            save_to_pickle(products, filename)
            print("Products saved to pickle successfully!")
        elif choice == "3":
            filename = input("Enter the CSV filename to read: ")
            products = read_from_csv(filename)
            print("Products read from CSV successfully!")
        elif choice == "4":
            filename = input("Enter the pickle filename to read: ")
            products = read_from_pickle(filename)
            print("Products read from pickle successfully!")
        elif choice == "5":
            add_product(products)
        elif choice == "6":
            target_product = input("Enter the product name: ")
            print_export_summary(products, target_product)
        elif choice == "0":
            print("Exiting the task1...")
            break
        else:
            print("Invalid choice! Please try again.")
