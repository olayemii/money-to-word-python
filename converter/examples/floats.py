from converter import Converter

converter_object = Converter.Converter("naira", "kobo")

print(converter_object.convert("105.56"))
print(converter_object.convert("1012345.0"))
print(converter_object.convert("105.456"), True) #True flag will round kobo  100 to naira
print(converter_object.convert("105342.33"))