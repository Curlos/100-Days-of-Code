from selenium import webdriver

chrome_driver_path = "/Users/curlos/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link)

times = driver.find_elements_by_css_selector('.event-widget time')
names = driver.find_elements_by_css_selector('.event-widget ul li a')
upcoming_event_data = {}

for i in range(len(times)):
    upcoming_event_data[i] = {'time': times[i].text, 'name': names[i].text}

print(upcoming_event_data)



# driver.close()
driver.quit()