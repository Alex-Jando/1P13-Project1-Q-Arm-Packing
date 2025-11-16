import os
import bcrypt
import getpass
import string

USER_FILE = "users.csv"


def valid_password(password: str) -> bool:
    """Checks whether a certain password is valid according to security criteria

    Args:
        password (str): The password to be checked

    Returns:
        bool: The validity of the password
    """

    # If the password is less than 6 characters it's invalid
    if len(password) < 6:
        return False
    # Check if the password contains any of the symbols
    for s in string.punctuation:
        if s in password:
            # If it contains a symbol then it is valid
            return True
    # If it doesn't contain punctuation then it is invalid
    return False


def sign_up():
    """Signs up a new user account and saves the new info in the user database"""

    # Tell the user they are signing up a new account
    print("Signing up a new account...")

    # If the USER_FILE database doesn't exist then create it
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w"):
            pass

    while True:
        # Get a new userid
        print("Userids must meet the following criteria:")
        print("1. Must be unique (can't already exist)")
        print("2. Can only contain letters and numbers")
        print("3. Can't contain any spaces")
        new_userid = input("Enter your new userid: ").strip()

        # Check if the entered userid meets contains only alphanumeric characters
        if not new_userid.isalpha():
            print("Your new userid contains non-alphanumeric characters!")
            continue

        # Open the UESR_FILE database
        with open(USER_FILE, "r") as f:
            for line in f.readlines():
                # Try to read each line
                try:
                    userid, _ = line.strip().split(",")
                # If a line isn't parsable, then skip over it to avoid an error
                except ValueError:
                    continue
                # Check if the userid on that line is the same as the new_userid
                if new_userid == userid:
                    # If it is then inform the user that the userid is already taken
                    print("Sorry, that userid already exists!")
                    break
            else:
                # If the userid doesn't already exist, then continue in the program
                break
    while True:
        # Inform the user of the password criteria
        print("For security, all passwords must meet the following criteria:")
        print("1. 6 or more characters")
        print(f"2. At least one of the following symbols: {string.punctuation}")
        # Prompt the user to create a new password and confirm it
        new_password = getpass.getpass("Enter your new password: ").strip()
        new_password_confirm = getpass.getpass("Confirm your new password: ").strip()
        # Ensure the passwords match
        if new_password != new_password_confirm:
            # If the passwords don't match then inform the user and tell them to re-enter them
            print("Your passwords don't match!")
            continue
        # Ensure the password are valid
        if not valid_password(new_password):
            # If the password is invalid then inform the user and tell them to re-enter them
            print("Your password doesn't meet the security criteria!")
            continue
        # If the passwords are confirmed and are valid then continue in the program
        break

    # Open the USER_FILE database, and append the new user account information to it
    with open(USER_FILE, "a") as f:
        # Hash the password before adding it to the file
        new_password_hash = bcrypt.hashpw(
            new_password.encode(),
            bcrypt.gensalt(),
        ).decode()
        f.write(f"{new_userid},{new_password_hash}\n")

    # Let the user know their new account has been created successfully

    print("Congratulations... Your new account has been created succesfully!")
