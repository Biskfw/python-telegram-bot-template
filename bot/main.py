from configuration import Config
from handlers.index import index
from telegram.ext import Application

def main():
    config = Config()

    app = Application.builder().token(config.bot_token).build()
    index(app)

    app.run_polling()

if __name__ == "__main__":
    main()
