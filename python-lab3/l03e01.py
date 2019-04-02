from sys import argv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction


MyTocken = ""


def showTasks(bot, update):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    if len(tasks) > 0:
        update.message.reply_text("\n".join(tasks))
    else:
        update.message.reply_text("No such Task!")


def newTask(bot, update, args):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    newTask = "".join(args)
    tasks.append(newTask)
    update.message.reply_text(newTask + "\n- INSERTED -")


def removeTask(bot, update, args):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    if len(tasks) > 0:
        text = "".join(args)
        if text in tasks:
            tasks.remove(text)
            update.message.reply_text(text + "\n- REMOVED -")
        else:
            update.message.reply_text(text + "\n- NOT IN TASKS -")
    else:
        update.message.reply_text("No such Task!")


def removeAllTasks(bot, update, args):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    if len(tasks) > 0:
        text = "".join(args)
        for t in tasks:
            if text in t:
                tasks.remove(t)
                update.message.reply_text(t + "\n- REMOVED -")
                f = True
        if not f:
            update.message.reply_text(text + "\n- NOT IN TASKS -")
    else:
        update.message.reply_text("No such Task!")


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

    fileName = argv[1]
    file = open(fileName, "r")
    tasks = file.read().splitlines()
    file.close()

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
