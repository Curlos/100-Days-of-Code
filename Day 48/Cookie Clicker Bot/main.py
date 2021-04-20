from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = "/Users/curlos/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
start_time = time.time()

def check_store(money_num):
    items = driver.find_elements_by_css_selector("#store b")[:-1]

    # One last invisible element at the end of the page that does not split properly so added [:-1] to exclude it
    for item in reversed(items):
        item_info = item.text.split('-')
        item_name = item_info[0].strip(' ')
        cost = int(item_info[1].strip(' ').replace(',', ''))

        while cost <= money_num:
            print(f"Bought '{item_name}' for {cost} cookies.")
            item.click()
            money_num -= cost
            break

while True:
    elapsed_time = int((time.time() - start_time))
    money = driver.find_element_by_id("money")
    money_num = int(money.text.replace(',', ''))

    if elapsed_time % 5 == 0:
        try:
            check_store(money_num)
        except:
            check_store(money_num)

    cookie.click()