def second_index(text: str, symbol: str) -> int or None:
    """
        Find and return the second index of symbol (second argument) in text (first argument) as int number.
        If there is no such symbol or symbol have only one appearence - return None.
    """
    try:
        result = text.index(symbol, text.index(symbol)+1, len(text))
    except:
        result = None
    return result

if __name__ == '__main__':
    print('Example: ')
    print(second_index("sims", "s"))    # 3
    print(second_index(" hi", " ")) # None
    print(second_index("hi mayor", " "))    # None
    print(second_index("hi mr Mayor", " ")) # 5