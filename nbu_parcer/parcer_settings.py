from selenium import webdriver


g_url_to_parse = 'https://coins.bank.gov.ua/my-account/'
driver = webdriver.Chrome(executable_path="E:\ВІТЯ\pythonProject_nacbank\chromedriver.exe")



import parcer_settings
import requests, time
from bs4 import BeautifulSoup

