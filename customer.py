from order import Order

class Customer:
    def __init__(self, name):
        # Initialize customer with name and empty orders list
        self.name = name
        self._orders = []

    @property
    def name(self):
        # Get customer's name
        return self._name

    @name.setter
    def name(self, value):
        # Set customer's name (1-15 chars)
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        # Return list of customer's orders
        return self._orders

    def coffees(self):
        # Return unique coffees customer ordered
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        # Create and add a new order for coffee at price
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        # Return customer who spent most on given coffee, or None
        spend_tracker = {}

        for order in coffee.orders():
            customer = order.customer
            spend_tracker[customer] = spend_tracker.get(customer, 0) + order.price

        if spend_tracker:
            return max(spend_tracker, key=spend_tracker.get)
        return None
