import re

""" with re.findall() method you can loop through string variable as second function argument to find and output
the needed variables, written as first argument.
"""

text_1 = "He spelled some compliments about her #00FF00 eye color"

search_1 = re.findall("\\bher\\b", text_1)      # r"\bher\b" | - will output spaced chars
#print(search_1)

search_2 = re.findall("me", text_1)
#print(search_2)

search_3 = re.findall("[a-zA-Z]", text_1)       # this will output all alphabet chars in text_1
#print(search_3)

search_4 = re.findall(".", text_1)       # this will output all text_1 chars with spaces
#print(search_4)

search_5 = re.findall("[^ a-zA-Z]", text_1)       # this will output none alphabet and space chars in text_1
#print(search_5)

search_6 = re.findall("[0-9]", text_1)       # this will output all the single digits chars in text_1
print(search_6)

search_7 = re.findall("[0-9][0-9]", text_1)       # this will output all the double numbers chars in text_1
print(search_7)