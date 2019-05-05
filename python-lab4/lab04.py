from sys import argv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction
import pymysql

MySQLpassword = "root"
MyTocken = "805046786:AAHo3KxnawJv-w4ePjSxt0ORYZWdfAOZGoY"

def showTasks(bot, update):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    select = "select * from tasks order by todo asc "
    cursor.execute(select)
    tuples = []
    for i in cursor.fetchall():
        tuples.append(i[1])
    if len(tuples) > 0:
        update.message.reply_text("\n".join(tuples))
    else:
        update.message.reply_text("No such Task!")


def newTask(bot, update, args):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    newTask = " ".join(args)
    cursor.execute(insert, (newTask, True, ))
    connection.commit()
    update.message.reply_text(newTask + "\n- INSERTED -")


def removeTask(bot, update, args):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    select = "select * from tasks where todo=(%s)"
    delete = "delete from tasks where todo=(%s)"
    text = " ".join(args)
    if cursor.execute(select, (text,)):
        cursor.execute(delete, (text,))
        connection.commit()
        update.message.reply_text(text + "\n- REMOVED -")
    else:
        update.message.reply_text(text + "\n- NOT IN TASKS -")


def removeAllTasks(bot, update, args):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    text = " ".join(args)
    select = "select * from tasks where todo like (%s)"
    delete = "delete from tasks where todo like (%s)"
    cursor.execute(select, ("%" + text + "%",))
    tuples = []
    for t in cursor.fetchall():
        tuples.append(t[1])
    if len(tuples) > 0:
        cursor.execute(delete, ("%" + text + "%",))
        connection.commit()
        update.message.reply_text("\n".join(tuples) + "\n- REMOVED -")
    else:
        update.message.reply_text(text + "\n- NOT IN TASKS -")


def start(bot, update):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    update.message.reply_text("Insert the command corresponding to the action you want to perform:\n\
/showTasks\n\
/newTask <task to add>\n\
/removeTask <task to remove>\n\
/removeAllTasks <substring to use to remove all the tasks that contain it>")


def echoError(bot, update):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    update.message.reply_text("I'm sorry, I can't do that.")


if __name__ == "__main__":

    file = open(argv[1], "r")
    tasks = file.read().splitlines()
    file.close()

    connection = pymysql.connect(user='root', password=MySQLpassword, host='localhost', database='task_list')
    cursor = connection.cursor()
    delete = "delete from tasks"
    cursor.execute(delete)
    insert = "insert into tasks(todo, urgent) values (%s, %s)"
    for t in tasks:
        cursor.execute(insert, (t, True, ))
    connection.commit()

    updater = Updater(token=MyTocken)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("showTasks", showTasks))
    dp.add_handler(CommandHandler("newTask", newTask, pass_args=True))
    dp.add_handler(CommandHandler("removeTask", removeTask, pass_args=True))
    dp.add_handler(CommandHandler("removeAllTasks", removeAllTasks, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, echoError))

    updater.start_polling()

    updater.idle()

    cursor.close()
    connection.close()