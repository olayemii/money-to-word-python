import unittest
from converter import Converter
Language = {
    "ENGLISH": 1
}
class EnglishConversionText(unittest.TestCase):
    """
    This is a unit test for the end program
    - First time using TDD, cause i am awesome
    and you are if you do that too
    """
    def setUp(self) -> None:
        self.converter = Converter.Converter("naira", "kobo", Language["ENGLISH"])

    def test_whole_number(self):
        self.assertEqual("three hundred and forty-five naira only", self.converter.convert("345"))
        self.assertEqual("thirty-four naira only", self.converter.convert("34"));
        self.assertEqual("three hundred and forty-five thousand, three naira only", self.converter.convert("345003"));
        self.assertEqual("four hundred and seventy-five million, nine hundred and twenty-three thousand, four hundred and fifty-five naira only", self.converter.convert("475923455"));
        self.assertEqual("nine hundred and seventy-nine million, eight hundred and seven thousand, four hundred and fifty-five naira only",
                         self.converter.convert("979807455"));
    #
    def test_numbers_with_zero_prefixed(self):
        self.assertEqual("", self.converter.convert("0000000"))
        self.assertEqual("fifty thousand, three naira only", self.converter.convert("050003"))
        self.assertEqual("fifty thousand, three hundred and three naira only", self.converter.convert("050303"))
        self.assertEqual("five billion, four hundred and seventy-five million, nine hundred and twenty-three thousand, four hundred and fifty-five naira only", self.converter.convert("005475923455"))

    def test_decimal_number(self):
        self.assertEqual("twenty-three naira only", self.converter.convert("23.0"))
        self.assertEqual("three hundred and forty-five thousand, three naira, nine kobo only", self.converter.convert("345003.09"))
        self.assertEqual("two hundred and thirty-three million, four hundred and sixty-four thousand, seven hundred and seventy-three naira, four hundred and fifty-seven kobo only", self.converter.convert("233464773.457", False))
    #

if __name__ == "__main__":
    unittest.main()