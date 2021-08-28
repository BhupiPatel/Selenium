from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time

desired_cap = {
  'browser_version': '75.0',
  'os': 'Windows',
  'os_version': '10',

  #Configure ChromeOptions to pass fake media stream
  'chromeOptions': {
    'args': ["--use-fake-device-for-media-stream", "--use-fake-ui-for-media-stream"]
  }
}
driver = webdriver.Remote(command_executor = 'http://USERNAME:ACCESS_KEY@hub.browserstack.com:80/wd/hub', desired_capabilities = desired_cap)

# WebCam Test
driver.get("https://webcamtests.com/check")
time.sleep(5)
driver.find_element_by_id("webcam-launcher").click()
time.sleep(2)

# Mic Test
driver.get("https://www.vidyard.com/mic-test/")
time.sleep(5)
driver.find_element_by_xpath("//*[@class='button' and text()='Grant access'][1]").click()
time.sleep(2)
driver.quit()