from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree
from store import Store

def main():
    """
    Main function to run the Best Buy store application.
    """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    second_half_price = SecondHalfPrice("Second Half Price")
    third_one_free = ThirdOneFree("Third One Free")
    thirty_percent = PercentDiscount("30% off", percent=30)

    product_list[0].promotion = second_half_price
    product_list[1].promotion = third_one_free
    product_list[3].promotion = thirty_percent

    best_buy = Store(product_list)

    while True:
        print("\nWelcome to Best Buy!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            products = best_buy.get_all_products()
            for product in products:
                print(product)
                
        elif choice == '2':
            total_quantity = best_buy.get_total_quantity()
            print(f"Total amount in store: {total_quantity}")
            
        elif choice == '3':
            shopping_list = []
            products = best_buy.get_all_products()
            for i, product in enumerate(products):
                print(f"{i+1}. {product.name} (Available: {product.quantity})")
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
                    total_price = best_buy.order(shopping_list)
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
    main()
