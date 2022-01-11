def count_popular_words(text: str, words: list) -> dict:
    """
        Count popular words (that you give as second argument) in text line with ''' format.
    """
    result = {}
    text = text.lower()
    for symbol in range(0, len(text)):
        if text[symbol] == "\n":
            text = text[:symbol] + " " + text[symbol+1:]
    
    text_list = text.split(" ")
    print(text_list)
    for word in words:
        result[word] = text_list.count(word)
    return result

if __name__ == '__main__':
    print("Example: ")
    print(count_popular_words(
    '''When I was One
    I had just begun
    When I was Two
    I was nearly new''', 
    ['i', 'was', 'three', 'near']))    # {'i': 4, 'was': 3, 'three': 0, 'near': 0}