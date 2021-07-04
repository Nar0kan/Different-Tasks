def all_the_same(elements):
    if elements:
        k = elements[0]
        for el in elements:
            if k != el:
                return False
        return True
    else:
        return True

print(all_the_same(['a', 'a', 'ab']), all_the_same([2]), all_the_same([]))
