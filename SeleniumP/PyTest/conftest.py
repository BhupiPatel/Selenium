import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome("/Users/bhupeshpatel/Downloads/chromedriver", options=options)

    driver.maximize_window()
    driver.implicitly_wait(30)

