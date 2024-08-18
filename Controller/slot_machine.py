import random

MACHINE_ROWS = 3
MACHINE_COLS = 3

symbols_json = {"A": 2, "B": 4, "C": 6, "D": 8, "E": 10, "F": 12}


def get_slot_machine_spin(rows, cols, symbols):
    # Generate a 2D list of all symbols
    all_symbols = []

    # Iterate over the dictionary and store all the values in all_symobols
    for symbol, count in symbols.items():
        for index in range(count):
            # all_symbols.append(index)       # This line prints the indexs until count associated to the current key
            all_symbols.append(symbol)
        # all_symbols.append(" ")

    # Initialize columns list. This will contain actually column values
    columns = []  # It actually looks like this `column[[7], [7], [7]] - You Win!`

    # Generate a random value for each column
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[
            :
        ]  # This statement copies all_symbols list. So operations on current_symbols wont
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(
                value
            )  # This line removes the chosen value from current_symbols list

            # Add value to the column
            column.append(value)

        # Add column to columns list
        columns.append(column)

    return columns


def print_result(columns):
    # Get the number of rows from the length of the first column
    rows = len(columns[0])

    # Initialize a list to hold each formatted row
    result = []

    # Iterate over each row
    for row in range(rows):
        # Join the elements in each row with a pipe separator
        row_output = " | ".join(col[row] for col in columns)
        # Add the formatted row to the result list
        result.append(row_output)

    # Join all rows with a newline character and return the result
    return "\n".join(result)


# This dictionary defines how much a winning line with each symbol will multiply the bet.
# A gives the highest payout (5 times the bet).
# F gives the lowest payout (1 times the bet).
symbol_multipliers = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1.5, "F": 1}


def check_winning(columns, bet_amount, lines):
    winnings = 0
    winning_lines = []

    # Iterate over each line the user bet on
    for line in range(lines):
        symbol = columns[0][
            line
        ]  # Get the symbol from the first column of the current line
        won = True

        # Check if all symbols in this line are the same
        for col in columns:
            if col[line] != symbol:
                won = False
                break

        # If the line is a winning line
        if won:
            # Add winnings based on the symbol multiplier
            winnings += bet_amount * symbol_multipliers[symbol]
            winning_lines.append(
                line + 1
            )  # Add 1 to make it human-readable (1-indexed)

    return winnings, winning_lines
