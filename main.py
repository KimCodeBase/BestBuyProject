from products import Product
from store import Store

product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = Store(product_list)

def start(store):
    while True:
        print("\nWelcome to Best Buy!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            products = store.get_all_products()
            for product in products:
                print(product.show())
                
        elif choice == '2':
            total_quantity = store.get_total_quantity()
            print(f"Total amount in store: {total_quantity}")
            
        elif choice == '3':
            shopping_list = []
            products = store.get_all_products()
            for i, product in enumerate(products):
                print(f"{i+1}. {product.name} (Available: {product.get_quantity()})")
            while True:
                product_choice = input("Enter product number (or 'done' to finish): ")
                if product_choice.lower() == 'done':
                    break
                try:
                    product_index = int(product_choice) - 1
                    if product_index < 0 or product_index >= len(products):
                        print("Invalid product number. Please try again.")
                        continue
                    quantity = int(input(f"Enter quantity for {products[product_index].name}: "))
                    shopping_list.append((products[product_index], quantity))
                    print("Product added to list!")
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
            
            if shopping_list:
                try:
                    total_price = store.order(shopping_list)
                    print(f"Order placed successfully! Total price: ${total_price}")
                except Exception as e:
                    print(f"Error placing order: {e}")
            else:
                print("No items ordered.")
        
        elif choice == '4':
            print("Thank you for visiting Best Buy!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    start(best_buy)
