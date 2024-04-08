import csv
import pickle

class Product:
    def __init__(self, name, country, importer, quantity):
        self.name = name
        self.country = country
        self.importer = importer
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Country: {self.country}, Importer: {self.importer}, Quantity: {self.quantity}"
    
class CSVSerializer:
    @staticmethod
    def serialize(data, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Country", "Importer", "Quantity"])
            for product in data:
                writer.writerow([product.name, product.country, product.importer, product.quantity])

    @staticmethod
    def deserialize(filename):
        data = []
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                name, country, importer, quantity = row
                product = Product(name, country, importer, quantity)
                data.append(product)
        return data

class PickleSerializer:
    @staticmethod
    def serialize(data, filename):
        with open(filename, "wb") as file:
            pickle.dump(data, file)

    @staticmethod
    def deserialize(filename):
        with open(filename, "rb") as file:
            data = pickle.load(file)
        return data