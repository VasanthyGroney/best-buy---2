from store import Store
from products import Product, NonStockedProduct, LimitedProduct

def start(store):
    while True:
        print("\nStore Menu")
        print("==========")
        print("1. List all products in store")
        print("2. Show total quantity in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice.isdigit():
            choice = int(choice)
        else:
            print("Invalid choice! Please enter a number.")
            continue

        if choice == 1:
            products = store.get_all_products()
            for product in products:
                product.show()
        elif choice == 2:
            total_quantity = store.get_total_quantity()
            print(f"Total quantity in store: {total_quantity}")
        elif choice == 3:
            print("------")
            products = store.get_all_products()
            for index, product in enumerate(products, start=1):
                print(f"{index}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
            print("------")
            print("When you want to finish order, enter empty text.")

            shopping_list = []
            while True:
                product_choice = input("Which product # do you want? ")
                if product_choice == "":
                    break
                if not product_choice.isdigit() or int(product_choice) < 1 or \
                   int(product_choice) > len(products):
                    print("Invalid choice, please enter a valid product number.")
                    continue
                product_index = int(product_choice) - 1
                product = store.products[product_index]
                quantity = int(input(f"What amount do you want? "))
                shopping_list.append((product, quantity))
                print("Product added to list!")

            total_price = store.order(shopping_list)
            print(f"Total price for the order: ${total_price:.2f}")
        elif choice == 4:
            print("Quitting the program.")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    # setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]
    best_buy = Store(product_list)
    start(best_buy)
