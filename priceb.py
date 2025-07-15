from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.bonbast.com/")

# لیست آیتم‌ها: (نام، id خرید، id فروش یا None)
items = [
    ("💵 دلار آمریکا", "usd1", "usd2"),
    ("💶 یورو", "eur1", "eur2"),
    ("💷 پوند انگلیس", "gbp1", "gbp2"),
    ("🇹🇷 لیر ترکیه", "try1", "try2"),
    ("🇨🇳 یوان چین", "cny1", "cny2"),
    ("🇷🇺 روبل روسیه", "rub1", "rub2"),
    ("🏅 طلای ۱۸ عیار", "gol18_top", None),
    ("🥇 سکه امامی", "emami1_top", None),
]

print("📊 نرخ لحظه‌ای ارز و طلا از سایت Bonbast:\n")

for name, buy_id, sell_id in items:
    try:
        buy_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, buy_id))
        )
        buy_price = buy_element.get_attribute("innerHTML").strip()

        print(f"{name}")
        print(f"   💰 قیمت: {buy_price} تومان\n") if not sell_id else None

        if sell_id:
            sell_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, sell_id))
            )
            sell_price = sell_element.get_attribute("innerHTML").strip()
            print(f"   🔼 خرید: {buy_price} تومان")
            print(f"   🔽 فروش: {sell_price} تومان\n")

    except Exception as e:
        print(f"⚠️ {name}: قیمت پیدا نشد")

driver.quit()
