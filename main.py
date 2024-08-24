import random


def line_breaker():
    print('-----------------------')


def spin_row():
    symbols = ['🍒', '🍑', '🍋', '🎰', '⭐']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))
    line_breaker()


def get_payout(row, bet):
    if row[0] == row [1] == row[2]:
        if row[0] == '🍒':
            return bet *3
        elif row[0] == '🍑':
            return bet *5
        elif row[0] == '🍋':
            return bet *10
        elif row[0] == '🎰':
            return bet *10
        elif row[0] == '⭐':
            return bet *50
    return 0


def main():
    balance = 100

    line_breaker()
    print('Welcome to the slot machine')
    print('Symbols: 🍒 🍑 🍋 🎰 ⭐')
    line_breaker()


    while balance > 0 :
        print(f"Current balance: €{balance}")

        bet = input('Place your bet: ')

        if not bet.isdigit():
            line_breaker()
            print('Please enter a valid number')
            line_breaker()
            continue

        bet = int(bet)

        if bet > balance:
            line_breaker()
            print('Insufficent funds')
            line_breaker()
            continue

        if bet <= 0:
            line_breaker()
            print('Bet must be a positive number')
            line_breaker()
            continue

        balance -= bet

        row = spin_row()
        line_breaker()
        print('Spinning... \n')
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            line_breaker()
            print(f'You won! €{payout}')
            line_breaker()
        else:
            line_breaker()
            print('Sorry you lost this round')
            line_breaker()

        balance += payout

        play_again = input('Do you want to play again? (y/n): ').lower()

        if play_again != 'y':
            break

    line_breaker()
    print(f'Game Over! Your final balance is €{balance}')
    line_breaker()

if __name__ == '__main__':
    main()
