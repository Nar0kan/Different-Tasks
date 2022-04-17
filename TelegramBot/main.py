import telebot              # External telegram bot library
from user import User       # Internal User class from user.py

# Initialize bot by his token
bot = telebot.TeleBot('Token')


# Specified commands handler
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Function to send brief info."""
    bot.reply_to(message, "Hello, this is test Loki BOT. Um... Say hello to him first please, he's kinda shy BOT.")


# Handle message with reversing it and send it back
@bot.message_handler(func=lambda message: True)
def simple_handler(message):
    """Main message handler. Try /reg or /log to sign in account."""
    if message.text.lower() in ('hey', 'hello', 'hi'):
        reply_text = "Hey, what's up?"
        bot.reply_to(message, reply_text)
        return None
    
    if message.text == "/reg" or message.text == "/register":
        bot.send_message(message.from_user.id, "To register write down your login.")
        bot.register_next_step_handler(message, register_login)
    
    if message.text == "/log" or message.text == "/log_in":
        bot.send_message(message.from_user.id, "To log in write down your login.")
        bot.register_next_step_handler(message, sign_up_login)


# SIGN UP
def sign_up_login(message):
    global login
    login = message.text

    if User.is_login_available(login):
        bot.send_message(message.from_user.id, f"This login is free. Please, try again.")
        bot.register_next_step_handler(message, sign_up_login)
    else:
        bot.send_message(message.from_user.id, "Your password please.")
        bot.register_next_step_handler(message, log_in_password)


def log_in_password(message):
    password = message.text

    if User.check_user_in_database(login, password):
        password = "********"
        bot.send_message(message.from_user.id, f"Welcome back, {login}!")
    else:
        bot.send_message(message.from_user.id, f"This password is incorrect. Try again!")
        bot.register_next_step_handler(message, log_in_password)


# REGISTER
def register_login(message):
    global login
    login = message.text
    
    if not User.is_login_available(login):
        bot.send_message(message.from_user.id, f"This login is already taken. Please, try another one.")
        bot.register_next_step_handler(message, register_login)
    else:
        bot.send_message(message.from_user.id, "Your password please.")
        bot.register_next_step_handler(message, register_password)


def register_password(message):
    password = message.text

    if not User.check_user_in_database(login, password):
        global new_user
        new_user = User(login, password)
        password = "********"
        new_user.register_in_database()
        bot.send_message(message.from_user.id, f"Welcome, {login}. How can I call you?")
        bot.register_next_step_handler(message, change_profile_nickname)


def change_profile_nickname(message):
    nickname = message.txt
    new_user.set_profile_nickname(nickname)
    bot.send_message(message.from_user.id, f"Hey, {nickname}, what's about your age? Being confidential is not appreciated in China...")
    bot.register_next_step_handler(message, change_profile_nickname)


if __name__ == "__main__":
    bot.infinity_polling()