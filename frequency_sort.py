def frequency_sort(items):
    # your code here
    global limit
    limit = 0
    result = []
    res = []
    def again(items, result):
        global limit
        for i in items:
            temp = items.count(i)
            limit = max(temp, limit)
        
        for j in items:
            if items.count(j) == limit:
                for i in range(limit):
                    result.append(j)
                del j
                break
            
    for i in range(len(set(items))):
        again(items, result)
    return result


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4,6,2,2,2,6,4,4,4]))
    print(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']))
    print(frequency_sort([]))
    print(frequency_sort([1]))
