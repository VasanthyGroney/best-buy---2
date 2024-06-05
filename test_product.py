import pytest
from products import Product


class Product:
    def __init__(self, name, price, quantity):
        self.validate_product_details(name, price)
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

    @staticmethod
    def validate_product_details(name, price):
        if not name:
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Product price cannot be negative")

    def is_active(self):
        return self.active

    def buy(self, amount):
        if amount > self.quantity:
            raise ValueError("Cannot purchase more than available quantity")
        total_price = self.price * amount
        self.quantity -= amount
        if self.quantity == 0:
            self.active = False
        return total_price, self.quantity
