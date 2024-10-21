class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '') 

    def valid(self):
        if not self.card_num.isdigit() or len(self.card_num) <= 1:
            return False

        total = 0
        reversed_digits = map(int, self.card_num[::-1])  

        for i, digit in enumerate(reversed_digits):
            if i % 2 == 1: 
                digit *= 2
                if digit > 9:
                    digit -= 9
            total += digit

        return total % 10 == 0