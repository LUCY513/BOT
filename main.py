from second import weather_token
import telebot
import requests
import datetime
 
 
bot = telebot.TeleBot('5551299595:AAEXEga6GkltbmM13S8DU5t8FypvJ48dfsA')
@bot.message_handler(commands=['start'])
def start(message):
    answer = f'Hello, {message.from_user.first_name} {message.from_user.last_name}.\n' \
             f'Enter the name of the city, please love.'
    bot.send_message(message.chat.id, answer, parse_mode='html')
 
@bot.message_handler()
def get_weather(message):
    try:
        data = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric')
        result = data.json()
 
        town = result['name']  # type(result) - словарь, по этому мы можем обраться к конкретному ключу для получения данных
        temperature = result['main']['temp']
        pressure = result['main']['pressure']
        wind = result['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(result['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(result['sys']['sunset'])
 
        bot.send_message(message.chat.id, f'Town: {town}\nTemperature: {temperature}C°\n'
                                          f'Pressure: {pressure} mm Hg\nWind speed: {wind} m/s\n'
                                          f'Sunrise time: {sunrise}\nSunset time: {sunset}\n'
                                          f'Have a nice day :) ', parse_mode='html')
 
    except:
        bot.send_message(message.chat.id, 'Error, enter the correct name of the city in lowercase, please.', parse_mode='html')
 
bot.polling(none_stop=True)