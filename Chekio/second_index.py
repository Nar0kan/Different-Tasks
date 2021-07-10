def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    try:
        k = text.index(symbol, text.index(symbol)+1, len(text))
    except:
        k = None
    return k

if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"), second_index(" hi", " "),
        second_index("hi mayor", " "), second_index("hi mr Mayor", " "))
