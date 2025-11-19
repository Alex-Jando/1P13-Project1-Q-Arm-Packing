import os
import random

# Load from the environment variable or just use orders.csv if it's not found
ORDERS_FILE = os.getenv("ORDERS_FILE") or "orders.csv"
TAX = 0.13


def complete_order(userid: str, products: list[list[str | float]]):
    """Prints a order summary and records the current order the orders database

    Args:
        userid (str): The userid which placed the order
        products (list[list[str  |  float]]): A list of the products that were made in the order and their prices
    """

    # Create the ORDERS_FILE database if it doesn't already exist
    if not os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "w"):
            pass

    # Sum up the prices of each product
    sub_total = sum([price for _, price in products])  # type: ignore
    # random.uniform generates a random number between 0.05 and 0.5 with equal probabilities for every value
    discount_total = sub_total * random.uniform(0.05, 0.5)
    # Calculate the tax amout
    tax_total = (sub_total - discount_total) * TAX
    # Calculate the final price to be paid
    final_total = sub_total - discount_total + tax_total

    # Save the data to the orders database
    with open(ORDERS_FILE, "a") as f:
        f.write(
            f"{userid},{final_total:.2f},{','.join([product for product, _ in products])}\n"  # type: ignore
        )

    # Declare an empty counter to record the number of orders by this userid
    order_count = 0

    # Loop over the orders database
    with open(ORDERS_FILE, "r") as f:
        for line in f.readlines():
            # Seperate the userid
            line_userid, *_ = line.strip().split(",")
            # Check whether the order on this line belongs to the current userid
            if line_userid == userid:
                # If it does then increment the order_count
                order_count += 1

    # Print out a final recipet with all the information relevant to the order
    print("=" * 30)
    print(f"{'Order Summary':^30}")
    print("=" * 30)
    print(f"{'Product'}{'Price':>23}")
    print("-" * 30)
    for product, price in products:
        print(f"{product:20}${f'{price:.2f}':>9}")
    print("=" * 30)
    print(f"{'Subtotal:':20}${f'{sub_total:.2f}':>9}")
    print(f"{'Discount:':20}${f'{discount_total:.2f}':>9}")
    print(f"{'Tax:':20}${f'{tax_total:.2f}':>9}")
    print(f"{'Final Price:':20}${f'{final_total:.2f}':>9}")
    print("=" * 30)
    print(
        f"{f"You've made {order_count} order{'s' if order_count != 1 else ''} so far.":^30}"
    )
    print(f"{'Thank you for your purchase!':^30}")
    print("=" * 30)
