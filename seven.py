from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart
driver = webdriver.Chrome()
sleep(5)
kayak = "https://www.kayak.com/flights/LTS-SIN/2024-11-29-flexible/2024-12-15-flexible?sort=bestflight_a"
driver.get(kayak)
sleep(5)
cheap_results = '//a[@data-code = "price"]'
driver.find_element_by_xpath(cheap_results).click()

xp_results_table = '//*[@class = "resultWrapper"]'
flight_containers = driver.find_elements_by_xpath(xp_results_table)
flights_list = [flight.text for flight in flight_containers]

# 列出前 3 个结果
flights_list[0:3]