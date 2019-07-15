from converter import Converter

converter_object = Converter.Converter("naira", "kobo")

print(converter_object.convert("100000000000000000000000"))
print(converter_object.convert("1012345"))
print(converter_object.convert("1012325"))
print(converter_object.convert("105342"))