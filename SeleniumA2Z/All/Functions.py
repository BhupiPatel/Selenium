from selenium import webdriver
from selenium.common.exceptions import WebDriverException, RemoteDriverServerException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
# desired_capabilities
# options

driver.get("URL")
driver.delete_all_cookies()
driver.close()
driver.quit()

# get
strg = driver.current_url
strg = driver.page_source
strg = driver.title

# findElements
driver.find_element(By.XPATH, '')
driver.find_element(By.ID, '')
driver.find_element(By.NAME, '')
driver.find_element(By.TAG_NAME, '')
driver.find_element(By.CLASS_NAME, '')
driver.find_element(By.CSS_SELECTOR, '')
driver.find_element(By.LINK_TEXT, '')
driver.find_element(By.PARTIAL_LINK_TEXT, '')
elList = driver.find_elements(By.XPATH, '')

driver.find_element_by_xpath('')
driver.find_element_by_class_name('')
driver.find_element_by_css_selector('')
driver.find_element_by_id('')
driver.find_element_by_link_text('')
driver.find_element_by_name('')
driver.find_element_by_partial_link_text('')
driver.find_element_by_tag_name('')
elList = driver.find_elements_by_xpath('')

# Operations
el = driver.find_element_by_xpath('')

el.click()
el.clear()
el.submit()
el.get_attribute()
el.get_property()
srtg = el.text
strg = el.tag_name
el.send_keys('')
el.send_keys('', Keys.ENTER)

# Switch to
# frame
driver.switch_to.frame('frameid')  # driver.switch_to_frame("framename"), where framename is the name attribute
# present under the frame/iframe tag in HTML.
driver.switch_to.frame(0)
driver.switch_to.frame(el)
driver.switch_to.default_content()
driver.switch_to.parent_frame()

# windows
driver.window_handles()
driver.current_window_handle()
driver.switch_to.window()

# Alart
driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()
driver.switch_to.alert.send_keys()
srtg = driver.switch_to.alert.text

# active element
var = driver.switch_to.active_element

# is
el.is_displayed()
el.is_enabled()
el.is_selected()

# navigat
driver.back()
driver.forward()
driver.refresh()

# manage
driver.maximize_window()
driver.fullscreen_window()
driver.get_window_position()
driver.set_window_position(0, 0)
driver.set_window_size(0, 0)
driver.get_window_size()

driver.get_cookie(0)
driver.get_cookies()
driver.delete_all_cookies()
driver.add_cookie(0)
driver.delete_cookie(0)

# select class
# Find id of option
x = driver.find_element_by_id('RESULT_RadioButton-9')
drop = Select(x)
drop.is_multiple()
# Select by index
drop.select_by_index(2)
drop.select_by_visible_text('')
drop.select_by_value('')

drop.deselect_all()
drop.deselect_by_index(0)
drop.deselect_by_value('')
drop.deselect_by_visible_text('')

drop.options()
drop.first_selected_option()
drop.all_selected_options()

# Action class

# create action chain object
action = ActionChains(driver)

menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav # submenu1")

action.click(menu).perform()
action.context_click(menu).perform()
action.double_click(menu).perform()
action.click_and_hold(menu).perform()
action.send_keys(menu).perform()
action.send_keys_to_element(menu, Keys.ENTER).perform()
action.drag_and_drop(menu, hidden_submenu).perform()
action.drag_and_drop_by_offset(menu, 1, 1).perform()
action.move_by_offset(1, 1).perform()
action.move_to_element(menu).perform()
action.move_to_element_with_offset(menu, 0, 0).perform()
action.key_down('a').perform()
action.key_up('a').perform()
action.pause(5000).perform()
action.release(Keys.BACKSPACE).perform()
action.reset_actions()
action.w3c_actions()
