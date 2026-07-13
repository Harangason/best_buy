try:
    from .products import Product
except ImportError:  # pragma: no cover
    from products import Product


class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added.")
        self.products.append(product)
        return f"Product '{product.name}' added to the store."

    def remove_product(self, product: Product) -> str:
        if isinstance(product, str):
            product = next((p for p in self.products if p.name == product), None)

        if product in self.products:
            self.products.remove(product)
            return f"Product '{product.name}' removed from the store."
        return f"Product '{getattr(product, 'name', product)}' not found in the store."

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

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
