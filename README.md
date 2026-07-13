# best_buy

`best_buy` is a small Python CLI project that simulates a simple store with an inventory model and ordering workflow.  
It separates business logic from presentation logic so the core models are easier to test and maintain.

## What this project contains

The project is intentionally small but includes all core parts of a basic application:

- a `Product` model for stock items
- a `Store` model with ordering and inventory operations
- a CLI entry point for interactive usage
- automated tests for business logic and regressions

## Project structure

- `products.py`
  - Contains the `Product` class
  - Validates/updates quantity and activation state
  - Supports:
    - `get_quantity()`
    - `set_quantity()`
    - `is_active()`
    - `activate()`
    - `deactivate()`
    - `buy()`
  - String representation is implemented in `__str__()`, which is used by `display_info()` and `show()`.

- `store.py`
  - Contains the `Store` class
  - Supports:
    - `add_product(product: Product)` (required)
    - `remove_product(product: Product)` (required interface)
    - `get_all_products()` (filters only active products)
    - `get_total_quantity()`
    - `order(shopping_list)`
  - Keeps core behavior separate from CLI input/output.

- `main.py`
  - Interactive text CLI
  - Implements presentation methods:
    - `show_menu()`
    - `list_products(store)`
    - `run_cli(store)`
  - Also contains `create_store()` and `main()` to bootstrap default data.

- `test_store.py`
  - Tests all store-related behavior (adding/removing products, ordering, validations).
- `test_main.py`
  - Tests product and regression behavior for earlier identified edge cases (quantity changes, activation, buy behavior, CLI output).

## Business logic details

- Active filtering:
  - `Store.get_all_products()` returns only active products.
  - Inactive products are ignored in listing and cannot be ordered.
- Quantity and activation rules:
  - `Product.set_quantity(0)` is allowed and deactivates the product.
  - `set_quantity` rejects negative values.
  - Setting a positive quantity reactivates product availability.
  - Buying from a product uses current stock and updates state.
  - If stock reaches 0 after buying, the product is automatically deactivated by quantity logic.
- Ordering:
  - `Store.order()` supports shopping-list entries either by `Product` instance or by product name.
  - It raises `ValueError` for:
    - unknown product,
    - inactive product,
    - invalid quantities.

## Run the app

Run from the project directory:

```bash
python main.py
```

You can also import and call `create_store()` and `run_cli()` from `main.py` if you want to integrate it in another script.

## Run tests

From `Codio/Term_3/best_buy`:

```bash
python -m unittest Term_3.best_buy.test_main.StoreAndProductRegressionTests --quiet
python -m unittest Term_3.best_buy.test_store.StoreOrderTests --quiet
```

or run both test modules directly with pytest:

```bash
python -m pytest -q
```

## Example CLI flow

1. Start the app.
2. Select `1` to list all active products.
3. Select `2` to show the total stock across all stored products.
4. Select `3` to place an order:
   - choose a product number,
   - enter amount,
   - repeat until you submit empty input,
   - receive order total.
5. Select `4` to quit.

## Notes for maintainers

- `products.py`, `store.py` contain only core behavior and validation.
- `main.py` is the presentation layer and should stay focused on CLI flow.
- Tests rely on stable behavior from both models and do not need network or external services.
