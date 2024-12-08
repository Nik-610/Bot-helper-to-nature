import telebot
from telebot import types
import requests

bot = telebot.TeleBot('7614311120:AAHTssIxJXZJRx1vHKQM8AYCtCmA0pCQkag')

# Ваш API-ключ
API_KEY = "e0950540-1f74-401e-b424-771f7556568f"

# Базовый URL API
BASE_URL = "https://api.airvisual.com/v2"

# Функция для получения данных о качестве воздуха в городе
def get_city_air_quality(city, state, country):
    url = f"{BASE_URL}/city"
    params = {
        "city": city,
        "state": state,
        "country": country,
        "key": API_KEY,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Проверяем успешность запроса
        data = response.json()
        
        if "data" in data:
            pollution = data["data"]["current"]["pollution"]
            weather = data["data"]["current"]["weather"]

            # Перевод давления в мм рт. ст.
            pressure_mm_hg = weather['pr'] * 0.75006375541921

            return (
                f"Качество воздуха в городе {city}, {state}, {country}:\n"
                f"- AQI(Индекс качества воздуха) (Россия): {pollution['aqius']}\n"
                f"- Основной загрязнитель: {pollution['mainus']}\n"
                f"- Температура: {weather['tp']}°C\n"
                f"- Давление: {pressure_mm_hg:.2f} мм рт. ст.\n"
                f"- Влажность: {weather['hu']}%"
            )
        else:
            return f"Ошибка: {data.get('message', 'Неизвестная ошибка')}"
    except requests.exceptions.RequestException as e:
        return f"Ошибка запроса: {e}"


@bot.message_handler(commands=['start'])
def qwizz(message):
    markup = types.InlineKeyboardMarkup()
    start = types.InlineKeyboardButton(text="🔍 Начать викторину", callback_data="start1")
    markup.add(start)
    bot.send_message(message.chat.id, "Привет, я бот-помощник по экологии. Чтобы начать, пройди тест на знание переработки мусора", reply_markup=markup)

# Первый вопрос 
@bot.callback_query_handler(func=lambda call: call.data == 'start1')
def q1(call):
    markup = types.InlineKeyboardMarkup()
    q1_1 = types.InlineKeyboardButton(text="1", callback_data="q1_1")
    q1_2 = types.InlineKeyboardButton(text="2", callback_data="q1_2")
    q1_3 = types.InlineKeyboardButton(text="3", callback_data="q1_3")
    markup.add(q1_1, q1_2, q1_3)
    bot.send_message(call.message.chat.id, "Первый вопрос: \nЧто, в основном, производят из переработанных пластиковых бутылок?\n\n1. Новые пластиковые бутылки\n2. Мягкие игрушки\n3. Одежду (футболки, свитера, костюма из синтетических волокон, даже спальные мешки)", reply_markup=markup)



# Первый вопрос неправилный ответ
@bot.callback_query_handler(func=lambda call: call.data == 'q1_2')
def q1_2_w(call):
    bot.send_message(call.message.chat.id, "Неправильно❌ Попробуй ещё")
    bot.register_next_step_handler(call.message, q1)



# Первый вопрос неправильный ответ
@bot.callback_query_handler(func=lambda call: call.data == 'q1_1')
def q1_3_w(call):
    bot.send_message(call.message.chat.id, "Неправильно❌ Попробуй ещё")
    bot.register_next_step_handler(call.message, q1)





# Второй вопрос
@bot.callback_query_handler(func=lambda call: call.data == 'q1_3')
def q2(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    markup = types.InlineKeyboardMarkup()
    q2_1 = types.InlineKeyboardButton(text="1", callback_data="q2_1")
    q2_2 = types.InlineKeyboardButton(text="2", callback_data="q2_2")
    q2_3 = types.InlineKeyboardButton(text="3", callback_data="q2_3")
    bot.send_message(call.message.chat.id, "Правильно✅")
    markup.add(q2_1, q2_2, q2_3)
    bot.send_message(call.message.chat.id, "Второй вопрос: \nКакой мусор считается самым распространенным (по количеству единиц) на Земле?\n\n1. Сигаретные окурки\n2. Полиэтиленовые пакеты\n3. Автомобильные покрышки", reply_markup=markup)



# Второй вопрос неправильный ответ
@bot.callback_query_handler(func=lambda call: call.data == 'q2_2')
def q2_2_w(call):
    bot.send_message(call.message.chat.id, "Неправильно❌ Попробуй ещё")
    bot.register_next_step_handler(call.message, q2)



# Второй вопрос неправилный ответ
@bot.callback_query_handler(func=lambda call: call.data == 'q2_3')
def q2_3_w(call):
    bot.send_message(call.message.chat.id, "Неправильно❌ Попробуй ещё")
    bot.register_next_step_handler(call.message, q2)





# Третий вопрос
@bot.callback_query_handler(func=lambda call: call.data == 'q2_1')
def q3(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    markup = types.InlineKeyboardMarkup()
    q3_1 = types.InlineKeyboardButton(text="1", callback_data="q3_1")
    q3_2 = types.InlineKeyboardButton(text="2", callback_data="q3_2")
    q3_3 = types.InlineKeyboardButton(text="3", callback_data="q3_3")
    bot.send_message(call.message.chat.id, "Правильно✅")
    markup.add(q3_1, q3_2, q3_3)
    bot.send_message(call.message.chat.id, "Третий вопрос: \nСколько килограммов мусора производит среднестатистический человек за год?\n\n1. 120кг\n2. 340кг \n3. 38кг", reply_markup=markup)



# Третий вопрос неправилный ответ
@bot.callback_query_handler(func=lambda call: call.data == 'q3_1')
def q3_1_w(call):
    bot.send_message(call.message.chat.id, "Неправильно❌ Попробуй ещё")
    bot.register_next_step_handler(call.message, q3)


# Третий вопрос неправилный ответ
@bot.callback_query_handler(func=lambda call: call.data == 'q3_3')
def q3_3_w(call):
    bot.send_message(call.message.chat.id, "Неправильно❌ Попробуй ещё")
    bot.register_next_step_handler(call.message, q3)

@bot.callback_query_handler(func=lambda call: call.data == 'q3_2')
def q3_2(call):
    city = "Moscow"
    state = "Moscow"
    country = "Russia"
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, "Поздравляю, Вы прошли викторину!🎉")
    bot.send_message(call.message.chat.id, "Это статистика загрязнения столицы России:")
    # Получаем данные из API
    air_quality_info = get_city_air_quality(city, state, country)
    bot.send_message(call.message.chat.id, air_quality_info)
    markup = types.InlineKeyboardMarkup()
    help_1 = types.InlineKeyboardButton(text="🍃Помочь", callback_data="help")
    markup.add(help_1)
    bot.send_message(call.message.chat.id, "Хотите помочь природе?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'help')
def helpp(call):
    bot.send_message(call.message.chat.id, "Вот несколько способов, как помочь природе:\n\n\n1. Сортировать мусор - например, старые вещи можно отдавать на благотворительность, а бумагу копить и сдавать в пункты приёма макулатуры.\n\n2. Отказаться от пластика - можно заменить обычные пакеты на многоразовые сумки-шопперы, использовать картонную одноразовую посуду, отдать предпочтение многоразовой бутылке для воды.\n\n3. Использовать правильные батарейки - химические компоненты, входящие в состав элементов питания, наносят вред окружающей среде. Батарейки нужно сдавать в специальный пункт приёма.\n\n4.Принять участие в озеленении - существует множество мероприятий по озеленению парков и скверов, в которых можно принять участие.\n\n5. Меньше пользоваться личным авто, ездить на велосипеде - не оставлять автомобиль заведённым просто так, ходить до магазина или работы пешком, хотя бы в хорошую погоду, отдавать предпочтение общественному транспорту.")
    bot.send_message(call.message.chat.id, "Если нужна будет помощь, пропиши /help\nУдачи в супергеройстве)🍀")

@bot.callback_query_handler(func=lambda call: call.data == 'help2')
def helppp(call):
    bot.send_message(call.message.chat.id, "Вот несколько способов, как помочь природе:\n\n\n1. Сортировать мусор - например, старые вещи можно отдавать на благотворительность, а бумагу копить и сдавать в пункты приёма макулатуры.\n\n2. Отказаться от пластика - можно заменить обычные пакеты на многоразовые сумки-шопперы, использовать картонную одноразовую посуду, отдать предпочтение многоразовой бутылке для воды.\n\n3. Использовать правильные батарейки - химические компоненты, входящие в состав элементов питания, наносят вред окружающей среде. Батарейки нужно сдавать в специальный пункт приёма.\n\n4.Принять участие в озеленении - существует множество мероприятий по озеленению парков и скверов, в которых можно принять участие.\n\n5. Меньше пользоваться личным авто, ездить на велосипеде - не оставлять автомобиль заведённым просто так, ходить до магазина или работы пешком, хотя бы в хорошую погоду, отдавать предпочтение общественному транспорту.")

@bot.message_handler(commands=['help'])
def hhelp(message):
    markup = types.InlineKeyboardMarkup()
    h1 = types.InlineKeyboardButton(text="1", callback_data="help2")
    h2 = types.InlineKeyboardButton(text="2", callback_data="air_quality")
    h3 = types.InlineKeyboardButton(text="3", callback_data="start1")
    markup.add(h1, h2, h3)
    bot.send_message(message.chat.id, "Здраствуйте! Чем я могу помочь?\n\n1. Узнать способы помочь природе\n2. Узнать качество воздуха в Москве\n3. Пройти викторину", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'air_quality')
def air_quality(call):
    city = "Moscow"
    state = "Moscow"
    country = "Russia"
    # Получаем данные из API
    air_quality_info = get_city_air_quality(city, state, country)
    bot.send_message(call.message.chat.id, air_quality_info)

bot.polling(none_stop=True)
print("Бот запущен...")
