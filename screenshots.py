from selenium import webdriver
from PIL import Image
from Screenshot import Screenshot
import time

driver = webdriver.Chrome()
url = "https://www.google.com"
driver.get(url)

driver.find_element("id", "APjFqb").click()

# for i in range(5):
#     driver.save_screenshot("ss{}.png".format(i))
#     time.sleep(5)

# screenshot = Image.open("ss.png")
# screenshot.show()

time.sleep(5)
driver.close()