import api
import telebot

bot = telebot.TeleBot('7909019197:AAEIreUNQ5JwwoMh67VjauYPBuiwjdwhSMI')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "درود مقدار و اسم ارز خودتو برام بفرست تا قیمتشو بهت بگم. مثال: 100not ")


@bot.message_handler(func=lambda message: True)
def crypto(message):
    crypto_name = message.text.lower().strip().replace(' ', '')
    print(crypto_name)
    number, letter = api.extract_numbers(crypto_name)
    if letter in api.crypto_dict.keys():
        crypto_price = api.value_price(crypto_name)
        bot.send_message(message.chat.id, crypto_price)
    else:
        bot.send_message(message.chat.id, "اشتباه! لطفا دوباره وارد کنید. مثال:  100not")


bot.polling()

