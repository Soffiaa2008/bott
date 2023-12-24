import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def start(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "/ban - бан пользователя, /go - создай покемона")

@bot.message_handler(commands=['ban']) 
def ban_user(message):
    global banned_users
    if message.reply_to_message:
        chat_id=message.chat.id
        user_id=message.reply_to_message.from_used.id
        user_status=bot.get_chat_member(chat_id,user_id).status
        if user_status == "administrator" or user_status == 'creator':
            bot.reply_to(message,"невозможно забанить админа!")
        else:
            try:
                with open("banned_users.txt","r") as file:
                    banned_users=file.read().splitlines()
            except FileNotFoundError:
                with open('banned_users.txt','w') as file:
                    file.write('')
            user_name=message.reply_to_message.from_user.username
            bot.ban_chat_member(chat_id, user_id)
            if user_name not in banned_users:
                with open('banned_users.txt','a') as file:
                    file.write(user_name + '\n')
                bot.reply_to(
                    message, f'пользователь @{user_name} был забанен'
                )
            else:
                bot.reply_to(
                    message, f'пользователь @{user_name} уже забанен'
                )
    else:
        bot.reply_to(
            message, "эта команда должна быть использована в ответ на соо пользователя, которого вы хотите забанить"
        )


@bot.message_handler(commands=['sr'])
def sr(message):
    if message.reply_to_message:
        if pokemon1 > pokemon2:
        pass
        elif pokemon1 < pokemon2:
            pass
        else: # если равны
            pass





bot.infinity_polling(none_stop=True)

