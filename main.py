import random

def line_breaker():
    print('-' * 23)

def spin_row():
    symbols = ['🍒', '🍑', '🍋', '🎰', '⭐']
    return random.choices(symbols, k=3)

def print_row(row):
    print(" | ".join(row))
    line_breaker()

def get_payout(row, bet):
    payout_multipliers = {'🍒': 3, '🍑': 5, '🍋': 10, '🎰': 10, '⭐': 50}
    return bet * payout_multipliers.get(row[0], 0) if row.count(row[0]) == 3 else 0

def main():
    balance = 100

    line_breaker()
    print('Welcome to the slot machine')
    print('Symbols: 🍒 🍑 🍋 🎰 ⭐')
    line_breaker()

    while balance > 0:
        print(f"Current balance: €{balance}")

        try:
            bet = int(input('Place your bet: '))
            if bet <= 0:
                raise ValueError('Bet must be a positive number')
            if bet > balance:
                raise ValueError('Insufficient funds')
        except ValueError as e:
            line_breaker()
            print(e)
            line_breaker()
            continue

        balance -= bet
        row = spin_row()
        line_breaker()
        print('Spinning...\n')
        print_row(row)

        payout = get_payout(row, bet)
        balance += payout

        line_breaker()
        print(f'You won! €{payout}' if payout > 0 else 'Sorry, you lost this round')
        line_breaker()

        if input('Do you want to play again? (y/n): ').lower() != 'y':
            break

    line_breaker()
    print(f'Game Over! Your final balance is €{balance}')
    line_breaker()

if __name__ == '__main__':
    main()
