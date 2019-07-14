import math
def chunkify(digit, chunkLength=3):
    maximum_array_elements = math.ceil(len(digit) / chunkLength)
    chunks = []
    for val in range(-1, -len(digit) - 1, -chunkLength):
        chunks.insert(0, list(digit[val - (chunkLength-1): val + 1 if val + 1 != 0 else None]))
    return chunks