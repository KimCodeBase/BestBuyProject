class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError('Invalid input:  Name cannot be empty, and price/quantity cannot be negative.  ')
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        
    def get_quantity(self):
        return self.quantity
    
    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError('Quantity cannot be negative')
        self.quantity = quantity
        if self.quantity == 0:
            self.deactive()
        
    def is_active(self):
        return self.active

    def active(self):
        self.active = True
    
    def deactive(self):
        self.active = False
    
    def show(self):
        return  f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock.")
        self.quantity -= quantity
        total_price = quantity * self.price
        if self.quantity == 0:
            self.deactive()
        return total_price

if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))  
    print(mac.buy(100)) 
    print(mac.is_active()) 

    print(bose.show())  
    print(mac.show()) 

    bose.set_quantity(1000)
    print(bose.show())  
