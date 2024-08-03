from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.ID, value="cookie")
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")

# Function to get the current number of cookies
def get_cookies():
    cookies_text = driver.find_element(by=By.ID, value="money").text
    return int(cookies_text.replace(",", ""))

# Function to buy the most expensive upgrade possible
def buy_upgrades():
    items = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
    affordable_upgrades = []
    for item in items:
        item_text = item.text
        if item_text:
            cost = int(item_text.split("-")[1].strip().replace(",", ""))
            if get_cookies() >= cost:
                affordable_upgrades.append((cost, item))
    if affordable_upgrades:
        # Buy the most expensive affordable upgrade
        affordable_upgrades.sort(key=lambda x: x[0], reverse=True)
        affordable_upgrades[0][1].click()

# Main loop
start_time = time.time()
timeout = 5 

while True:
    cookie.click()
    # Check and buy upgrades every 5 seconds
    if time.time() - start_time > timeout:
        buy_upgrades()
        start_time = time.time()
