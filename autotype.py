from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

driver = webdriver.Chrome()
driver.get("https://monkeytype.com")
time.sleep(5)

cookie =driver.find_element(By.CLASS_NAME,"active")
if(cookie):
  cookie.click()

body = driver.find_element(By.TAG_NAME,"body")
body.click()
while True:
  elem = driver.find_elements(By.CLASS_NAME,"word")
  for el in elem:
    pyautogui.write(el.text+ " ")
    time.sleep(0.18)



