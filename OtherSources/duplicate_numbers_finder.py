def main() -> None:
    """Function that open file to take numbers from and iterate through to find duplicates. Then writing key: value dictionary as a result to a new file."""
    
    numbers_list = []
    file_name = str(input('Input file name with .txt extension: '))

    # Work with start file
    try:
        with open(file_name, 'r') as file_1:
            # Loop through numbers to input in list numbers from .txt file
            for element in file_1:
                if element[-1] == "\n":
                    numbers_list.append(element[:-1])
                else:
                    numbers_list.append(element)
    except FileNotFoundError:
        print("File is not found. Please ensure to type the right file name.")
    
    numbers_set = set(numbers_list)

    # Work with output file
    with open("numbers_count.txt", "w") as file_2:
        # Loop through unique elements in set(number_list) to write number: count(number) in an output file
        for unique_element in numbers_set:
            line =  f"\n Number {unique_element} meets {numbers_list.count(unique_element)} times."
            file_2.write(line)


if __name__ == "__main__":
    main()