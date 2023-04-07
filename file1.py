import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

webpage = requests.get("https://www.webscraper.io/test-sites/e-commerce/static")
print(webpage.text)


