

[1,2,3,4]
"Hello, world"

def find_symbol(text: str, symbol: str) -> int:
    return text.find(symbol)

def find_symbol_my(text: str, symbol: str) -> int:
    # for index, char in enumerate(text):
    #     if char == symbol:
    #         return index

    for i in range(len(text)):
        if text[i] == symbol:
            return i
    return -1

print(find_symbol_my("Hello, world", "w"))