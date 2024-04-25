class Product:
    def __init__(self, name, country, quantity):
        self._name = name
        self._country = country
        self._quantity = quantity

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def get_country(self):
        return self._country
    
    def set_country(self, country):
        self._country = country

    def get_quantity(self):
        return self._quantity
    
    def set_quantity(self, quantity):
        self._quantity = quantity

    def __str__(self):
        return f"Product: {self._name}, Country: {self._country}, Quantity: {self._quantity}"
    
    name = property(get_name, set_name)
    country = property(get_country, set_country)
    quantity = property(get_quantity, set_quantity)