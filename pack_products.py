from Common.qarm_interface_wrapper import QArmInterface
from time import sleep

GRIPPER_IMPLEMENTATION = 1
arm = QArmInterface(GRIPPER_IMPLEMENTATION)


def drop(gripper_extension: float):
    """Drops the product into the delivery bin

    Args:
        gripper_extension (float): The amount the gripper needs to open
    """
    sleep(1)
    arm.home()
    sleep(1)
    arm.rotate_base(-50)
    sleep(1)
    arm.rotate_elbow(25)
    sleep(1)
    arm.rotate_shoulder(-15)
    sleep(1)
    arm.rotate_gripper(gripper_extension)
    sleep(1)
    arm.home()
    sleep(1)


def sponge():
    """Picks up the Sponge product"""
    sleep(1)
    arm.home()
    sleep(1)
    arm.rotate_base(19)
    sleep(1)
    arm.rotate_shoulder(40)
    sleep(1)
    arm.rotate_elbow(-9)
    sleep(1)
    arm.rotate_gripper(-600)
    sleep(1)
    arm.rotate_shoulder(-30)
    sleep(1)
    arm.home()
    sleep(1)
    drop(600)


def bottle():
    """Picks up the Bottle product"""
    sleep(1)
    arm.home()
    sleep(1)
    arm.rotate_base(12)
    sleep(1)
    arm.rotate_shoulder(42)
    sleep(1)
    arm.rotate_elbow(-10)
    sleep(1)
    arm.rotate_gripper(-650)
    sleep(1)
    arm.rotate_shoulder(-30)
    sleep(1)
    arm.home()
    sleep(1)
    drop(650)


def rook():
    """Picks up the Rook product"""
    sleep(1)
    arm.home()
    sleep(1)
    arm.rotate_gripper(-100)
    sleep(1)
    arm.rotate_base(5)
    sleep(1)
    arm.rotate_shoulder(40)
    sleep(1)
    arm.rotate_elbow(-10)
    sleep(1)
    arm.rotate_shoulder(5)
    sleep(1)
    arm.rotate_gripper(-900)
    sleep(1)
    arm.rotate_shoulder(-30)
    sleep(1)
    arm.home()
    sleep(1)
    drop(1000)


def d12():
    """Picks up the D12 product"""
    sleep(1)
    arm.home()
    sleep(1)
    arm.rotate_gripper(-100)
    sleep(1)
    arm.rotate_base(-2)
    sleep(1)
    arm.rotate_shoulder(40)
    sleep(1)
    arm.rotate_elbow(-12)
    sleep(1)
    arm.rotate_shoulder(7)
    sleep(1)
    arm.rotate_gripper(-600)
    sleep(1)
    arm.rotate_shoulder(-30)
    sleep(1)
    arm.home()
    sleep(1)
    drop(700)


def witch_hat():
    """Picks up the Witch Hat product"""
    sleep(1)
    arm.home()
    sleep(1)
    arm.rotate_gripper(-300)
    sleep(1)
    arm.rotate_base(-9)
    sleep(1)
    arm.rotate_shoulder(40)
    sleep(1)
    arm.rotate_elbow(-13)
    sleep(1)
    arm.rotate_shoulder(7)
    sleep(1)
    arm.rotate_gripper(-900)
    sleep(1)
    arm.rotate_shoulder(-30)
    sleep(1)
    arm.home()
    sleep(1)
    drop(1200)


def bowl():
    """Picks up the Bowl product"""
    sleep(1)
    arm.home()
    sleep(1)
    arm.rotate_base(-14)
    sleep(1)
    arm.rotate_shoulder(41)
    sleep(1)
    arm.rotate_elbow(-17)
    sleep(1)
    arm.rotate_shoulder(8)
    sleep(1)
    arm.rotate_gripper(-1000)
    sleep(1)
    arm.rotate_shoulder(-30)
    sleep(1)
    drop(1000)


def pack_products(products: list[list[str | float]]):
    """Controls the Q-Arm to pickup the products

    Args:
        products (list[list[str  |  float]]): A list of the products to be packed
    """

    for product in products:
        name = product[0]
        if name == "Sponge":
            # Do Q-Arm movement to grab sponge item

            sponge()

        elif name == "Bottle":
            # Do Q-Arm movement to grab bottle item

            bottle()

        elif name == "Rook":
            # Do Q-Arm movement to grab rook item

            rook()

        elif name == "D12":
            # Do Q-Arm movement to grab d12 item

            d12()

        elif name == "WitchHat":
            # Do Q-Arm movement to grab witch hat item

            witch_hat()

        elif name == "Bowl":
            # Do Q-Arm movement to grab bowl item

            bowl()

        else:
            # If the product name isn't one of the valid products print error message
            print(f"ERROR: product {name} not a packable product.")
            continue

        print(f"{name} product successfully packed!")
