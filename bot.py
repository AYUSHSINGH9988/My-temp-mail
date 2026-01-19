import telebot
import os

# PASTE YOUR TOKEN BELOW inside the quotes
TOKEN = "7954674228:AAFx2cc1tqEqglt7brxKkUOa_lcxodsiIJo"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I was deployed via GitHub!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

print("Bot started...")
bot.infinity_polling()
