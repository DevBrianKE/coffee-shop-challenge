class Order:
    def __init__(self, customer, coffee, price):
        # Create an order and link it to customer and coffee
        self.customer = customer
        self.coffee = coffee
        self.price = price

        customer.orders().append(self)
        coffee.orders().append(self)

    @property
    def price(self):
        # Get order price
        return self._price

    @price.setter
    def price(self, value):
        # Set price once; must be float between 1.0 and 10.0
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        if hasattr(self, '_price'):
            raise AttributeError("Price cannot be changed after set")
        self._price = value

    @property
    def customer(self):
        # Get customer
        return self._customer

    @customer.setter
    def customer(self, value):
        # Set customer; must be Customer instance
        if not isinstance(value, Customer):
            raise TypeError("Customer must be of type Customer")
        self._customer = value

    @property
    def coffee(self):
        # Get coffee
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        # Set coffee; must be Coffee instance
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be of type Coffee")
        self._coffee = value
