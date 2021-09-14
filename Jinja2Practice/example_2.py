# Using escape (for HTML good looking text)
from jinja2 import escape

link = '''In HTML-docs links are presented by such piece of code:
<a href="#">Link</a>'''

msg = escape(link)

print(msg, end = '\n\n\n')

# More laborious and time consuming method
from jinja2 import Template

link = '''In HTML-docs links are presented by such piece of code:
<a href="#">Link</a>'''

tm = Template("{{ l |e}}")
msg = tm.render(l = link)

print(msg)