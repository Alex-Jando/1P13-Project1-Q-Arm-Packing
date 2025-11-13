def lookup_products(barcode: str) -> list[list[str | float]]:
    """Looks up product pricing info from the products.csv file

    Args:
        barcode (str): The scanned barcode containing product names

    Returns:
        list[list[str | float]]: 2D array of product names and prices
    """

    # Split products from scanned barcode
    products = barcode.strip().split(" ")

    # Make an empty product list
    products_list = []

    # For each product
    for product in products:
        # Try to find product in products database
        with open("products.csv", "r") as f:
            # Read through database
            for line in f.readlines():
                # Get the product from each line
                try:
                    name, price = line.split(",")

                    # If the line is blank there will be an unpacking error
                except ValueError:
                    pass

                # If product name matches
                if name == product:
                    products_list.append([name, float(price)])
                    break

            # If product not found then
            else:
                # Error Message since product not found
                print(f'ERROR: Product "{product}" not found in products database!')
    return products_list
