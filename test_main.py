import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

try:
    from .main import run_cli
    from .products import Product
    from .store import Store
except ImportError:  # pragma: no cover
    from main import run_cli
    from products import Product
    from store import Store


class StoreAndProductRegressionTests(unittest.TestCase):
    def setUp(self):
        self.product = Product("Laptop", price=1200, quantity=2)
        self.store = Store([self.product])

    def test_set_quantity_allows_zero_and_deactivates(self):
        self.product.set_quantity(0)
        self.assertFalse(self.product.is_active())
        self.assertEqual(self.product.get_quantity(), 0)

    def test_set_quantity_rejects_negative(self):
        with self.assertRaises(ValueError):
            self.product.set_quantity(-1)

    def test_set_quantity_raises_when_product_reactivated_with_positive_value(self):
        self.product.set_quantity(0)
        self.assertFalse(self.product.is_active())

        self.product.set_quantity(3)
        self.assertTrue(self.product.is_active())
        self.assertEqual(self.product.get_quantity(), 3)

    def test_activate_and_get_quantity_are_available(self):
        self.product.set_quantity(0)
        self.product.activate()
        self.assertTrue(self.product.is_active())
        self.assertEqual(self.product.get_quantity(), 0)

    def test_buy_rejects_inactive_product(self):
        self.product.deactivate()
        with self.assertRaises(ValueError) as error:
            self.product.buy(1)
        self.assertIn("not active", str(error.exception))

    def test_buy_reaches_zero_and_deactivates(self):
        self.product.set_quantity(2)
        total = self.product.buy(2)
        self.assertEqual(total, 2400)
        self.assertEqual(self.product.get_quantity(), 0)
        self.assertFalse(self.product.is_active())

    def test_add_product_adds_object(self):
        new_product = Product("Mouse", price=50, quantity=10)
        message = self.store.add_product(new_product)
        self.assertIn("added to the store", message)
        self.assertIn(new_product, self.store.products)
        self.assertEqual(self.store.get_all_products()[-1], new_product)

    def test_remove_product_accepts_product_object(self):
        self.store.remove_product(self.product)
        self.assertNotIn(self.product, self.store.products)

    def test_remove_product_still_works_for_name_as_additional_feature(self):
        removed_msg = self.store.remove_product("Laptop")
        self.assertIn("removed from the store", removed_msg)
        self.assertEqual(len(self.store.products), 0)

    def test_cli_output_shows_menu_and_totals(self):
        output = io.StringIO()
        with patch("builtins.input", side_effect=["1", "2", "4"]):
            with redirect_stdout(output):
                run_cli(self.store)
        printed = output.getvalue()
        self.assertIn("Store Menu", printed)
        self.assertIn("Laptop", printed)
        self.assertIn("Total of 2 items in store", printed)


if __name__ == "__main__":
    unittest.main()
