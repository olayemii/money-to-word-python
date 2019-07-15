import math
def chunkify(digit, chunkLength=3):
    chunks = []
    for val in range(-1, -len(digit) - 1, -chunkLength):
        chunks.insert(0, list(digit[val - (chunkLength-1): val + 1 if val + 1 != 0 else None]))
    return chunks