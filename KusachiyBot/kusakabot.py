from telegram import bot, update, message, ChatPermissions, ChatMember, user, Document, File # Чтобы интелесентс подсказывал
from telegram.ext import Updater
import logging
from telegram.ext import Filters, MessageHandler, CommandHandler
from time import time
import random

master = 385730505
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
updater = Updater(token = '1169911956:AAH2Yci-RHTcFveYAK8ZJDOU6IicBPgUXdo', use_context = True)

dispatcher = updater.dispatcher

# Реакция бота на команду /start
def start(update, context):
    update.message.reply_text("Привет, я бот-кусака.\nЛюбой конфликт можно разрешить дружеским кусем, а я буду вашим верховным судьей))))0)\nТакже я являюсь полноценным администратором чатов.\nПросто добавь меня в беседу и мы познакомимся поближе!\nНашли баг? Есть вопрос? Пишите моему создателю @Starlexx")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Реакция бота на команду /help
def help(update, context):
    update.message.reply_text("Привет, на данный момент я знаю следующие команды: \n /start \n /help \n Умею кусаться, мутить и банить пользователей!\nПодробнее: \n /mute \n /ban \n /kus")

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

# Реакция бота на команду /mute
def mute(update, context):
    update.message.reply_text("Чтобы замутить пользователья, надо ответить на его сообщение: \"мут (число) (мин, ч, сут)\"\nНапример: мут 5 ч\nЧтобы размутить пользователя, надо ответить на его сообщение: \"анмут\"")

mute_handler = CommandHandler('mute', mute)
dispatcher.add_handler(mute_handler)

# Реакция бота на команду /ban
def ban(update, context):
    update.message.reply_text("Чтобы забанить пользователья, надо ответить на его сообщение: \"бан\"\nЧтобы разбанить пользователя, надо ответить на его сообщение: \"анбан\"\nЕсли разбаненный уже общался со мной, то я пришлю ему ссылку для возврата в чат")

ban_handler = CommandHandler('ban', ban)
dispatcher.add_handler(ban_handler)

# Реакция бота на команду /kus
def kus(update, context):
    update.message.reply_text("Чтобы попытаться укусить пользователья, надо ответить на его сообщение: \"кусь\"\nБудь осторожнее, ведь охотник в любой момент может стать жертвой и укусить в ответ!")

kus_handler = CommandHandler('kus', kus)
dispatcher.add_handler(kus_handler)

# Реализуем кусь, мут, бан

def bite(update, context):
    # Схватываем всех админов и помещаем в list
    admins = context.bot.get_chat_administrators(update.message.chat.id)

    # Определяем, есть ли среди отправителя и получателя админы
    sender = ChatMember(update.message.from_user.id, 'unknown')
    for i in range (0, len(admins)):
        if (sender.user == admins[i].user.id):
            sender.status = 'administrator'

    if (sender.status != 'administrator'):
        sender.status = 'member'

    recipient = ChatMember(update.effective_message.reply_to_message.from_user.id, 'unknown') 
    for i in range (0, len(admins)):
        if (recipient.user == admins[i].user.id):
            recipient.status = 'administrator'

    if (recipient.status != 'administrator'):
        recipient.status = 'member'

    # Обрабатываем сам кусь 
    if (update.effective_message.text.lower() == 'кусь'):
        # Подбрасываем монетку
        coin = random.randint(1, 100)
        file_num = random.randint(1, 5)

        # admin vs admin
        if (sender.status == recipient.status == 'administrator'):
            update.message.reply_photo(photo = open('special/love.jpg', 'rb'))
            update.message.reply_text("Воу-воу, битва админов. Я на такое не подписывался!")
            return

        # admin vs member
        if (sender.status == 'administrator' and coin % 2 == 0):
            update.message.reply_photo(photo = open('special/armored.jpg', 'rb'))
            update.message.reply_text("Админу @" + str(update.message.from_user.username) + " не удалось укусить пользователя @" + str(update.effective_message.reply_to_message.from_user.username) + "!")
            return    
        elif (recipient.status != 'administrator' and sender.status == 'administrator'):
            context.bot.restrict_chat_member(update.message.chat.id, update.effective_message.reply_to_message.from_user.id, permissions = ChatPermissions(can_send_messages = False), until_date = time() + 30)
            update.message.reply_photo(photo = open('kus\'/kus\'' + str(file_num) + '.jpg', 'rb'))
            update.message.reply_text("Админ @" + str(update.message.from_user.username) + " не оставил шансов пользователю @" + str(update.effective_message.reply_to_message.from_user.username) + "!")
            return
        
        # member vs admin
        if (recipient.status == 'administrator'):
            context.bot.restrict_chat_member(update.message.chat.id, update.message.from_user.id, permissions = ChatPermissions(can_send_messages = False), until_date = time() + 30)
            update.message.reply_photo(photo = open('antikus\'/antikus\'' + str(file_num) + '.jpg', 'rb'))
            update.message.reply_text("Слабоумие и отвага. Админ @" + str(update.effective_message.reply_to_message.from_user.username) + " даже не почувствовал пользователя @" + str(update.message.from_user.username) + " !")           
            return

        # member vs member
        if (coin % 2 == 0 and update.message.from_user):
            context.bot.restrict_chat_member(update.message.chat.id, update.message.from_user.id, permissions = ChatPermissions(can_send_messages = False), until_date=time() + 30)
            update.message.reply_photo(photo = open('antikus\'/antikus\'' + str(file_num) + '.jpg', 'rb'))
            update.message.reply_text("Пользователь  @" + str(update.message.from_user.username) + " попробовал укусить @" + str(update.effective_message.reply_to_message.from_user.username) + ", но тот увернулся и нанес антикусь!")
        else:
            context.bot.restrict_chat_member(update.message.chat.id, update.effective_message.reply_to_message.from_user.id, permissions = ChatPermissions(can_send_messages = False), until_date = time() + 30)
            update.message.reply_photo(photo = open('kus\'/kus\'' + str(file_num) + '.jpg', 'rb'))
            update.message.reply_text("Пользователь  @" + str(update.message.from_user.username) + " кусил @" + str(update.effective_message.reply_to_message.from_user.username) + "!")
    
    # Реализуем мут
    st = update.effective_message.text.lower()
    s = st.split()

    if (s[0] == 'мут' and (sender.status == 'administrator' or sender.user == master) and recipient.status !='administrator' and recipient.user != master):
        try:
            t = int(s[1])
            if (s[2] == 'мин'): t = t * 60
            elif(s[2] == 'ч'): t = t * 3600
            elif(s[2] == 'cут'): t = t * 3600 * 24
        except:
            update.message.reply_text("Укажи правильно время мута, котик!")
            return
        context.bot.restrict_chat_member(update.message.chat.id, update.effective_message.reply_to_message.from_user.id, permissions = ChatPermissions(can_send_messages = False), until_date = time() + t)
        update.message.reply_text("@" + str(update.effective_message.reply_to_message.from_user.username) + " получил мут на " + s[1] + " " + s[2] + "!")
    elif (s[0] == 'мут' and sender.status == recipient.status == 'administrator'):
            update.message.reply_text("Воу-воу, битва админов. Я на такое не подписывался!")
    elif (s[0] == 'мут' and recipient.user == master):
        update.message.reply_photo(photo = open('special/shield.jpg', 'rb'))
        update.message.reply_text("РРРРРРРРРРРРРРР! За что ты так с моим хозяином?!")
    elif (s[0] == 'мут'):
        update.message.reply_text("Котик, не обманывай меня, ты не админ!")

    # Обрабатываем анмут 
    if (update.effective_message.text.lower() == 'анмут' and (sender.status == 'administrator' or sender.user == master) and recipient.status !='administrator' and recipient.user != master):
        context.bot.restrict_chat_member(update.message.chat.id, update.effective_message.reply_to_message.from_user.id, permissions = ChatPermissions(can_send_messages = True), until_date = 0)
        update.message.reply_text("@" + str(update.effective_message.reply_to_message.from_user.username) + " вновь может писать!")    
    elif (update.effective_message.text.lower() == 'анмут' and sender.status == recipient.status == 'administrator'):
            update.message.reply_text("Воу-воу, битва админов. Я на такое не подписывался!")
    elif (update.effective_message.text.lower() == 'анмут'):
        update.message.reply_text("Котик, не обманывай меня, ты не админ!")

    # Обрабатываем бан 
    if (update.effective_message.text.lower() == 'бан' and (sender.status == 'administrator' or sender.user == master) and recipient.status !='administrator' and recipient.user != master):
        context.bot.kick_chat_member(update.message.chat.id, update.effective_message.reply_to_message.from_user.id, until_date = 0)
        update.message.reply_text("@" + str(update.effective_message.reply_to_message.from_user.username) + " получил бан!(")
    elif (update.effective_message.text.lower() == 'бан' and sender.status == recipient.status == 'administrator'):
            update.message.reply_text("Воу-воу, битва админов. Я на такое не подписывался!")
    elif (update.effective_message.text.lower() == 'бан' and recipient.user == master):
        update.message.reply_photo(photo = open('special/shield.jpg', 'rb'))
        update.message.reply_text("РРРРРРРРРРРРРРР! За что ты так с моим хозяином?!")
    elif (update.effective_message.text.lower() == 'бан'):
        update.message.reply_text("Котик, не обманывай меня, ты не админ!")

    # Обрабатываем анбан
    if (update.effective_message.text.lower() == 'анбан' and (sender.status == 'administrator' or sender.user == master) and recipient.status !='administrator' and recipient.user != master):
        context.bot.unban_chat_member(update.message.chat.id, update.effective_message.reply_to_message.from_user.id, until_date = 0)
        update.message.reply_text("@" + str(update.effective_message.reply_to_message.from_user.username) + " был разбанен!)")
        link = context.bot.export_chat_invite_link(update.message.chat.id)
        context.bot.send_message(update.effective_message.reply_to_message.from_user.id, "Котик, тебя разбанили! Ссылка для возврата в чат:" + link)
    elif (update.effective_message.text.lower() == 'анбан' and sender.status == recipient.status == 'administrator'):
            update.message.reply_text("Воу-воу, битва админов. Я на такое не подписывался!")
    elif (update.effective_message.text.lower() == 'анбан' and recipient.user == master):
        update.message.reply_photo(photo = open('special/shield.jpg', 'rb'))
        update.message.reply_text("РРРРРРРРРРРРРРР! За что ты так с моим хозяином?!")
    elif (update.effective_message.text.lower() == 'анбан'):
        update.message.reply_text("Котик, не обманывай меня, ты не админ!")
bite_handler = MessageHandler(Filters.reply, bite)
dispatcher.add_handler(bite_handler)

updater.start_polling()
updater.idle()