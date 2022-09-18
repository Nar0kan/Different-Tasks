import telebot                      # External telegram bot library
from passGen import Password        # Internal Password class taken from passGen.py file
with open('TOKEN.log', 'r') as t:
    TOKEN = ''.join(t.readlines())

# Initializaation of the BOT by his token
bot = telebot.TeleBot(TOKEN)


# start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """The function to welcome new user."""
    reply = 'Hello, I am Loki BOT. Created to generate passwords for you.'
    bot.reply_to(message, reply)


# help command
@bot.message_handler(commands=['help'])
def send_help(message):
    """The function to send brief supportive info."""
    reply = """
            /gen len=16 alp=abc dig=123 req=123 - generate new password, where:
            \n\tlen - length of the password (optional, default - 16) - int
            \n\talp - alphabet (optional) - str
            \n\tdig - digits (optional) - str
            \n\treq - required symbols to be surely used (optional) - str
            """
    bot.reply_to(message, reply)


# Handle message
@bot.message_handler(func=lambda message: True)
def simple_handler(message):
    """Main message handler"""
    if message.text[:4] == '/gen':
        args_list = str(message.text[5:]).split()

        for i in range(len(args_list)):
            args_list[i] = args_list[i].split('=')

        ARGS = {'len': 16, 'alp': "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:\"'/?>,.<][}{|\\", \
                    'dig': "0123456789", 'req': ""}

        for arg in args_list:
            key = arg[0]
            new_value = arg[1]

            if key and new_value:
                ARGS[key] = str(new_value)
        
        PASSWORD = Password(ARGS)
        bot.send_message(message.from_user.id, PASSWORD.generate())
    else:
        bot.reply_to(message, '...')


if __name__ == "__main__":
    bot.infinity_polling()