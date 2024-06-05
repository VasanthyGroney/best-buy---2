class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, amount):
        if amount > self.quantity:
            return "Not enough stock available"
        else:
            self.quantity -= amount
            return f"{amount} units of {self.name} bought. {self.quantity} remaining."

    def is_active(self):
        return self.quantity > 0

    def show(self):
        print(f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def set_quantity(self, quantity):
        self.quantity = quantity

class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def buy(self, amount):
        return f"{amount} units of {self.name} bought. Unlimited quantity available."

    def is_active(self):
        return True

    def set_quantity(self, quantity):
        pass  # Do nothing, quantity should always stay zero

    def show(self):
        print(f"Product: {self.name}, Price: ${self.price}, Quantity: Unlimited")

class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, amount):
        if amount > self.maximum:
            return f"Cannot buy more than {self.maximum} units of {self.name} at a time."
        return super().buy(amount)
