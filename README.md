# Slot Machine Game 🎰

This is a simple command-line slot machine game built with Python. The project allows users to deposit money, place bets, spin the slot machine, and check if they've won based on the outcome. It's a fun, lightweight project to get started with basic Python programming concepts.

## Features

- **User Deposit**: Users can deposit money into their balance.
- **Betting System**: Users can select the number of lines to bet on and the amount to bet per line.
- **Slot Machine Spin**: The slot machine generates random outcomes and displays the result in a 3x3 grid.
- **Winning Check**: The game checks if the user has won based on matching symbols in the lines they bet on.
- **Dynamic Payouts**: The winnings are calculated based on symbol multipliers, with rarer symbols offering higher payouts.

## How It Works

1. **User Deposit**: The user is prompted to enter an amount to deposit. The balance is updated with this amount.
2. **Place Bets**: The user chooses the number of lines (up to 3) they want to bet on and the amount to bet on each line. The total bet is calculated and deducted from the balance.
3. **Spin the Slot Machine**: The slot machine generates a random 3x3 grid of symbols.
4. **Check Winnings**: If the user has matching symbols across any of the lines they bet on, they win and their balance is credited with the appropriate amount based on the symbol multipliers.
5. **Game Over**: The game continues until the user's balance reaches zero.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Usage

1. Just clone the repository now:
   ```bash
   git clone https://github.com/your-username/slot-machine-game.git
