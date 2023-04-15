
from imaplib import Commands
from pydoc import text
import telebot
from telebot import types
import psycopg2
from user_id import host, user, db_name, password
import random
bot=telebot.TeleBot("5490035526:AAFdwLTw2v1rEmvd8KGZO3igArIVXdqN6EA")



try:
    connection = psycopg2.connect(
        host=host,
        password=password,
        user=user,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version; {cursor.fetchone()}")
        cursor.execute(""f'SELECT second_id FROM users_id WHERE first_id = {5434270608}::TEXT;'"")
        record = cursor.fetchall()
        print(record)
        cursor.execute("SELECT * from users_id")
        print("Результат", cursor.fetchall())
except Exception as _ex:
    print(_ex)



@bot.message_handler(commands=['start'])             #Блок комманд
def wesit(message):
    mess=f'Привет {message.from_user.first_name}, пообщаемся?'
    markup =types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.InlineKeyboardButton('/VK_Developer')
    start = types.InlineKeyboardButton('/Messengers')
    startt = types.InlineKeyboardButton('/Help')
    stop = types.InlineKeyboardButton('/Show_Developer')
    markup.add(website, start, stop, startt)
    bot.send_message(message.chat.id,mess,reply_markup=markup)



@bot.message_handler(commands=['Help'])             #Блок комманд
def wesiit(message):
    bot.send_message(message.chat.id,"Этот бот создан для отработки навыков, просто набора опыта, и по фану в том числе. Он в себе заключает анонимный чат, если так же сами скинете свою фотку он ее оценит :) ")



@bot.message_handler(commands=['VK_Developer'])          #Ссылка на меня
def website(message):
    print(message.chat.id,message.from_user.first_name,"Запросил вашу ссылку")
    markup =types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Страница РазРаБотЧИкА!",url='https://vk.com/id734513847' ))
    bot.send_message(message.chat.id,'Перейдите на сайт!',reply_markup=markup)



interlocutors = {}
searchers = []



@bot.message_handler(commands=['Show_Developer'])         #Для себя
def pis(message):
    print()



@bot.message_handler(commands=['Messengers'])            #База данных
def userr(message):
    mesi =f'Ну что {message.from_user.first_name} начнем общения?'
    markup =types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    webs = types.InlineKeyboardButton('/Find_User')
    stopi = types.InlineKeyboardButton('/start')
    markup.add(webs, stopi )
    bot.send_message(message.chat.id,mesi,reply_markup=markup)
  
first_users = 0
second_users = 0

@bot.message_handler(commands=['stop'])            #stoping procces
def goga(message):
    if message.text == "/stop":
        print(7)
        try:
            connection = psycopg2.connect(
            host=host,
            password=password,
            user=user,
            database=db_name
            )
            connection.autocommit = True
            with connection.cursor() as cursor:
                try:
                    global second_users, first_users
                    cursor.execute(""f'SELECT second_id FROM users_id WHERE first_id = {message.chat.id}::text;'"")
                    first_users = cursor.fetchall()
                    first_users = first_users[0][0]
                    print(f'[INFO] Добавлен первый айди {first_users[0][0]}')
                    delete_query_1 = ""f'Delete from users_id where first_id = {message.chat.id}::text;'""
                    cursor.execute(delete_query_1)
                    connection.commit()
                    second_users = message.chat.id
                    print(f'[INFO] Добавлен второй айди {second_users}')
                    print("[INFO] Первое айди в первой связке успешно удалено")
                except IndexError:
                    print("[INFO] В таблице не найдено значение первого айди в первой связке")
                try:
                    delete_query_2 = ""f'Delete from users_id where second_id = {second_users}::text;'""
                    cursor.execute(delete_query_2)
                    connection.commit()
                    print("[INFO] Второе айди в первой связке успешно удалено")
                except IndexError:
                    print("[INFO] В таблице не найдено значение второго айди в первой связке")
                try:
                    delete_query_3 = ""f'Delete from users_id where first_id = {message.chat.id}::text;'""
                    cursor.execute(delete_query_3)
                    connection.commit()
                    print("[INFO] Первое айди во второй связке успешно удалено")
                except IndexError:
                    print("[INFO] В таблице не найдено значение первого айди во второй связке")
                try:
                    delete_query_4 = ""f'Delete from users_id where second_id = {second_users}::text;'""
                    cursor.execute(delete_query_4)
                    connection.commit()
                    print("[INFO] Второе айди во второй связке успешно удалено")
                    if message.chat.id == second_users:
                        bot.send_message(message.chat.id,"Собеседник отключен, можете продолжить общение или закончить его на данный момент") 
                        bot.send_message(str(first_users),"Собеседник отключился, можете продолжить общение или закончить его на данный момент")
                    else:
                        bot.send_message(message.chat.id,"Собеседник отключен, можете продолжить общение или закончить его на данный момент") 
                        bot.send_message(second_users,"Собеседник отключился, можете продолжить общение или закончить его на данный момент")
                    second_users = 0
                    print("[INFO] Айдишник успешно удален:)")
                except IndexError:
                    print("[INFO] В таблице не найдено значение второго айди во второй связке")

            mesi =f'Ну что {message.from_user.first_name} начнем общения?'
            markup =types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            webs = types.InlineKeyboardButton('/Find_User')
            stopi = types.InlineKeyboardButton('/start')
            markup.add(webs, stopi )
            bot.send_message(message.chat.id,mesi,reply_markup=markup)
        except KeyError:
            mesi =f'Ну что {message.from_user.first_name} начнем общения?'
            markup =types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            webs = types.InlineKeyboardButton('/Find_User')
            stopi = types.InlineKeyboardButton('/start')
            markup.add(webs, stopi )
            bot.send_message(message.chat.id,mesi,reply_markup=markup)
            bot.send_message(message.chat.id,"Мы еще вас ни с кем не соединяли")



@bot.message_handler(commands=['Find_User'])            #База данных и сам чат
def gog(message):
    connection.autocommit = True
    if message.text == "/Find_User":
        markup =types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        webss = types.InlineKeyboardButton('/stop')
        markup.add(webss )
        bot.send_message(message.chat.id,"Пока Я ищу Вам общение, напоминаю что если хотите закончить общение нажмите стоп",reply_markup=markup)
        searchers.append(message.chat.id)
        print("Searchers", searchers)
        online_chats_for_me = searchers.copy()
        online_chats_for_me.remove(message.chat.id)

        print("Online", online_chats_for_me)
        print("Searchers", searchers)
        
        if len(online_chats_for_me) == 0:
            bot.send_message(message.chat.id,"Кажется вы одни сейчас ищете общения, не растраивайтесь, подождите и возможно кто-то да присоединится ;)")
            return

        with connection.cursor() as cursor:
            interlocutor = random.choice(online_chats_for_me)
            cursor.execute(
        ""f'INSERT INTO users_id(first_id, second_id) VALUES({interlocutor}, {message.chat.id});'""
        )
            cursor.execute(
        ""f'INSERT INTO users_id(first_id, second_id) VALUES({message.chat.id}, {interlocutor});'""
        )
        bot.send_message(interlocutor,"Собеседник присоединился! Можете общаться!")
        bot.send_message(message.chat.id,"Собеседник присоединился! Можете общаться!")
        searchers.remove(interlocutor)
        searchers.remove(message.chat.id)
    


@bot.message_handler(content_types=['text'])  
def private_message(message):
    try:
        connection = psycopg2.connect(
        host=host,
        password=password,
        user=user,
        database=db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(""f'SELECT second_id FROM users_id WHERE first_id = {message.chat.id}::text;'"")
            record = cursor.fetchall()
            cursor.execute("SELECT * from users_id")
            print(f'{message.chat.id} написал {record[0][0]}')

            bot.send_message(int(record[0][0]), message.text)
    except:
        print("[INFO] Произошла ошибка в одной из строки кода с 190 по 208, или у отправителя нет принимающего")



@bot.message_handler(content_types=['photo'])               #Интерактив
def get_user_photo(message):
    bot.send_message(message.chat.id,'Прикольное фото mean!')



All_ID={            #База даных
"Danila_id": "404269833",
"Bogdan_id": "5434270608",
"maksim_id": "5421880706",
"user_id": "0"
}

bot.polling(none_stop=True)