from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
i


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Xin chào {update.effective_user.full_name}. Chúc {update.effective_user.full_name} một ngày tốt lành! 😊 ')


app = ApplicationBuilder().token("7384027524:AAHgL6Dz5rFOATYFrJLDkzt8vfvrfNj1AfM").build()


app.add_handler(CommandHandler("hello", hello))

#google sheet
import os
import gspread
from google.oauth2.service_account import Credentials
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Đường dẫn tới file JSON chứa thông tin xác thực
SERVICE_ACCOUNT_FILE = 'credentials.json'

# Phạm vi mà Google Sheets API yêu cầu
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Kết nối tới Google Sheets
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

# Mở bảng tính Google Sheets với ID của nó
SPREADSHEET_ID = 'your_spreadsheet_id_here'  # Thay thế bằng ID bảng tính của bạn
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

# Hàm ghi dữ liệu vào Google Sheets
def append_data_to_sheet(name, message):
    sheet.append_row([name, message])

# Hàm xử lý khi bot nhận được tin nhắn
def handle_message(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat.id
    user_name = update.message.from_user.full_name
    user_message = update.message.text

    # Ghi dữ liệu vào Google Sheets
    append_data_to_sheet(user_name, user_message)

    # Phản hồi lại người dùng
    context.bot.send_message(chat_id=chat_id, text=f"Đã ghi dữ liệu: {user_message}")

# Hàm chính để khởi động bot
def main():
    # Thay YOUR_TELEGRAM_BOT_API_TOKEN bằng token của bot của bạn
    updater = Updater("YOUR_TELEGRAM_BOT_API_TOKEN")

    # Thêm handler để xử lý tin nhắn từ người dùng
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Bắt đầu bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
#Kết thúc google sheet#


app.run_polling()
