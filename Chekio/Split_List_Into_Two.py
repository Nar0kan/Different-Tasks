def split_list(items: list) -> list:
    if len(items) % 2 == 0:
        return [items[:int(len(items)/2)], items[int(len(items)/2):]]
    else:
        return [items[:int(len(items)/2)+1], items[1+int(len(items)/2):]]

print(split_list([1, 2, 3, 4, 5, 6, 7]))
