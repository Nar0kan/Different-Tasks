from jinja2 import Template

members = [ {"name": "Alex", "age": 21},
            {"name": "Dora", "age": 19},
            {"name": "Casper", "age": 23},
            {"name": "Josh", "age": 18},
            {"name": "Helena", "age": 22},
            {"name": "Pixy", "age": 20}]

# Using 'for' and 'if' constructions in templates
tm = Template('''
{% for member in members -%}
{% if member.age > 20 -%}
    Name: {{member.name}}, age: {{member.age}}.
{% elif member.age < 20 -%}
    Name: {{member.name}}.
{% else -%}
    Name: {{member.name}}, age: 20, chosen one.
{% endif -%}
{% endfor -%}
''')
msg = tm.render(members = members)

print(msg)