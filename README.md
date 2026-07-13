# best_buy

A small Python store simulator with a `Product` model, a `Store` class, and a text-based CLI for browsing products and placing orders.

## Features

- List all active products in the store
- Show the total number of items in stock
- Create an order by selecting products from the CLI menu
- Reduce inventory automatically when products are purchased
- Run automated tests with `pytest`

## Project Structure

- `products.py` - Product model and inventory-related behavior
- `store.py` - Store business logic (no user interaction)
- `main.py` - Interactive CLI (menu, listing, ordering flow)
- `test_store.py` - Unit tests for the store workflow
- `_static/` - Static HTML/CSS assets used by the project

## Run The App

Start the CLI with:

```bash
python main.py
```

## Run Tests

Run the test suite with:

```bash
python -m pytest -q
```

## Notes

- The CLI shows only active products.
- Orders are placed by selecting a product number and quantity.
- The final order total is printed after checkout.
