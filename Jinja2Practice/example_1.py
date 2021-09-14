from jinja2 import Template

name_var = "Jonathan"
age_var = "28"

# Creating Template and rendering
tm = Template("Hello, this is {{ name }} and i'm {{ age }} years old.")
msg1 = tm.render(name = name_var, age = age_var)


# Simple f-strings compare
msg2 = f"Hello, this is {name_var} and i'm {age_var} years old."

# Output 1
print(msg1, msg2, sep = '\n', end = '\n\n classes\n')

# Working with classes
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

person_1 = Person("Mike", 16)
person_2 = Person("Linda", 25)

tm1 = Template("Hello, {{ p1.get_name() }} this is {{ p2.get_name() }}.")
msg1 = tm1.render(p1 = person_1, p2 = person_2)

# Output 2
print(msg1)