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
    
    
def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))
    
if __name__ == "__main__":
    main()