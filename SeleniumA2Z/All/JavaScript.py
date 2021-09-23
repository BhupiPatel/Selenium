from selenium import webdriver

driver = webdriver.Chrome()

# Click
javaScript = "document.getElementsByName('username')[0].click();"
driver.execute_script(javaScript)
btn = driver.find_element_by_name ("spbutton")
driver.execute_script ("arguments[0].click();", btn)
# feel an element with dATA
driver.execute_script("document.getElementById('login_email').value='12345'")
javaScript = "document.getElementsByClassName('gsc-input')[0].value = 'T' "
driver.execute_script(javaScript)
driver.execute_script("arguments[0].value='Bhupi';", btn)
# you can have more than one JavaScript action in your statement.
userName = driver.find_element_by_xpath("//button[@name='username']")
password = driver.find_element_by_xpath("//button[@name='password']")
driver.execute_script("arguments[0].click();arguments[1].click();", userName, password)
# extract the value with Javascript Executor
print(driver.execute_script('return document.getElementsByName("username")[0].value'))
print(driver.execute_script('return document.getElementById("fsr").innerText'))
# to scroll with Javascript executor
driver.execute_script ("window.scrollTo(0,document.body.scrollHeight);")
# print the page title in console
print(driver.execute_script('return document.title'))
# print the page URL in console
print(driver.execute_script('return document.URL'))
# Check specific radio button or checkbox
driver.execute_script("document.querySelector(\"input[value='seven']\").checked=true")
driver.execute_script()
