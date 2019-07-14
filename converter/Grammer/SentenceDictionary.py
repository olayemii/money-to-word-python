from converter.Helpers import chunkify, reformatter
from converter.Grammer import DigitDictionary
import re
class SentenceDictionary():
    """
    This class is used for generating the sentence for each money
    making use of the DigitDictionary class as a building block,
    it generates the currency word by first splitting into groups of 3s
    from behind and parsing backwards-front
    """
    def __init__(self, main_currency, sub_currency, language=''):
        """init method to set main and sub currency for the sentence dictionary"""
        __class__.sub_currency = sub_currency
        __class__.main_currency = main_currency


    @staticmethod
    def get_sentence(digit, round_kobo):
        main_sentence = ""
        digit = digit.split(".")
        digits = reformatter.normalize_kobo(digit, round_kobo)
        if digits[0] > 0:
            main_sentence += __class__._get_sentence(str(digits[0]))+f" {__class__.main_currency}"+ (" only" if digits[1] == 0 else "")
        if digits[1] > 0:
            main_sentence += ", "+__class__._get_sentence(str(digits[1]))+" "+__class__.sub_currency+" only"

        return reformatter.reformat(main_sentence) if main_sentence else ""


    @staticmethod
    def _get_sentence(digit):
        """Master method for generating each word"""

        sentence = ""
        chunks = chunkify.chunkify(digit)
        # print(chunks)
        chunklen = len(chunks)
        for key,ars in enumerate(chunks):
            #check for length of current iter being above 2 (3 digits)
            #If above 2, get unit of last character in group -3
            if (len(ars) > 2) and ars[-3] != '0':
                #Send the hundreth value
                sentence += DigitDictionary.DigitDictionary.get_unit_as_word(int(ars[-3])) + " hundred "
                # If second or last number is zero dont add a trailing and
                if ars[-1] != '0' or ars[-2] != '0':
                    sentence += "and "
                #     Reformatting to remove unwanted commas, spaces
                sentence = reformatter.reformat(sentence)
            #     Condition to use get tns lower than 20
            # If previous element is 1
            if len(ars) > 1:
                if (ars[-2] != "1"):
                    sentence += DigitDictionary.DigitDictionary.get_tens(int(ars[-2]))
                else:
                    sentence += DigitDictionary.DigitDictionary.get_tens_less_than_twenty(int(ars[-1]))
                sentence = reformatter.reformat(sentence)
            if len(ars)  > 0:
                if not(len(ars) > 1 and ars[-2] == "1"):
                    sentence += ("-" if len(ars) > 1 and ars[-2] != '0' else "") + DigitDictionary.DigitDictionary.get_unit_as_word(int(ars[-1]))
                sentence += f" {(DigitDictionary.DigitDictionary.get_hundreds(chunklen-1-key))+', '} "
                sentence = reformatter.reformat(sentence)
        sentence = sentence.strip(" ,")
        # print(re.sub('\s+', 'a', sentence))
        # if  sentence:
        #     sentence = sentence + " " + __class__.main_currency + (" only" if include_cur else "")
        return sentence
    @staticmethod
    def _get_place_value(digitlen):
        if digitlen == 3:
            __class__.sentence += "hundred"
        elif digitlen == 4:
            __class__.sentence += "thousand"
