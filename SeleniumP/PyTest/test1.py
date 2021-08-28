from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
import requests
from selenium.webdriver.support.ui import Select
from time import sleep


@pytest.mark.usefixtures("driver")
class basetest:
    pass


class TestA1(basetest):
    @pytest.fixture()
    def initrun(self):
        a = "success"
        return a

    def test_login(self):
        un = self.driver.find_element_by_xpath("//div[@class='input-row']//input[@class='ng-untouched ng-pristine ng-invalid']")
        un.send_keys("patmdpt@gmail.com")
        passw = self.driver.find_element_by_xpath("//input[@class='ng-untouched ng-pristine ng-invalid']")
        passw.send_keys("Qwe@1234")
        login = self.driver.find_element_by_xpath("//button[@class='btn prime-btn']")
        login.click()
        # assert initrun == "b"
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "")))

    @pytest.mark.skip(reason="skiped")
    def test_skip(self):
        el = self.driver.find_element_by_xpath("")

    def test_finish(self):
        self.driver.delete_all_cookies()
        self.driver.close()
