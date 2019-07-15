from converter.Grammar import DigitDictionary, SentenceDictionary
from converter.Exceptions import DumbheadException
class Converter():
    def __init__(self, main_currency, sub_currency, language=''):
        self.b= SentenceDictionary.SentenceDictionary(main_currency, sub_currency, language)
    def convert(self, value, round_kobo=False):
        try:
            if float(value) > 999999999999999:
                raise DumbheadException.DumbHeadException("Come on, you are that type that keeps searching for what could break a program?")
        except DumbheadException.DumbHeadException as e:
            print(e.message)
            exit()

        return self.b.get_sentence(str(float(value)), round_kobo) #Removing trailing zeroes when casted to int
a = Converter("dollars", "cents")
#
#
# for i in  range(500, 2000000000, 2030405):
#     print(i, a.convert(str(i)))
#
# print(a.convert(105))