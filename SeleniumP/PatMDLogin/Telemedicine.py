import pytest
import helpers.helpers as util
from time import sleep
from selenium.webdriver.common.keys import Keys
import allure
import unittest
from selenium.common.exceptions import NoSuchElementException
from random import randint
from faker import Faker
from datetime import date
from datetime import timedelta
import random
from selenium.webdriver.support.ui import Select
import re

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options



class Test0005(baseTestBug):
fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    fdriver = webdriver.Firefox(executable_path='/Users/bhupeshpatel/Downloads/geckodriver',firefox_options=fireFoxOptions)

    # for jenkins

    # options = Options()
    # options.add_argument('--disable-gpu')
    # options.add_argument('use-fake-ui-for-media-stream')
    # options.add_argument("--use-fake-device-for-media-stream")
    # options.add_experimental_option('prefs',{'profile.default_content_setting_values.notifications':1})
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1920,1080')
    # options.binary_location = "/usr/bin/google-chrome"
    # fdriver = webdriver.Chrome('/home/ubuntu/chromedriver',chrome_options=options)

    # for local mechine

    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('use-fake-ui-for-media-stream')
    options.add_argument("--use-fake-device-for-media-stream")
    options.add_experimental_option('prefs',{'profile.default_content_setting_values.notifications':1})
    # options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    # options.binary_location = "/usr/bin/google-chrome"
    fdriver = webdriver.Chrome('/Users/bhupeshpatel/Downloads/chromedriver',chrome_options=options)


#     # go into doc app liv vid

    @allure.title("Log Into Module")
    def test_bug_login_00051(self):
        loginInto(envObj.test_useEnviroment(self),self.driver,"PATIENT")
        sleep(10)
        self.driver.set_window_size(1400, 900)
        filePath = util.save_screenshot(self.driver,"liveNowTeleVid","Patient","0002")
        allure.attach.file(filePath,attachment_type=allure.attachment_type.PNG)

    @allure.title("click login")
    def test_bug_click_login_00051(self):
        sleep(8)
        login = util.Find_Element_Xpath(self.driver,"//button[@class='dropbtn']")
        util.MouseOver(self.driver, login)
        sleep(4)
        pat_login = util.Find_Element_Xpath(self.driver,"//div[@class='as patient']//a[contains(text(),'Login to Continue')]")
        pat_login.click()
        sleep(10)
        filePath = util.save_screenshot(self.driver,"liveNowTeleVid","Patient","0002")
        allure.attach.file(filePath,attachment_type=allure.attachment_type.PNG)

    @allure.title("enter email password and login")
    def test_bug_enter_email_password_and_login_login_00051(self):
        udid = "patmdpt@gmail.com"
        password = "Qwe@1234"
        util.patientLogin(self.driver,udid,password)
        sleep(20)

        filePath = util.save_screenshot(self.driver,"liveNowTeleVid","Patient","0002")
        allure.attach.file(filePath,attachment_type=allure.attachment_type.PNG)

    @allure.title("click on appointment")
    def test_bug_click_on_appointment_00051(self):
        # opt_button = util.Find_Element_Xpath(self.driver,"//ion-button[@class='tool-btn ham-btn md button button-solid ion-activatable ion-focusable hydrated']")
        # opt_button.click()
        # click_appoint = util.Find_Element_Xpath(self.driver,"//ion-menu-toggle[2]//ion-item[1]")
        # click_appoint.click()
        # self.driver.get("https://dev.patientmd.com:8080/#/telemedicine/live-now")
        self.driver.get(envObj.test_useEnviroment(self)+'/telemedicine/live-now')
        sleep(15)
        filePath = util.save_screenshot(self.driver,"liveNowTeleVid","Patient","0002")
        allure.attach.file(filePath,attachment_type=allure.attachment_type.PNG)

    @allure.title("click on doc appoint")
    def test_bug_doc_app_00051(self,globalList,globalListint):
        # app = util.Find_Element_Xpath(self.fdriver,"(//*[contains(text(),'Anirban majumdar')])[1]")
        elements = self.driver.find_elements_by_xpath("//div[@class='ng-star-inserted']//div//ion-list[1]")
        name = self.driver.find_elements_by_xpath("//body//div[@class='main-container-zu']//div//div//ion-list[1]//ion-item[1]//div[1]//div[1]//div[2]//h6[1]")
        time = self.driver.find_elements_by_xpath("//body//div[@class='main-container-zu']//div//div//ion-list[1]//ion-item[1]//div[1]//div[1]//span[2]")
        vid = self.driver.find_elements_by_xpath("//div//ion-list[1]//ion-item[1]//div[1]//div[1]//span[1]//ion-icon[1]")

        print(len(elements))
        for i in range (len(elements)):
            if "videocam" in vid[i].get_attribute("aria-label") and "Christ Pavlatos" in name[i].text :
                globalListint.intList.append(time[i].text)
                util.ActionClick(self.driver, elements[i])

        print(globalListint.intList)
        sleep(15)
        filePath = util.save_screenshot(self.driver,"liveNowTeleVid","Patient","0002")
        allure.attach.file(filePath,attachment_type=allure.attachment_type.PNG)

    @allure.title("click on continue")
    def test_bug_click_on_continue_00051(self):
        video_tele = util.Find_Element_Xpath(self.driver, "//*[text()='CONTINUE VIDEO TELEMEDICINE']")
        util.ActionClick(self.driver, video_tele)
        sleep(15)
        filePath = util.save_screenshot(self.driver,"liveNowTeleVid","Patient","0002")
        allure.attach.file(filePath,attachment_type=allure.attachment_type.PNG)


#     # doctors


    @allure.title("Log Into Module")
    def test_bug_login_00052(self):
        loginInto(envObj.test_useEnviroment(self),self.fdriver,"PATIENT")
        sleep(10)
        self.fdriver.set_window_size(1400, 900)
        filePath = util.save_screenshot(self.fdriver,"liveNowTeleVid","Patient","0002")
        allure.attach.file(filePath,attachment_type=allure.attachment_type.PNG)

    @allure.title("click login")
    def test_bug_click_login_00052(self):
        sleep(8)
        login = util.Find_Element_Xpath(self.fdriver,"//button[@class='dropbtn']")
        util.MouseOver(self.fdriver, login)
        sleep(2)
        pat_login = util.Find_Element_Xpath(self.fdriver,"//div[@class='as doctor']//a[contains(text(),'Login to Continue')]")
        pat_login.click()
        sleep(20)
        filePath = util.save_screenshot(self.fdriver,"liveNowTeleVid","Patient","0002")
        allure.attach.file(filePath,attachment_type=allure.attachment_type.PNG)

    @allure.title("enter email password and login")
    def test_bug_enter_email_password_and_login_login_00052(self):
        udid = "patmddr1@yopmail.com"
        password = "Qwe1234"
        util.patientLogin(self.fdriver,udid,password)
        sleep(20)

        filePath = util.save_screenshot(self.fdriver,"liveNowTeleVid","Patient","0002")
        allure.attach.file(filePath,attachment_type=allure.attachment_type.PNG)

    @allure.title("goto live now")
    def test_bug_goto_live_now_00052(self):
        # self.fdriver.get("https://dev.patientmd.com:8080/#/m/telemedicine/live-now")
        self.fdriver.get(envObj.test_useEnviroment(self)+'/m/telemedicine/live-now')
        sleep(15)
        filePath = util.save_screenshot(self.fdriver,"liveNowTeleVid","Patient","0002")
        allure.attach.file(filePath,attachment_type=allure.attachment_type.PNG)

    @allure.title("click on doc appoint")
    def test_bug_doc_app_00052(self,globalList,globalListint):
        elements = self.fdriver.find_elements_by_xpath("//body//div[@class='main-container-zu']//div//div//div//div//ion-list[1]")
        name = self.fdriver.find_elements_by_xpath("//body//div[@class='main-container-zu']//div//div//ion-list[1]//ion-item[1]//div[1]//div[1]//div[2]//h6[1]")
        time = self.fdriver.find_elements_by_xpath("//body//div[@class='main-container-zu']//div//div//ion-list[1]//ion-item[1]//div[1]//div[1]//span[2]")
        vid = self.fdriver.find_elements_by_xpath("//body//div[@class='main-container-zu']//div//div//div//div//ion-list[1]//ion-item[1]//div[1]//div[1]//span[1]//ion-icon[1]")
        # for i in range (len(elements)):
        #     if "videocam" in vid[i].get_attribute("aria-label") and "Anirban majumdar" in name[i].text :
        #         globalListint.intList.append(time[i].text)
        #         util.ActionClick(self.driver, elements[i])
        print(len(elements))
        for i in range (len(elements)):
            if time[i].text == globalListint.intList[0]:
                print(time[i].text +" : "+ globalListint.intList[0]+" : "+str(i))
                util.ActionClick(self.fdriver, elements[i])

#         print(globalListint.intList)

#         # print(globalList.empList)


        sleep(15)
        filePath = util.save_screenshot(self.fdriver,"liveNowTeleVid","Patient","0002")
        allure.attach.file(filePath,attachment_type=allure.attachment_type.PNG)

    @allure.title("click on continue")
    def test_bug_continue_00052(self):
        continuBtn = util.Find_Element_Xpath(self.fdriver,"//button[@class='fab-cyan']")
        util.ActionClick(self.fdriver, continuBtn)
        sleep(15)
        filePath = util.save_screenshot(self.fdriver,"liveNowTeleVid","Patient","0002")
        allure.attach.file(filePath,attachment_type=allure.attachment_type.PNG)

        # check screen of driver
    @allure.title("check screen")
    def test_bug_check_screen_00051(self):
        # if alert = self.fdriver.switch_to.alert.is_displayed():
        #     alert.accept()
        sleep(15)
        filePath = util.save_screenshot(self.driver,"liveNowTeleVid","Patient","0002")
        allure.attach.file(filePath,attachment_type=allure.attachment_type.PNG)
        # check screen of fdriver
    @allure.title("check screen")
    def test_bug_check_screen_00052(self):
        # self.fdriver.switch_to.alert.accept()
        sleep(15)
        filePath = util.save_screenshot(self.fdriver,"liveNowTeleVid","Patient","0002")
        allure.attach.file(filePath,attachment_type=allure.attachment_type.PNG)
        self.fdriver.close()
