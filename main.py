#Untangled logic into smaller functions for testing purposes:
def pin_length(pin):
    if len(str(pin)) != 4:
        raise ValueError("Please enter a 4 digit pin.")

    return True

def positive_withdrawal_balance(amount):
    if amount < 0:
        raise ValueError("Please enter a positive amount.")

    return True

def check_pin_is_number(pin):
    res = isinstance(pin, int)
    if res == False:
        raise ValueError("Please enter a number")

    return True

#Functions used by the program:
def pin_validated(pin):
    if len(str(pin)) != 4:
        raise ValueError("Please enter a 4 digit pin.")

    res = isinstance(pin, int)
    if res == False:
        raise ValueError("Please enter a number")

    assert pin == 2468

    return True

def withdrawal_validated(withdrawal):
    if withdrawal > 100:
        raise ValueError(f"You do not have enough in your account to withdraw £{format(withdrawal, '.2f')}")

    if withdrawal < 0:
        raise ValueError(f"Please enter a positive amount.")

    return True

success = False

for i in range(3):
    try:
        userPin = input("Enter your pin: ")
        pin_validated(int(userPin))
        withdrawal = input("Current Balance: £100. Please enter how much you would like to withdraw: ")
        withdrawal_validated(float(withdrawal))

    except AssertionError as exc:
        print("Pin incorrect, please contact your bank.")
        success = False

    except ValueError as exc:
        print(f"Invalid input: {exc}")
        success = False

    else:
        balance = 100 - float(withdrawal)
        print(f"Withdrawing £{withdrawal}. New current balance: £{format(round(balance, 2), '.2f')}")
        success = True

    finally:
        if success:
            print("Your transaction has been processed. Thank you for banking with us.")
        else:
            print("Could not complete your transaction.")
