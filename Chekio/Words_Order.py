def words_order(text: str, words: list) -> bool:
    # i know this isn't the best solution and not even clear one, i just make it work
    if len(words) == 1 and words[0] in text:
        return True
    elif not text:
        return False
    
    text_list = text.split(" ")
    
    try:
        temp = text_list.index(words[0])
    except ValueError: return False
    
    k = []
    
    for i in words[1:]:
        try:
            p = text_list.index(i)
        except ValueError: return False
        
        if i in text_list and temp < p:
            k.append(True)
        else:
            k.append(False)
        
    return all(k)

if __name__ == '__main__':
    print("Example:")
    print(words_order("I am here", ['I', 'here']))      #True
    print(words_order("I am here", ['I', 'I']))         #False
    print(words_order("I am here", ['here', 'am']))     #False
    print(words_order("", ['I', 'am']))                 #False
    print(words_order("I am here", ['I']))              #True
    print(words_order('hi world im here', ['world', 'here', 'hi']))     #False
    print(words_order('hi world im here', ['world', 'hi', 'here']))     #False
    print(words_order('hi world im here', ['country', 'world']))        #False
