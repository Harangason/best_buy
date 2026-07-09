from products import Product


class Store:

    def __init__(self, products):
        self.products = products

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return f"Product '{product_name}' removed from the store."
        return f"Product '{product_name}' not found in the store."
    
    def get_total_quantity(self) -> int:
        total_quantity = sum(product.quantity for product in self.products)
        return total_quantity
    
    def get_all_products(self) -> list[Product]:
        return [product for product in self.products if product.is_active()]
    
    def order(self, shopping_list) -> float:
        total_cost = 0.0
        for item in shopping_list:
            product_or_name, quantity = item
            product_name = product_or_name.name if isinstance(product_or_name, Product) else product_or_name

            if isinstance(product_or_name, Product):
                product = next((p for p in self.products if p is product_or_name), None)
            else:
                product = next((p for p in self.products if p.name == product_or_name), None)

            if product is None:
                raise ValueError(f"Product '{product_name}' not found in the store.")
            if not product.is_active():
                raise ValueError(f"Product '{product_name}' is not active.")
            total_cost += product.buy(quantity)
        return total_cost

    def list_products(self):
        for index, product in enumerate(self.get_all_products(), start=1):
            print(f"{index}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")

    def show_menu(self):
        print("   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

    def run_cli(self):
        while True:
            self.show_menu()
            choice = input("Please choose a number: ")

            if choice == "1":
                print("------")
                self.list_products()
                print("------")
            elif choice == "2":
                print(f"Total of {self.get_total_quantity()} items in store")
            elif choice == "3":
                print("------")
                self.list_products()
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
                        selected_product = self.get_all_products()[product_index]
                        shopping_list.append((selected_product, quantity))
                        print("Product added to list!")
                    except (ValueError, IndexError):
                        print("Invalid selection.")

                total_cost = self.order(shopping_list)
                print("********")
                print(f"Order made! Total payment: ${total_cost:.0f}")
            elif choice == "4":
                break


def main():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    best_buy.run_cli()


if __name__ == "__main__":
    main()