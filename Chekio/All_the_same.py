def is_all_the_same(elements: list) -> bool:
    """
        Check if elements are all the same in list. If it's so - return True,
        else return False. Also return True if list consist of no elements or only one element.
    """
    if elements:
        first_element = elements[0]
        for element in elements:
            if first_element != element:
                return False
        return True
    else:
        return True

if __name__ == "__main__":
    print(is_all_the_same(['a', 'a', 'ab']))   # return False
    print(is_all_the_same(['amogus', 'amogus']))    # return True
    print(is_all_the_same([2])) # return True
    print(is_all_the_same([]))  # return True