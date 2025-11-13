import sys
from lookup_products import lookup_products
from pack_products import pack_products
from authenticate import authenticate
from complete_order import complete_order


def scan_barcode() -> str:
    return "Sponge D12 Bottle"


def customer_summary(userid: str):
    pass


def main():
    # Welcome the user
    print("Welcome to the Q-Arm packing software...")

    # Authenticate the user and store the userid
    userid = authenticate()

    # Continue the main loop of scanning barcodes until the user is done
    while True:
        # Scan a barcode and save the value
        barcode = scan_barcode()

        # Get products array
        products = lookup_products(barcode)

        # Complete Q-Arm movements to pack the products
        pack_products(products)

        # Output a summary of the current order
        complete_order(userid, products)

        # Check if the user wishes to continue
        while (
            continue_scanning := input(
                "Would you like to keep scanning barcodes? (y/n) "
            )
            .strip()
            .casefold()
        ) not in ["y".casefold(), "n".casefold()]:
            print('Please either enter "y" or "n"!')

        # If the user doesn't wish to continue exit the loop
        if continue_scanning == "n".casefold():
            break

        # Continue scanning...

    # Once the program is complete output a total summary of all the orders
    customer_summary(userid)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard Interupt Detected...")
        print("Exiting the program!")
        sys.exit()
