class Product:
    def __init__(self, name, price, quantity, active=True):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active

    def display_info(self):
        return f"Product Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}, Active: {self.active}"
    
    def quantity(self) -> int: 
        return self.quantity
    
    def set_quantity(self, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity cannot be zero or negative.")
        self.quantity = quantity
        
    def is_active(self) -> bool:
        return self.active
    
    def set_active(self, active: bool):
        self.active = active
        
    def deactivate(self):
        self.active = False 
        
    def show(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}, Active: {self.active}"
    
    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")
        self.quantity -= quantity
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