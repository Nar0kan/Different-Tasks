# I know this isn't the best solution and not even clear one, i just make it work
def words_order(text: str, words: list) -> bool:
    """
        Checks if words in text are in the same order as you write in arguments. 
        First argument - text(string), second one - words (list of strings)
    """
    if len(words) == 1 and words[0] in text:
        return True
    elif not text:
        return False
    
    text_list = text.split(" ")
    
    try:
        first_word = text_list.index(words[0])
    except ValueError: return False
    
    result = []
    
    for word in words[1:]:
        try:
            word_index = text_list.index(word)
        except ValueError: return False
        
        if word in text_list and first_word < word_index:
            result.append(True)
        else:
            result.append(False)
    
    return all(result)

if __name__ == '__main__':
    print("Example: ")
    print(words_order("I am here", ['I', 'here']))      #True
    print(words_order("I am here", ['I', 'I']))         #False
    print(words_order("I am here", ['here', 'am']))     #False
    print(words_order("", ['I', 'am']))                 #False
    print(words_order("I am here", ['I']))              #True
    print(words_order('hi world im here', ['world', 'here', 'hi']))     #False
    print(words_order('hi world im here', ['world', 'hi', 'here']))     #False
    print(words_order('hi world im here', ['country', 'world']))        #False