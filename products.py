class Product:
    def __init__(self, name, price, quantity, active=True):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active

    def __str__(self):
        return (
            f"Product Name: {self.name}, Price: ${self.price:.2f}, "
            f"Quantity: {self.quantity}, Active: {self.active}"
        )

    def display_info(self):
        return str(self)

    def show(self):
        return str(self)

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        self.active = quantity > 0

    def activate(self):
        self.active = True

    def is_active(self) -> bool:
        return self.active

    def set_active(self, active: bool):
        self.active = active

    def deactivate(self):
        self.active = False

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if not self.active:
            raise ValueError(f"Product '{self.name}' is not active.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")
        self.set_quantity(self.quantity - quantity)
        return self.price * quantity
    
    

def main():
    product1 = Product("Laptop", 999.99, 10)
    product2 = Product("Smartphone", 499.99, 20)

    print(product1.display_info())
    print(product2.display_info())

    product1.set_quantity(5)
    print(product1.display_info())

    product1.deactivate()
    print(product1.display_info())

    try:
        product1.buy(3)
        print(product1.display_info())
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
