try:
    from .products import Product
    from .store import Store
except ImportError:  # pragma: no cover
    from products import Product
    from store import Store


def show_menu():
    print("   Store Menu")
    print("   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(store: Store):
    for index, product in enumerate(store.get_all_products(), start=1):
        print(f"{index}. {product}")


def run_cli(store: Store):
    while True:
        show_menu()
        choice = input("Please choose a number: ")

        if choice == "1":
            print("------")
            list_products(store)
            print("------")
        elif choice == "2":
            print(f"Total of {store.get_total_quantity()} items in store")
        elif choice == "3":
            print("------")
            list_products(store)
            print("------")
            print("When you want to finish order, enter empty text.")

            shopping_list = []
            while True:
                product_number = input("Which product # do you want? ")
                if product_number == "":
                    break

                amount = input("What amount do you want? ")
                if amount == "":
                    break

                try:
                    product_index = int(product_number) - 1
                    quantity = int(amount)
                    selected_product = store.get_all_products()[product_index]
                    shopping_list.append((selected_product, quantity))
                    print("Product added to list!")
                except (ValueError, IndexError):
                    print("Invalid selection.")

            if shopping_list:
                try:
                    total_cost = store.order(shopping_list)
                    print("********")
                    print(f"Order made! Total payment: ${total_cost:.0f}")
                except ValueError as error:
                    print(f"Could not complete order: {error}")
        elif choice == "4":
            break


def create_store():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    return Store(product_list)


def main():
    best_buy = create_store()
    run_cli(best_buy)


if __name__ == "__main__":
    main()
