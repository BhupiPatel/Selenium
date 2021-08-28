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
un = driver.find_element_by_xpath("//div[@class='input-row']//input[@class='ng-untouched ng-pristine ng-invalid']")
un.send_keys("patmdpt@gmail.com")
passw = driver.find_element_by_xpath("//input[@class='ng-untouched ng-pristine ng-invalid']")
passw.send_keys("Qwe@1234")
login = driver.find_element_by_xpath("//button[@class='btn prime-btn']")
login.click()
print("success")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "myDynamicElement")))

driver.send

driver.delete_all_cookies()
driver.close()
