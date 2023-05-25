import telegram.ext

TOKEN="5870357601:AAGySmIthzxWxlJ5qHj2TPp3Raun7n-wPRk"

updater=telegram.ext.Updater(TOKEN)
dispatcher=updater.dispacher

def start(update,context):
    update.message.reply_text("Welcome!")

def help(update,context):
    update.message.reply_text(
        """
        /start -> starts the bot
        /help -> this message
        /upload -> uploads the specified document
        /download -> downloads the file with specified ID
        /playlist -> provides links to specified subject's YouTube playlists
        /contact -> provides the bot creator's contact details
        """
        )

def content(update,content):
    update.message.reply_text("SAMPLE TEXT")

def upload():
    pass

def download():
    pass

def playlist():
    pass

def contact():
    update.message.reply_text("Bot creator's telegram username:@albin_s_philip")

dispatcher.add_handler(telegram.ext.CommandHandler("start",start))
dispatcher.add_handler(telegram.ext.CommandHandler("help",help))
dispatcher.add_handler(telegram.ext.CommandHandler("upload",upload))
dispatcher.add_handler(telegram.ext.CommandHandler("download",download))
dispatcher.add_handler(telegram.ext.CommandHandler("playlist",playlist))
dispatcher.add_handler(telegram.ext.CommandHandler("contact",contact))

updater.start_polling()
updater.idle()


