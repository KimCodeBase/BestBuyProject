class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError('Invalid input: Name cannot be empty, and price/quantity cannot be negative.')
        self.name = name
        self.price = price
        self._quantity = quantity  
        self.active = True
        self._promotion = None      
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError('Quantity cannot be negative')
        self._quantity = value
        if self._quantity == 0:
            self.deactivate()
    
    @property
    def promotion(self):
        return self._promotion
    
    @promotion.setter
    def promotion(self, value):
        self._promotion = value
        
    def is_active(self):
        return self.active

    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    def __str__(self):
        promo_desc = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo_desc}"

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def buy(self, quantity):
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock.")
        
        self.quantity -= quantity
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self.price
        
        if self.quantity == 0:
            self.deactivate()
        return total_price

class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self._quantity = 0  
    
    @property
    def quantity(self):
        return 0
    
    @quantity.setter
    def quantity(self, value):
        raise ValueError("Cannot change quantity of a non-stocked product.")
    
    def __str__(self):
        promo_desc = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name} (Non-Stocked), Price: {self.price}{promo_desc}"

class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum
    
    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} of this product.")
        return super().buy(quantity)
    
    def __str__(self):
        promo_desc = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name} (Limited, Max: {self.maximum}), Price: {self.price}, Quantity: {self.quantity}{promo_desc}"
