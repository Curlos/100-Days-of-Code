from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/curlos/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com/")

firstName = driver.find_element_by_name("fName")
lastName = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")

firstName.send_keys("Donald")
lastName.send_keys("Trump")
email.send_keys("dtrump@whitehouse.com")

email.send_keys(Keys.ENTER)