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

# Create orders: customer, coffee, price
o1 = Order(c1, cof1, 2.0)
o2 = Order(c1, cof2, 5.0)
o3 = Order(c1, cof1, 4.0)
o4 = Order(c2, cof2, 3.0)
o5 = Order(c2, cof3, 6.0)

if __name__ == "__main__":
    print("Coffee Shop Challenge Debug:")

    # Number of orders Steve made
    print(f"{c1.name}'s orders: {len(c1.orders())}")
    
    # Unique coffees Steve ordered
    print(f"{c1.name}'s coffees: {len(c1.coffees())}")
    
    # Total orders of Mocha
    print(f"{cof1.name} orders: {cof1.num_orders()}")
    
    # Average price for Mocha orders
    print(f"{cof1.name} avg price: {cof1.average_price()}")
    
    # Customer who spent most on Latte
    most_spender = Customer.most_aficionado(cof2)
    if most_spender:
        print(f"Top {cof2.name} customer: {most_spender.name}")
    else:
        print(f"No orders for {cof2.name}")
