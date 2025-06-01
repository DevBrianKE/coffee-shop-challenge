class Coffee:
    def __init__(self, name):
        # Initialize coffee with name and empty orders list
        self.name = name
        self._orders = []

    @property
    def name(self):
        # Get coffee name
        return self._name

    @name.setter
    def name(self, value):
        # Enforce immutability: once set, the coffee name cannot be changed
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after set")
        self._name = value

    def orders(self):
        # List all orders for this coffee
        return self._orders

    def customers(self):
        # List unique customers who ordered this coffee
        return list({order.customer for order in self._orders})

    def num_orders(self):
        # Number of orders for this coffee
        return len(self._orders)

    def average_price(self):
        # Average price of all orders; 0 if none
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)
