import os

ORDERS_FILE = "orders.csv"


def customer_summary(userid: str):
    """Prints a customer summary of all orders made by the userid

    Args:
        userid (str): The userid for which information will be printed
    """

    # Create the ORDERS_FILE database if it doesn't already exist
    if not os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "w"):
            pass

    # Declare an empty counter to track total product cost
    total_cost = 0
    # Declare an empty list to track each order made by the userid
    user_orders = []

    # Open the ORDERS_FILE
    with open(ORDERS_FILE, "r") as f:
        # Read through each line
        for line in f.readlines():
            # Break apart the data on each line
            line_userid, line_total, *line_products = line.strip().split(",")
            # If the line isn't an order for the current userid then skip over it
            if not line_userid == userid:
                continue
            # Increment the total cost
            total_cost += float(line_total)
            # Record the order
            user_orders.append(line_products)

    # Declare an empty dictionary to counter product orders
    product_count = {}

    # Loop over all products
    for order in user_orders:
        for product in order:
            # If the product isn't already counted for set its count to 1
            if product not in product_count:
                product_count[product] = 1
            # If the product is already counter then increment it by 1
            else:
                product_count[product] += 1

    # Print out the final reciept containing information from all the orders
    print("=" * 30)
    print(f"{'Customer Summary':^30}")
    print("=" * 30)
    print(f"User ID: {userid:>21}")
    print(f"Total Cost: {(f'${total_cost:.2f}'):>18}")
    print(f"Total Orders: {len(user_orders):>16}")
    print("=" * 30)
    print(f"{'Product'}{'Quantity':>23}")
    print("-" * 30)
    # Loop over the product_counter dictionary for the counts of the different products
    for product, count in product_count.items():
        print(f"{product:26}{count:>4}")
    print("=" * 30)
