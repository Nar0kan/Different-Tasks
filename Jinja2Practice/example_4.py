#Filters
from jinja2 import Template

data = [
    {"fruit": "lemon","price": 10.0}, 
    {"fruit": "watermelon","price": 29.0}, 
    {"fruit": "pineapple","price": 32.0}, 
    {"fruit": "apple","price": 3.5}, 
    {"fruit": "orange","price": 6.0}
]

#SUM
sum_tm = Template("Summary price of all the fruits: {{ fruits | sum(attribute = 'price') }}")
msg1 = sum_tm.render(fruits = data)

#MAX
max_tm = Template("Maximum price of all the fruits have: {{ (fruits | max(attribute = 'price')).fruit }}")
msg2 = max_tm.render(fruits = data)

#MIN + CAPITALIZE
min_tm = Template('Minimum price of all the fruits have: {{(fruits|min(attribute="price")).fruit|capitalize}}')
msg3 = min_tm.render(fruits = data)

#INT + STRING + JOIN
int_tm = Template('Int + Str + Join: {{fruits[0].price | int| string| join("_")}}')
msg4 = int_tm.render(fruits = data)

#Output
#print(msg1, msg2, msg3, msg4, sep = "\n")

# using filters as template construction {% filter filter_name %} and {% endfilter %}

class Person:
    def __init__(self, name, age, hobby = "None"):
        self.name = name
        self.age = age
        self.hobby = hobby

club_list = [
    Person("Joey", 25, "osu!"),
    Person("Matt", 20, "Starcraft 2"),
    Person("Cristy", 19, "TES"),
    Person("Jolyne", 23, "Soccer")
    ]

tpl = '''
Club members:
{% for m in cl -%}
{% filter upper -%}
    * {{ m.name }}
{% endfilter -%}
{% endfor -%}
'''

tm = Template(tpl)
msg = tm.render(cl = club_list)

print(msg)