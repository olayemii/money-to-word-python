class DigitDictionary():

    """Class to get basic digits as words digits"""

    digit_map = {
        "units": {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"
        },
        "tens_less_than_twenty": {
            0: "ten",
            1: "eleven",
            2: "twelve",
            3: "thirteen",
            4: "fourteen",
            5: "fifteen",
            6: "sixteen",
            7: "seventeen",
            8: "eighteen",
            9: "nineteen"
        },
        "tens": {
            2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "ninety"
        },
        "hundreds": {
            0: "",
            1: "thousand",
            2: "million",
            3: "billion",
            4: "trillion"
        }
    }

    @staticmethod
    def get_unit_as_word(digit):
        return __class__.digit_map["units"][digit] \
            if digit in __class__.digit_map["units"] else ""

    @staticmethod
    def get_tens_less_than_twenty(digit):
        return __class__.digit_map["tens_less_than_twenty"][digit]\
            if digit in __class__.digit_map["tens_less_than_twenty"] else ""

    @staticmethod
    def get_tens(digit):
        return __class__.digit_map["tens"][digit] if digit in __class__.digit_map["tens"] else ""

    @staticmethod
    def get_hundreds(digit):
        return __class__.digit_map["hundreds"][digit] if digit in __class__.digit_map["hundreds"] else ""