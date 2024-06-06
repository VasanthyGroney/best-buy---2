class Promotion:
    def __init__(self, name):
        self.name = name
    def apply_promotion(self, product, quantity):
        pass

class PercentageDiscount(Promotion):
    def __init__(self, name, percentage):
        super().__init__(name)
        self.percentage = percentage

    def apply_promotion(self, product, quantity):
        return (product.price * quantity ) / 100 * self.percentage


class SecondItemHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity < 2:
            return product.price * quantity
        else:
            full_price_items = quantity // 2 + quantity % 2
            half_price_items = quantity // 2
            total_price = (full_price_items * product.price) + (half_price_items * product.price * 0.5)
            return total_price


class Buy2Get1Free(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        # For every set of 3 items, 1 is free
        free_items = quantity // 3
        payable_items = quantity - free_items
        total_price = payable_items * product.price
        return total_price

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

