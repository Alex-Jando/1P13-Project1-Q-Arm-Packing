def pack_products(products: list[list[str | float]]):
    for product in products:
        name = product[0]
        # have a function for each product movement
        if name == "Sponge":
            # Do Q-Arm movement to grab sponge item

            pass

        elif name == "Bottle":
            # Do Q-Arm movement to grab bottle item

            pass

        elif name == "Rook":
            # Do Q-Arm movement to grab rook item

            pass

        elif name == "D12":
            # Do Q-Arm movement to grab d12 item

            pass

        elif name == "WitchHat":
            # Do Q-Arm movement to grab witch hat item

            pass

        elif name == "Bowl":
            # Do Q-Arm movement to grab bowl item

            pass

        else:
            print(f"ERROR: product {name} not a packable product.")
            continue

        print(f"{name} product successfully packed!")
