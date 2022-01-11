def frequency_sort(items: list) -> list:
    """
        Sort elements in list by their frequency.
    """
    items_set = set(items)
    frequency_dict = {}
    for element in items_set:   # Looping through set that contain unique elements from items list
        frequency_dict[element] = items.count(element)  # In frequency dict we writing key-value pairs as items.element: items.count(element) but for unique one's only
    sorted_dict = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)  # Sorting frequency_dict by DESC values and saving it as sorted_dict
    items = []
    for key, value in sorted_dict:
        items.append(key)
    return items

if __name__ == '__main__':
    print("Example: ")
    print(frequency_sort([4,6,2,2,2,6,4,4,4]))  # [4, 2, 6]
    print(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']))    # ['bob', 'carl', 'alex'] or [['bob', 'alex', 'carl']]
    print(frequency_sort([]))   # []
    print(frequency_sort([1]))  # [1]