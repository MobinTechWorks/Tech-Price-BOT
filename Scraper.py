from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# راه‌اندازی درایور کروم
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# باز کردن سایت bonbast
driver.get("https://www.bonbast.com/")

try:
    # منتظر بمون تا المنت‌های قیمت لود بشن
    buy_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "usd1"))
    )
    sell_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "usd2"))
    )

    # گرفتن مقدار از innerHTML
    buy_price = buy_element.get_attribute("innerHTML").strip()
    sell_price = sell_element.get_attribute("innerHTML").strip()

    print("💵 قیمت خرید دلار:", buy_price)
    print("💸 قیمت فروش دلار:", sell_price)

except Exception as e:
    print("⛔ خطا:", e)

finally:
    driver.quit()
