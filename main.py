import sys

sys.path.append("../")

# Package used to manage environment variables
try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    print('WARNING: Please install the "dotenv" module to use environment variables.')

# Loads the environment variables that specify file paths
load_dotenv(".env")

from Common.qarm_interface_wrapper import BarcodeScanner
from lookup_products import lookup_products
from pack_products import pack_products, arm
from authenticate import authenticate
from complete_order import complete_order
from customer_summary import customer_summary

scan_barcode = BarcodeScanner.scan_barcode


def main():
    """Main function for Q-Arm packing software"""

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


# Common check to only run the full program if the main file is run directly
if __name__ == "__main__":
    try:
        # Calibrate the Q-Arm gripper to open at 1200 degrees
        arm.rotate_gripper(1200)
        # Run the main function
        main()
    except KeyboardInterrupt:
        # If ctrl+c is pressed at any point exit the program
        print("Keyboard Interupt Detected...")
        print("Exiting the program!")
    finally:
        # Disconnect the Q-Arm
        arm.end_arm_connection()
        # Exit the program
        sys.exit()
