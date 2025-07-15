import telebot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# توکن ربات
TOKEN = "7811956303:AAEO-2JJnClU-1ac5JeMUpSotz80LZLYd3w"
bot = telebot.TeleBot(TOKEN)

# تابع گرفتن قیمت‌ها
def get_prices():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.bonbast.com/")

        wait = WebDriverWait(driver, 10)

        prices = {}
        prices['USD_buy'] = wait.until(EC.presence_of_element_located((By.ID, "usd1"))).text.strip()
        prices['USD_sell'] = wait.until(EC.presence_of_element_located((By.ID, "usd2"))).text.strip()
        prices['EUR_buy'] = driver.find_element(By.ID, "eur1").text.strip()
        prices['EUR_sell'] = driver.find_element(By.ID, "eur2").text.strip()
        prices['GBP_buy'] = driver.find_element(By.ID, "gbp1").text.strip()
        prices['GBP_sell'] = driver.find_element(By.ID, "gbp2").text.strip()
        prices['TRY_buy'] = driver.find_element(By.ID, "try1").text.strip()
        prices['TRY_sell'] = driver.find_element(By.ID, "try2").text.strip()
        prices['CNY_buy'] = driver.find_element(By.ID, "cny1").text.strip()
        prices['CNY_sell'] = driver.find_element(By.ID, "cny2").text.strip()
        prices['RUB_buy'] = driver.find_element(By.ID, "rub1").text.strip()
        prices['RUB_sell'] = driver.find_element(By.ID, "rub2").text.strip()
        prices['Gold'] = driver.find_element(By.ID, "gol18_top").text.strip()
        prices['Coin'] = driver.find_element(By.ID, "emami1_top").text.strip()
        driver.quit()
        return prices

    except Exception as e:
        return {"error": str(e)}

# هندلر /start
@bot.message_handler(commands=['start', 'price'])
def send_prices(message):
    data = get_prices()
    if "error" in data:
        bot.reply_to(message, f"⛔ خطا در دریافت اطلاعات:\n{data['error']}")
        return

    text = f"""📊 نرخ لحظه‌ای ارز و طلا از Bonbast:

💵 دلار
  🔼 خرید: {data['USD_buy']} تومان
  🔽 فروش: {data['USD_sell']} تومان

💶 یورو
  🔼 خرید: {data['EUR_buy']} تومان
  🔽 فروش: {data['EUR_sell']} تومان

💷 پوند
  🔼 خرید: {data['GBP_buy']} تومان
  🔽 فروش: {data['GBP_sell']} تومان

🇹🇷 لیر
  🔼 خرید: {data['TRY_buy']} تومان
  🔽 فروش: {data['TRY_sell']} تومان

🇨🇳 یوان
  🔼 خرید: {data['CNY_buy']} تومان
  🔽 فروش: {data['CNY_sell']} تومان

🇷🇺 روبل
  🔼 خرید: {data['RUB_buy']} تومان
  🔽 فروش: {data['RUB_sell']} تومان

🥇 طلا ۱۸ عیار: {data['Gold']} تومان
🥈 سکه امامی: {data['Coin']} تومان
"""
    bot.reply_to(message, text)

# اجرای ربات
bot.polling()
