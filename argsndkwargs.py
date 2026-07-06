# kwargs = allows you to pass multiple key word arguement which are stored in a dictionary
# args = allows you to pass multiple arguement

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5))

def display(*name):
    for arg in name:
        print(arg, end = " ")

display("John", "Doe", "is", "a", "developer")


# kwargs = allows you to pass multiple key word arguement which are stored in a dictionary
def address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(address(street = "123 Main St", city = "New York", state = "NY", zip_code = "10001"))

# using both args and kwargs in a function
def shipping_cost(*args, **kwargs):
    total_cost = 0
    for cost in args:
        total_cost += cost
    for key, value in kwargs.items():
        total_cost += value
        print(f"{key}: {value}")
    return total_cost

print(shipping_cost(10, 20, 30, tax = 5, shipping_fee = 15))


# random.randint() = returns a random integer between the given range
# random.randint(1, 10) = returns a random integer between 1 and 10 (inclusive)
# random.choice()
# random.choice("Hello") = returns a random character from the given string