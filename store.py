from products import Product

class Store:
    def __init__(self, products):
        self.products = products
    
    def add_product(self, product):
        self.products.append(product)
        
    def remove_product(self, product):
        self.products.remove(product) 
    
    def get_total_quantity(self):
        total_quantity = 0  
        for product in self.products:
            total_quantity += product.quantity 
        return total_quantity 
        
    def get_all_products(self):
        active_products = []
        for product in self.products: 
            if product.is_active():
                active_products.append(product)
        return active_products
        
    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price

    def __contains__(self, product):
        return product in self.products

    def __add__(self, other):
        combined_products = self.products + other.products
        return Store(combined_products)

    def __str__(self):
        return '\n'.join(str(product) for product in self.products)

if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    store = Store(product_list)
    products = store.get_all_products()
    
    print(store.get_total_quantity()) 

    order_cost = store.order([(products[0], 1), (products[1], 2)])  
    print(f"Order cost: {order_cost} dollars.")
