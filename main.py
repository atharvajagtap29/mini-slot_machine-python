from Controller.user_actions import (
    user_deposit,
    get_number_of_lines,
    get_user_bet_amount,
)

from Controller.slot_machine import (
    get_slot_machine_spin,
    print_result,
    check_winning,  # Import the new function
    MACHINE_ROWS,
    MACHINE_COLS,
    symbols_json,
)


def main():
    balance = user_deposit()
    print(f"Your current balance is: ${balance}")

    while balance > 0:
        lines = get_number_of_lines()
        amount = get_user_bet_amount()

        total_amount = lines * amount
        print(
            f"You have bet on {lines} lines with ${amount} per line. Total bet: ${total_amount}"
        )

        if balance >= total_amount:
            balance -= total_amount
            print(f"Bet placed successfully. Your new balance is: ${balance}")

            result = get_slot_machine_spin(MACHINE_ROWS, MACHINE_COLS, symbols_json)
            final_result = print_result(result)
            print(final_result)

            # Check if the user has won
            winnings, winning_lines = check_winning(result, amount, lines)

            if winnings > 0:
                balance += winnings
                print(
                    f"Congratulations! You've won ${winnings} on lines: {', '.join(map(str, winning_lines))}"
                )
                print(f"Your new balance is: ${balance}")
            else:
                print("No win this time. Better luck next time!")

        else:
            print(f"Insufficient balance to place this bet. Your balance: ${balance}")
            print(f"Try Again!")

    if balance <= 0:
        print("Your balance is zero. Game over.")


main()
