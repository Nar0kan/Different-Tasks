def frequency_sort(items):
    # your code here
    res = []
    temp_dict = {}
    for i in items:
        temp_dict[i] = items.count(i)
    temp = sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)
    for el in temp:
        for j in range(el[1]):
            res.append(el[0])
    return res
if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([9, 0, 4, 6, 2, 2, 6, 4, 4, 4, 0]))
