def frequency_sort(items: list) -> list:
    """
        Sort elements in list by their frequency and output all of them in that order.
    """
    result = []
    temp_dict = {}
    for item in items:
        temp_dict[item] = items.count(item)
    sorted_dict = sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)
    for element in sorted_dict:
        for j in range(element[1]):
            result.append(element[0])
    return result

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([9, 0, 4, 6, 2, 2, 6, 4, 4, 4, 0])) # [4, 4, 4, 4, 0, 0, 6, 6, 2, 2, 9]
    print(frequency_sort([3, 2, 3, 3, 2, 8, 6, 4, 4, 1, 1])) # [3, 3, 3, 2, 2, 4, 4, 1, 1, 8, 6]