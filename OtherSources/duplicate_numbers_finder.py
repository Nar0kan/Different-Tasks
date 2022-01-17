def main() -> None:
    """Function that open file to take numbers from and iterate through to find duplicates. Then writing key: value dictionary as a result to a new file."""
    
    numbers_list = []
    file_name = str(input('Input file name with .txt extension: '))

    # Work with start file
    try:
        file_1 = open(file_name, 'r')
        # Loop through numbers to input in list numbers from .txt file
        for element in file_1:
            if element[-1] == "\n":
                numbers_list.append(element[:-1])
            else:
                numbers_list.append(element)
    except FileNotFoundError:
        print("File is not found. Please ensure to type the right file name.")
    finally:
        file_1.close()
    
    numbers_set = set(numbers_list)

    # Work with output file
    file_2 = open("numbers_count.txt", "w")
    # Loop through unique elements in set(number_list) to write number: count(number) in an output file
    for unique_element in numbers_set:
        line =  f"\n Number {unique_element} meets {numbers_list.count(unique_element)} times."
        file_2.write(line)

    file_2.close()


if __name__ == "__main__":
    main()