from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



chrome_driver_path = "/Users/ankushsingal/Desktop/webscraping/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

event_times = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(event_times.text)

driver.quit()