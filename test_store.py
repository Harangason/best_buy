import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

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

    def test_cli_lists_products_and_shows_total_amount(self):
        store = Store([
            Product("MacBook Air M2", price=1450, quantity=100),
            Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            Product("Google Pixel 7", price=500, quantity=250),
        ])

        output = io.StringIO()
        with patch("builtins.input", side_effect=["1", "4"]):
            with redirect_stdout(output):
                store.run_cli()

        printed_output = output.getvalue()
        self.assertIn("Store Menu", printed_output)
        self.assertIn("MacBook Air M2", printed_output)
        self.assertIn("Total of 850 items in store", printed_output)


if __name__ == "__main__":
    unittest.main()
