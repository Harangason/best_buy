import unittest

from products import Product
from store import Store


class StoreOrderTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
