# Coffee Shop Challenge - Object Relationships

## Overview

This project implements a coffee shop domain model with three main classes: `Customer`, `Coffee`, and `Order`. The implementation demonstrates object relationships in Python, including one-to-many and many-to-many relationships, property validation, and aggregate methods.

## Classes

### Customer

Represents a coffee shop customer with:

- **Properties**:
  - `name`: Validated string (1-15 characters)
  
- **Methods**:
  - `orders()`: Returns all orders placed by the customer
  - `coffees()`: Returns unique coffees ordered
  - `create_order(coffee, price)`: Creates a new order
  - `most_aficionado(coffee)`: Class method to find top spender for a coffee

### Coffee

Represents a coffee type with:

- **Properties**:
  - `name`: Validated string (≥3 characters), immutable after creation
  
- **Methods**:
  - `orders()`: Returns all orders for this coffee
  - `customers()`: Returns unique customers who ordered this coffee
  - `num_orders()`: Returns total order count
  - `average_price()`: Calculates mean order price

### Order

Represents a transaction linking a customer to a coffee:

- **Properties**:
  - `customer`: Must be Customer instance
  - `coffee`: Must be Coffee instance
  - `price`: Validated float (1.0-10.0), immutable after creation

## Relationships

- A `Customer` has many `Orders`
- A `Coffee` has many `Orders`
- An `Order` belongs to one `Customer` and one `Coffee`
- `Customer` and `Coffee` have a many-to-many relationship through `Order`

## Example Usage

```python
from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
c1 = Customer("Steve")
c2 = Customer("Diana")

# Create coffees
cof1 = Coffee("Mocha")
cof2 = Coffee("Latte")
cof3 = Coffee("Cappuccino")

# Create orders
o1 = Order(c1, cof1, 2.0)
o2 = Order(c1, cof2, 5.0)
o3 = Order(c1, cof1, 4.0)
o4 = Order(c2, cof2, 3.0)
o5 = Order(c2, cof3, 6.0)

# Query relationships
print(f"{c1.name} ordered {len(c1.orders())} times")
print(f"{cof1.name} was ordered {cof1.num_orders()} times")
print(f"Average price for {cof1.name}: ${cof1.average_price():.2f}")
print(f"Top {cof2.name} customer: {Customer.most_aficionado(cof2).name}")

## Features

- **Validation**: Strict type and value checking for all properties
- **Immutability**: Certain properties cannot be changed after creation
- **Relationship Management**: Automatic maintenance of two-way relationships
- **Aggregate Methods**: Statistical calculations like average price
- **Bonus Method**: Identifies top spending customer per coffee type

## Testing

The implementation includes test cases in the `tests/` directory:

- `customer_test.py`: Tests Customer class functionality
- `coffee_test.py`: Tests Coffee class functionality
- `order_test.py`: Tests Order class functionality

Run tests to verify all requirements are met.

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Clone the repository
2. Navigate to project directory
3. Run with Python: `python debug.py` to see example output