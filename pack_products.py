from Common.qarm_interface_wrapper import QArmInterface
from time import sleep

GRIPPER_IMPLEMENTATION = 1
arm = QArmInterface(GRIPPER_IMPLEMENTATION)


def drop(gripper_extension: float):
    sleep(1)
    arm.home()
    sleep(1)
    arm.rotate_base(-55)
    sleep(1)
    arm.rotate_elbow(25)
    sleep(1)
    arm.rotate_gripper(gripper_extension)
    sleep(1)
    arm.home()
    sleep(1)


def sponge():
    sleep(1)
    arm.home()
    sleep(1)
    arm.rotate_base(17)
    sleep(1)
    arm.rotate_shoulder(40)
    sleep(1)
    arm.rotate_elbow(-7)
    sleep(1)
    arm.rotate_gripper(-600)
    sleep(1)
    arm.rotate_shoulder(-30)
    sleep(1)
    arm.home()
    sleep(1)
    drop(600)


def bottle():
    sleep(1)
    arm.home()
    sleep(1)
    arm.rotate_base(11)
    sleep(1)
    arm.rotate_shoulder(41)
    sleep(1)
    arm.rotate_elbow(-7)
    sleep(1)
    arm.rotate_gripper(-600)
    sleep(1)
    arm.rotate_shoulder(-30)
    sleep(1)
    arm.home()
    sleep(1)
    drop(600)


def pack_products(products: list[list[str | float]]):
    for product in products:
        name = product[0]
        # have a function for each product movement
        if name == "Sponge":
            # Do Q-Arm movement to grab sponge item

            sponge()

        elif name == "Bottle":
            # Do Q-Arm movement to grab bottle item

            bottle()

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
