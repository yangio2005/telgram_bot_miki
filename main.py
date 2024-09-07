from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Xin chào {update.effective_user.first_name}. Chúc {update.effective_user.first_name} một ngày tốt lành! 😊 ')


app = ApplicationBuilder().token("7384027524:AAHgL6Dz5rFOATYFrJLDkzt8vfvrfNj1AfM").build()


app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("news", news))
app.run_polling()
