from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



chrome_driver_path = "/Users/ankushsingal/Desktop/webscraping/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(event_times.text)
#
# driver.quit()
# article_count.click()

# find link by Text
# all_portals = driver.find_element(By.LINK_TEXT, 'Community portal')
# all_portals.click()

#Searching
searching = driver.find_element(By.NAME, 'search')
searching.send_keys("Python")
searching.send_keys(Keys.ENTER)

#FILL THE FORM
# driver.get("https://secure-retreat-92358.herokuapp.com")
#
# first_name = driver.find_element(By.NAME, "fName")
# first_name.send_keys("Angela")
# last_name = driver.find_element(By.NAME, "lName")
# last_name.send_keys("Yu")
# email = driver.find_element(By.NAME, "email")
# email.send_keys("info@info.com")
#
# submit = driver.find_element(By.CSS_SELECTOR, "form button")
# submit.click()