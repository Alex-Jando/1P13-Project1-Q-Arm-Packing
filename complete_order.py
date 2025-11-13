import os
import random

ORDERS_FILE = "orders.csv"
TAX = 0.13


def complete_order(userid: str, products: list[list[str | float]]):
    # Create the ORDERS_FILE database if it doesn't already exist
    if not os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "w"):
            pass

    with open(ORDERS_FILE, "a") as f:
        # create empty cumulative variables
        total_price = 0
        file_data = ""
        users = []
        order_count = 0
        receipt = f"{'=' * 33}\n{('Order Summary'):^33}\n{'_' * 33}\n"

        for product in products:
            # Add formatted receipt row to receipt
            receipt += f"|{product[0]:<20}{('$' + str(round(product[1], 2))):>10}\t|\n"  # type: ignore
            # Add formatted string to file_data
            file_data += f",{product}"
            # Add price
            total_price += round(product[1], 2)  # type: ignore
        # Calculate discount, tax, and final price
        discount_percent = random.uniform(0.05, 0.5)
        discount_amount = round(total_price * discount_percent, 2)
        tax_amount = round((total_price - discount_amount) * (TAX), 2)
        final_price = round((total_price - discount_amount + tax_amount), 2)

        # add final receipt lines to receipt
        receipt += f"{'=' * 33}\nSubtotal:   \t\t${total_price:>6}\n"
        receipt += f"Discount:   \t\t${(discount_amount):>6}\n"
        receipt += f"Tax:        \t\t${(tax_amount):>6}\n"
        receipt += f"Final Price:\t\t${final_price:>6}\n"
        # add userid and final price to file_data
        file_data = f"{userid},{final_price}" + file_data + "\n"

        # write to orders.csv and close
        f.write(file_data)

    with open(ORDERS_FILE, "r") as f:
        # read open orders.csv to read
        for line in f.readlines():
            users.append(line.split(",")[0])

        order_count = users.count(userid)

        # add final message to receipt and print
        receipt += f"\nYou've made {order_count} order{'s' if order_count > 1 else ''}!\nThank you for your purchase!"
        print(receipt)
