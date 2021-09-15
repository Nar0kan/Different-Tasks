from jinja2 import FileSystemLoader, Environment

games = [
    {"title": "Crysis", "genre": "Shooter"},
    {"title": "osu!", "genre": "Rhytm"},
    {"title": "TES 4: Oblivion", "genre": "RPG"},
    {"title": "Flatout 2", "genre": "Racing"},
    {"title": "Minecraft", "genre": "Sandbox"},
    {"title": "Assassin's Creed", "genre": "Action"},
    {"title": "Age of Wonders 3", "genre": "Strategy"},
]

#file_loader = FileSystemLoader('templates')
env = Environment(loader = FileSystemLoader('templates'))

tm = env.get_template('index.htm')
msg = tm.render(games = games)

#I overwrote this msg variable in templates/changed_index.htm
#print(msg)

# INCLUDE function
anime_list = [
    "OnePunchMan",
    "Link Click",
    "Haikyuu!!",
    "Colorful",
    "This Hero is Invincible but 'Too Cautious'",
    "Bakuman",
    "Haven't You Heard? I'm Sakamoto",
    "Terraformars",
]

tm = env.get_template('page.htm')
msg = tm.render(domain = "myanimelist.net", title = "My anime list", anime_list = anime_list)

#I overwrote this in templates/changed_page.htm
print(msg)