# Define the maximum number of lines available
MAX_NUMBER_OF_LINES = 3

# Set max & min bet amount
MAX_BET_AMOUNT = 1000
MIN_BET_AMOUNT = 10


# Below function will take a user input as deposit amount
def user_deposit():
    try:
        # while true : because we will keep executing this function until valid response is given by user
        while True:
            user_input = input("Enter the amount you want to deposit: $")
            # checking if the input is a valid number
            if user_input.isdigit():
                # isdigit() function will check if the amount is actually a positive whole number. It will check for number even in a string
                # Now cast the input to float or int, as by default it comes as a string
                amount = float(user_input)

                # Now check if the amount is positive. if yes break outta while loop [as valid amount entered]
                if amount > 0:
                    break
                else:
                    print("Please enter amount greater than 0")
            else:
                print(f"Please enter a number")
        return amount
    except Exception as e:
        print(f"Here is user_deposit() function exception {e}")


# The function that takes user input for number of lines to bet on
def get_number_of_lines():
    try:
        while True:
            lines = input(
                f"Enter number of lines to bet on (1 - {str(MAX_NUMBER_OF_LINES)})?"
            )
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= MAX_NUMBER_OF_LINES:
                    break
                else:
                    print(f"Please enter a number between 1 and {MAX_NUMBER_OF_LINES}")
            else:
                print(f"Please enter a number")

        return lines
    except Exception as e:
        print(f"Here is get_number_of_lines() function exception {e}")


# The function to get the user bet amount
def get_user_bet_amount():
    try:
        while True:
            bet_amount = input("Enter the amount you want to bet on each line: $")
            if bet_amount.isdigit():
                bet_amount = float(bet_amount)

                if MIN_BET_AMOUNT <= bet_amount <= MAX_BET_AMOUNT:
                    break
                else:
                    print(
                        f"Please enter an amount between ${MIN_BET_AMOUNT} and ${MAX_BET_AMOUNT}"
                    )
            else:
                print(f"Please enter a number")
        return bet_amount
    except Exception as e:
        print(f"Here is get_user_bet_amount() function exception {e}")
