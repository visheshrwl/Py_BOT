from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

username = "USERNAME"
password = "PASSWORD"

driver = webdriver.Chrome()

driver.get("https://github.com/login")

driver.find_element("id", "login_field").send_keys(username)
driver.find_element("id", "password").send_keys(password)

driver.find_element("name", "commit").click()

WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

error_message = "Incorrect username or password."

errors = driver.find_elements("css selector", ".flash-error")

if any (error_message in e.text for e in errors):
    print("[!] Login Failed")
else:
    print("[+] Login Successful")


repos = driver.find_element("css selector", ".js-repos-container")

WebDriverWait(driver=driver, timeout=10).until((lambda x: repos.text != "Loading...."))

for repo in repos.find_elements("css selector", "li.public"):
    print(repo.find_element("css selector", "a").get_attribute("href"))

# SCROLL_PAUSE_TIME = 1

# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     time.sleep(SCROLL_PAUSE_TIME)

#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

time.sleep(20)
driver.close()