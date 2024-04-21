import csv
from .Product import Product

def save_to_csv(products, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Country', 'Quantity'])
        for product in products:
            writer.writerow([product.name, product.country, product.quantity])


def read_from_csv(filename):
    products = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name, country, quantity = row
            product = Product(name, country, quantity)
            products.append(product)
    return products