import random
import time

def spin_machine():
    symbols = ['🍉', '🍒', '🍋', '🔔', '⭐']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def print_symbols(row):
    print("┌───────────────┐")
    print("│ " + " | ".join(row) + " │")
    print("└───────────────┘")

def evaluate_spin(row , bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet*4
        elif row[0] == '🍋':
            return bet*5
        elif row[0] == '🔔':
            return bet*10
        elif row[0] == '⭐':
            return bet*20
    return 0


def start_game():
    balance = 100
    print("┌──────────────────────────────────┐")
    print("🎰 Welcome to Python Slots Machine🎰")
    print("└──────────────────────────────────┘")
    print("Symbols: 🍉 🍒 🍋 🔔 ⭐")

    while balance > 0:

        print (f"Current balance: ${balance}")
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid amount")
            continue

        bet = int (bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        result = spin_machine()


        print("Spinning: \n")
        time.sleep(1)
        print_symbols(result)

        payout = evaluate_spin(result, bet)

        if payout > 0:
            print(f"YOu won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to play again (Y/N): ")

        if play_again.lower() != 'y':
            break
    print("---------------")
    print(f"Game over! Your final balance is ${balance}")
    print("---------------")
if __name__ == '__main__':
    start_game()
