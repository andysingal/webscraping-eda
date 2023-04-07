from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/ankushsingal/Desktop/webscraping/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.python.org/')

# logo = driver.find_element(By.CLASS_NAME, value="python-logo")
# print(logo.tag_name)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}
for n in range(len(event_times)):
    events[n] = {
        'time':event_times[n].text,
        'name':event_names[n].text
    }
print(events)

driver.quit()
