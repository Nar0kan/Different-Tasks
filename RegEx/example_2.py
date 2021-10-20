import re

""" This file will represent major, minor and other quantificators in re with findall function"""

#major form
text_1 = "Google, Gooogle, Goooooogle"
match_1 = re.findall(r"o{2,5}", text_1)
#print(match_1)

#minor form
match_2 = re.findall(r"o{2,5}?", text_1)
#print(match_2)


"""short forms"""

match_3 = re.findall(r"o{2,}", text_1)
#print(match_3)

match_4 = re.findall(r"Go{,3}gle", text_1)
#print(match_4)

match_5 = re.findall(r"o{2}", text_1)
#print(match_5)


# also \d, \ and some other commands may be used with quants
text_2 = "380631212123"

match_6 = re.findall("380\d{9}", text_2)
print(match_6)