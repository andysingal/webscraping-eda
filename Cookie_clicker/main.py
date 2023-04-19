from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "/Users/ankushsingal/Desktop/webscraping/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
CLICKABLE = "rgba(238, 238, 238, 1)"

def click_cookie(seconds):
    cookie = driver.find_element(By.ID, "cookie")
    t_end = time.time() + seconds
    while time.time() < t_end:
        cookie.click()
        time.sleep(0.001)


def buy_best():
    store = driver.find_elements(By.CSS_SELECTOR, "#store div")
    for item in reversed(store):
        if item.value_of_css_property("background-color") == CLICKABLE:
            item.click()
            break


end = time.time() + 60 * 5
while time.time() < end:
    click_cookie(5)
    buy_best()
cookie_per_s = driver.find_element(By.ID, "cps").text
print(cookie_per_s)
time.sleep(5)