#"Hello World"(print)

from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

# Open MonkeyType in Chrome
driver = webdriver.Chrome()
driver.get("https://monkeytype.com")
time.sleep(5) # Wait to load browser


# Handle cookie
cookie =driver.find_element(By.CLASS_NAME,"active")
if(cookie):
  cookie.click()

# Find Body and click it to focus on MonkeyType
body = driver.find_element(By.TAG_NAME,"body")
body.click()

try:

# Write Words in MonkeyType

  while True:
    elem = driver.find_element(By.CLASS_NAME,"word.active")
    pyautogui.write(elem.text+" ",interval=0) # adjust time 

except Exception as e:
# Shows error if failed
  print(e)

# To view the result 
time.sleep(10)
# Automatically close the browser
driver.quit()