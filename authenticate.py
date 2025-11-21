from sign_up import sign_up
import os
import bcrypt
import getpass

# Load from the environment variable or just use users.csv if it's not found
USER_FILE = os.getenv("USER_FILE") or "users.csv"


def authenticate() -> str:
    """Authenticates a user by signing them in and redirecting them to
    sign_up() if they don't have an account

    Returns:
        str: userid
    """

    # If the USER_FILE database doesn't exist then create it
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w"):
            pass

    # Check if the user has an account already
    while (
        account_exists := input("Do you have an account? (y/n): ").strip().casefold()
    ) not in ["y", "n"]:
        print('Please either enter "y" or "n"!')

    # If the user doesn't have an account, then sign them up for one
    if account_exists == "n":
        sign_up()

    while True:
        # Get the userid and password
        attempt_userid = input("Enter your user id: ").strip()
        # Use The getpass function to hide what the user is typing for security
        attempt_password = getpass.getpass("Enter your password: ").strip()

        # Open the USER_FILE database
        with open(USER_FILE, "r") as f:
            for line in f.readlines():
                # Try to read each line
                try:
                    userid, password_hash = line.strip().split(",")
                # If a line isn't parsable, then skip over it to avoid errors
                except ValueError:
                    continue
                # If the line contains info for a different userid, then continue
                if attempt_userid != userid:
                    continue
                # Check if the attempted password is valid for the userid
                if bcrypt.checkpw(attempt_password.encode(), password_hash.encode()):
                    # If it is then the user should be logged in with this userid
                    print(f"Successfully Logged In as userid: {userid}!")
                    return userid
                # Otherwise tell the user their password is incorrect
                print("Incorrect password!")
                break
            else:
                # If the userid doesn't exist in the database, then tell the user
                print("Incorrect userid!")

        # Try logging them in again
        print("Please try logging in again...")
