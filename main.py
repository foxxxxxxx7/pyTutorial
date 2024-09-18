class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        odd_total = 0
        even_total = 0
        total = 0

        clean_num = self.card_num[::-1].replace(' ', '')
        if not clean_num.isdigit():
            return False

        for n in clean_num[::2]:
            odd_total += int(n)
        for n in clean_num[1::2]:
            n = int(n) * 2
            if n > 9:
                n -= 9
            even_total += n
        total = even_total + odd_total
        return total % 10 == 0 and len(clean_num) > 1