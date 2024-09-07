from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes



async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Xin chào {update.effective_user.full_name}. Chúc {update.effective_user.full_name} một ngày tốt lành! 😊 ')
async def xinchao(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Xin chào {update.effective_user.full_name}. Chúc bạn một ngày tốt lành!')

app = ApplicationBuilder().token("7384027524:AAHgL6Dz5rFOATYFrJLDkzt8vfvrfNj1AfM").build()


app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("xinchao", xinchao))

#google sheet
import os
import gspread
from google.oauth2.service_account import Credentials
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Đường dẫn tới file JSON chứa thông tin xác thực
SERVICE_ACCOUNT_FILE = 'credentials.json'

# Phạm vi mà Google Sheets API yêu cầu
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Kết nối tới Google Sheets
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

# Mở bảng tính Google Sheets với ID của nó
SPREADSHEET_ID = '1eoR1LGzEsJfjJ6sBh0XMSFTctHntqtTVPadEOsM3I5g'  # Thay thế bằng ID bảng tính của bạn
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

# Hàm ghi dữ liệu vào Google Sheets
def append_data_to_sheet(name, message):
    sheet.append_row([name, message])

# Hàm xử lý khi bot nhận được tin nhắn
async def handle_message(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    user_name = update.message.from_user.full_name
    user_message = update.message.text

    # Ghi dữ liệu vào Google Sheets
    append_data_to_sheet(user_name, user_message)

    # Phản hồi lại người dùng
    await context.bot.send_message(chat_id=chat_id, text=f"Đã ghi dữ liệu: {user_message}")

# Hàm chính để khởi động bot
async def main():
    # Thay YOUR_TELEGRAM_BOT_API_TOKEN bằng token của bot của bạn
    application = Application.builder().token("7384027524:AAHgL6Dz5rFOATYFrJLDkzt8vfvrfNj1AfM").build()

    # Thêm handler để xử lý tin nhắn từ người dùng
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Bắt đầu bot
    await application.start()
    await application.updater.start_polling()
    await application.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

#Kết thúc google sheet#


app.run_polling()
