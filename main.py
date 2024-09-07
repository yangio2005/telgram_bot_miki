from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import json
import gspread
from google.oauth2.service_account import Credentials


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Xin chào {update.effective_user.full_name}. Chúc {update.effective_user.full_name} một ngày tốt lành! 😊 ')


app = ApplicationBuilder().token("7384027524:AAHgL6Dz5rFOATYFrJLDkzt8vfvrfNj1AfM").build()


app.add_handler(CommandHandler("hello", hello))


# Đường dẫn tới file JSON chứa thông tin xác thực
SERVICE_ACCOUNT_FILE = 'path_to_your_service_account.json'

# Phạm vi mà Google Sheets API yêu cầu
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Tải thông tin xác thực từ file JSON
creds = None
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Kết nối với Google Sheets
client = gspread.authorize(creds)

# Mở bảng tính Google Sheets với ID của nó
SPREADSHEET_ID = 'your_spreadsheet_id_here'  # Thay thế bằng ID bảng tính của bạn
sheet = client.open_by_key(SPREADSHEET_ID).sheet1
app.run_polling()
