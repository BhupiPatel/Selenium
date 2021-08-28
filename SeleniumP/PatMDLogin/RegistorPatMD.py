from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
import requests
from selenium.webdriver.support.ui import Select
from time import sleep

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome("/Users/bhupeshpatel/Downloads/chromedriver", options=options)
driver.maximize_window()
driver.implicitly_wait(30)
action = ActionChains(driver)
driver.get("https://www.patientmd.com/#")
login = driver.find_element_by_xpath("//button[@class='dropbtn']")
action.move_to_element(login).perform()
reg = driver.find_element_by_xpath("")