

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

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()


product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
                ]