class Product:
    def __init__(self, name, country, quantity):
        self.name = name
        self.country = country
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Country: {self.country}, Quantity: {self.quantity}"