class Promotion:
    def __init__(self, name):
        self.name = name  

    def apply_promotion(self, product, quantity):
        raise NotImplementedError("Subclasses must implement this method")

class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount = (self.percent / 100) * product.price
        return (product.price - discount) * quantity

class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_quantity = quantity // 2 + quantity % 2
        half_price_quantity = quantity // 2
        return (full_price_quantity * product.price) + (half_price_quantity * product.price * 0.5)
    
class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_quantity = (2 * (quantity // 3)) + (quantity % 3)
        return full_price_quantity * product.price
