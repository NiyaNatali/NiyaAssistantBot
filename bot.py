import os
import telebot
from telebot import types
from datetime import datetime

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет! Я Niya, твой ассистент.")

@bot.message_handler(func=lambda message: True)
def echo_handler(message):
    bot.send_message(message.chat.id, f"Ты сказал: {message.text}")

bot.infinity_polling()
