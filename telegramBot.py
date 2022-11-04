from codecs import ignore_errors
from imaplib import Commands
from pydoc import text
import telebot
from telebot import types
import random
bot=telebot.TeleBot("5490035526:AAFdwLTw2v1rEmvd8KGZO3igArIVXdqN6EA")



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
    bot.send_message(message.chat.id,"Этот бот создан для отработки навыков, просто набора опыта, и по фану в том числе. Он в себе заключает анонимный чат, и маленький интерактив вызывающийся: Фото, Я, Привет, если так же сами скинете свою фотку он ее оценит :) ")

@bot.message_handler(commands=['Pre_start'])             #Блок комманд
def websit(message):
    mess=f'Привет {message.from_user.first_name}, пообщаемся?'
    markup =types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.InlineKeyboardButton('/VK_Developer')
    start = types.InlineKeyboardButton('/Messengers')
    stop = types.InlineKeyboardButton('/Show_Developer')
    markup.add(website, start, stop, )
    bot.send_message(message.chat.id,mess,reply_markup=markup)



@bot.message_handler(commands=['VK_Developer'])          #Ссылка на меня
def website(message):
    print(message.chat.id,message.from_user.first_name,"Запросил вашу ссылку")
    markup =types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Страница РазРаБотЧИкА!",url='https://vk.com/id734513847' ))
    bot.send_message(message.chat.id,'Перейдите на сайт!',reply_markup=markup)



All_Id=[[5421880706,0],[543427068,0] ]



@bot.message_handler(commands=['Show_Developer'])         #Для себя
def pis(message):
    print(All_Id)



@bot.message_handler(commands=['Messengers'])            #База данных
def userr(message):
    mesi =f'Ну что {message.from_user.first_name} начнем общения?'
    markup =types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    webs = types.InlineKeyboardButton('/Find_User')
    stopi = types.InlineKeyboardButton('/Back')
    markup.add(webs, stopi )
    bot.send_message(message.chat.id,mesi,reply_markup=markup)
    a = 0
    try:
        while message.chat.id != All_Id[a][0]:
            a += 1
            if message.chat.id == All_Id[a][0]:
                All_Id[a][1] = 0
                print(All_Id)
                break
    except IndexError:
        All_Id.append([message.chat.id,0])
        bot.send_message(message.chat.id,"Отлично, теперь вы в базе данных!")



@bot.message_handler(commands=['stop'])           #стопает чат и пользователь потом пассив типо;)
def stoop(message):
    markup =types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    webss = types.InlineKeyboardButton('/Find_User')
    ww = types.InlineKeyboardButton('/start')
    markup.add(webss, ww)
    a = 0
    while message.chat.id != All_Id[a][0]:
        a += 1
        print(a)
        if message.chat.id == All_Id[a][0]:
            All_Id[a][1] = 0
            print(All_Id)
            bot.send_message(message.chat.id,"Чат остановлен! Можете попробывать снова, или вернуться назад!",reply_markup=markup)
            break



@bot.message_handler(content_types=['text'])            #База данных и сам чат
def gog(message):
    if message.text == "/Find_User":
        markup =types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        webss = types.InlineKeyboardButton('/stop')
        markup.add(webss )
        bot.send_message(message.chat.id,"Пока Я ищу Вам общение, напоминаю что если хотите закончить общение нажмите стоп",reply_markup=markup)
        a = 0
        while message.chat.id != All_Id[a][0]:
            a += 1
            print(a)
            if message.chat.id == All_Id[a][0]:
                All_Id[a][1] = 1
                print(All_Id)
                break   
    try:
        vv = []
        b = 0    
        while 1 != All_Id[b][1]:
            b += 1
            if All_Id[b][0] == message.chat.id:
                break
            if 1 == All_Id[b][1]:
                vv.append(message.chat.id)
                vv.append(All_Id[b][0])
                print(vv)
                if len(vv) == 2:
                    bot.send_message(vv[0],"Собеседник присоединился! Можете общаться!")
                    bot.send_message(vv[1],"Собеседник присоединился! Можете общаться!")
                    if message.text != "/stop":
                        if message.chat.id == vv[0]:
                            print(vv[0])
                            bot.send_message(vv[1],message.text)
                        elif message.chat.id == vv[1]:
                            print(vv[1])
                            bot.send_message(vv[0],message.text)

    except IndexError:
        bot.send_message(message.chat.id,"Кажется вы одни сейчас ищете общения, не растраивайтесь, подождите немного и Я Вас с кем-нибудь свяжу;)")

            

@bot.message_handler(commands=['Back'])         #Возврат
def piss(message):
    mark =types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    ww = types.InlineKeyboardButton('/start')
    mark.add(ww)
    bot.send_message(message.chat.id,"чтобы вернуться нажмите /start",reply_markup=mark)



#@bot.message_handler(content_types=['text'])            #Интерактив
#def get_uzer_text(message):
#    if message.text == "Я":
#       bot.send_message(message.chat.id,message, parse_mode='html')
#    elif message.text == "Фото":
#        photo = open('sss.png', 'rb')
#        bot.send_photo(message.chat.id, photo)
#    elif message.text == "Привет":
#        for i in range(1):
#            a = random.randint(0,4)
#            gg = mass[a]
#            bot.send_message(message.chat.id, gg)
#    elif message.text == "Danila":
#        bot.send_message(message.chat.id,All_ID["Danila_id"])
#    elif message.text == "Bogdan":
#       bot.send_message(message.chat.id,All_ID["Bogdan_id"])
#    elif message.text == "user_id":
#        All_ID["user_id"] = message.chat.id 
#        bot.send_message(message.chat.id,All_ID["user_id"])        
#    elif message.text == "maksim":
#        bot.send_message(message.chat.id,All_ID["maksim_id"])
#    elif message.text == "Мой id":
#        bot.send_message(message.chat.id,f"Твой id:{message.from_user.id}", parse_mode='html')
#    else:
#        bot.send_message(message.chat.id,'Такой команды у нас еще нет! Может вы не верно ее ввели?')



@bot.message_handler(content_types=['photo'])               #Интерактив
def get_user_photo(message):
    bot.send_message(message.chat.id,'Прикольное фото mean!')



All_ID={            #База даных
"Danila_id": "404269833",
"Bogdan_id": "5434270608",
"maksim_id": "5421880706",
"user_id": "0"
}
mass = ["И тебе привет!","Здравствуй!","Салют!","Категорически приветствую!","Доброго времени суток!"]



bot.polling(none_stop=True)