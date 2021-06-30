from functools import reduce
# Use map to print the square of each numbers rounded
# to two decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]
# Fix all three respectively.
map_result = list(map(lambda x: round(x*x, 3), my_floats))
filter_result = list(filter(lambda name: len(name) <=7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)
print(map_result)
print(filter_result)
print(reduce_result)
#test_output_contains("[18.922, 37.088, 10.562, 95.453, 4.666, 78.854, 21.068]")
#test_output_contains("['olumide', 'josiah', 'omoseun']")
#test_output_contains("24840")
#success_msg("Congrats! Nice work.")
