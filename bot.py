import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7811956303:AAEO-2JJnClU-1ac5JeMUpSotz80LZLYd3w"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! من Tech Price BOT هستم 💰\n"
        "برای دریافت قیمت دلار بنویس: /dollar\n"
        "قیمت یورو: /euro\n"
        "قیمت سکه: /coin"
    )

def get_price(code):
    try:
        url = "https://www.navasan.net/api/latest/"
        response = requests.get(url)
        data = response.json()
        return data[code]["value"], data[code]["date"], data[code]["time"]
    except:
        return None, None, None

async def dollar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    value, date, time = get_price("usd")
    if value:
        await update.message.reply_text(f"💵 قیمت دلار: {value} تومان\n📅 {date} ⏰ {time}")
    else:
        await update.message.reply_text("❌ خطا در دریافت قیمت دلار.")

async def euro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    value, date, time = get_price("eur")
    if value:
        await update.message.reply_text(f"💶 قیمت یورو: {value} تومان\n📅 {date} ⏰ {time}")
    else:
        await update.message.reply_text("❌ خطا در دریافت قیمت یورو.")

async def coin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    value, date, time = get_price("coin_old_design")
    if value:
        await update.message.reply_text(f"🪙 قیمت سکه بهار آزادی: {value} تومان\n📅 {date} ⏰ {time}")
    else:
        await update.message.reply_text("❌ خطا در دریافت قیمت سکه.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("dollar", dollar))
app.add_handler(CommandHandler("euro", euro))
app.add_handler(CommandHandler("coin", coin))

print("✅ ربات در حال اجراست...")
app.run_polling()
