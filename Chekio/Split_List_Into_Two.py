def split_list(items: list) -> list:
    """
        Split list into two separate lists inside itself. When size is odd number - left side is bigger on one.
    """
    if len(items) % 2 == 0:
        return [items[:int(len(items)/2)], items[int(len(items)/2):]]
    else:
        return [items[:int(len(items)/2)+1], items[1+int(len(items)/2):]]

if __name__ == "__main__":
    print(split_list([1, 2, 3, 4, 5, 6, 7]))    # [[1, 2, 3, 4], [5, 6, 7]]
    print(split_list([1, 2, 3, 4, 5, 6]))   # [[1, 2, 3], [4, 5, 6]]
    print(split_list([1]))  # [[1], []]
    print(split_list([]))   # [[], []]