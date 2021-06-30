def popular_words(text: str, words: list) -> dict:
    # your code here
    result = {}
    temp_2 = []
    temp_3 = []
    
    text = text.lower()
    temp_1 = text.split("\n")
    
    for i in temp_1:
        if i:
            temp_2.append(i.split(" "))


    for j in temp_2:
        for i in j:
            temp_3.append(i)

    print(temp_3)
    
    for k in words:
        lim = 0
        if k in temp_3:
            for element in temp_3:
                if element == k:
                    lim+=1
        result[k] = lim
    return result


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))
