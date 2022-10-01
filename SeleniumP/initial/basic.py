from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep


driver = webdriver.Chrome("C:/Users/thebh/Downloads/chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@name='q']").send_keys("bhupi")

e=driver.find_element_by_xpath("//*[@name='btnK']")
select =  Select(e)
select.select_by_visible_text("xxx")
#driver.find_element_by_xpath("//*[@name='btnK']").click()

a = webdriver.ActionChains(driver)
a.click(e)
a.perform()
sleep(3)

driver.delete_all_cookies()
driver.close()