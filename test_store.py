import unittest

try:
    from .products import Product
    from .store import Store
except ImportError:  # pragma: no cover
    from products import Product
    from store import Store


class StoreOrderTests(unittest.TestCase):
    def test_add_product_stores_product(self):
        store = Store([Product("Laptop", price=1000, quantity=5)])
        new_product = Product("Mouse", price=25, quantity=10)

        message = store.add_product(new_product)

        self.assertEqual(message, "Product 'Mouse' added to the store.")
        self.assertIn(new_product, store.products)

    def test_add_product_rejects_non_product(self):
        store = Store([Product("Laptop", price=1000, quantity=5)])
        with self.assertRaises(TypeError):
            store.add_product("not a product")

    def test_remove_product_removes_by_object(self):
        product = Product("Laptop", price=1000, quantity=5)
        store = Store([product])

        message = store.remove_product(product)

        self.assertEqual(message, "Product 'Laptop' removed from the store.")
        self.assertNotIn(product, store.products)

    def test_order_accepts_product_objects_and_returns_total_cost(self):
        product_list = [
            Product("MacBook Air M2", price=1450, quantity=100),
            Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        ]
        store = Store(product_list)

        total_cost = store.order([(store.get_all_products()[0], 1), (store.get_all_products()[1], 2)])

        self.assertEqual(total_cost, 1950.0)
        self.assertEqual(product_list[0].quantity, 99)
        self.assertEqual(product_list[1].quantity, 498)

    def test_order_accepts_product_names_too(self):
        product_list = [Product("Laptop", price=1000, quantity=1)]
        store = Store(product_list)

        total_cost = store.order([("Laptop", 1)])

        self.assertEqual(total_cost, 1000)
        self.assertEqual(product_list[0].quantity, 0)

    def test_order_rejects_inactive_product(self):
        product = Product("Laptop", price=1000, quantity=3)
        product.deactivate()
        store = Store([product])

        with self.assertRaises(ValueError) as context:
            store.order([(product, 1)])

        self.assertIn("not active", str(context.exception))

    def test_order_raises_when_product_not_found(self):
        store = Store([Product("Laptop", price=1000, quantity=3)])

        with self.assertRaises(ValueError) as context:
            store.order([("Tablet", 1)])

        self.assertIn("not found in the store", str(context.exception))

    def test_get_all_products_filters_inactive(self):
        active = Product("Laptop", price=1200, quantity=1)
        inactive = Product("Mouse", price=20, quantity=0, active=False)
        store = Store([active, inactive])

        active_products = store.get_all_products()
        self.assertEqual(len(active_products), 1)
        self.assertEqual(active_products[0].name, "Laptop")

    def test_get_total_quantity_uses_all_products(self):
        store = Store([Product("Laptop", price=1200, quantity=2), Product("Mouse", price=20, quantity=0)])

        self.assertEqual(store.get_total_quantity(), 2)


if __name__ == "__main__":
    unittest.main()
