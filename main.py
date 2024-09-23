class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean_number(number)
        self.area_code = self.number[0:3]
        self.exchange_code = self.number[3:6]
        self.subs_num = self.number[6:10]

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subs_num}"

    def clean_number(self, number):
        clean_num = number.translate(str.maketrans(")(.-+", "     ")).replace(' ', '')
        if len(clean_num) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(clean_num) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(clean_num) == 11 and clean_num[0] != '1':
            raise ValueError("11 digits must start with 1")
        if (len(clean_num) == 11 and clean_num[1] == '0') or (len(clean_num) == 10 and clean_num[0] == '0'):
            raise ValueError("area code cannot start with zero")
        if (len(clean_num) == 11 and clean_num[1] == '1') or (len(clean_num) == 10 and clean_num[0] == '1'):
            raise ValueError("area code cannot start with one")
        if (len(clean_num) == 11 and clean_num[4] == '0') or (len(clean_num) == 10 and clean_num[3] == '0'):
            raise ValueError("exchange code cannot start with zero")
        if (len(clean_num) == 11 and clean_num[4] == '1') or (len(clean_num) == 10 and clean_num[3] == '1'):
            raise ValueError("exchange code cannot start with one")
        elif len(clean_num) == 11:
            clean_num = clean_num[1:]
        for c in clean_num:
            if c.isalpha():
                raise ValueError("letters not permitted")
            elif not c.isdigit():
                raise ValueError("punctuations not permitted")

        return clean_num