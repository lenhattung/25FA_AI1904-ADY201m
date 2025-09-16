from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khoi tao WebDriver
driver = webdriver.Chrome();

# Mo mot trang web
driver.get("https://gomotungkinh.com")
time.sleep(5)

# Tìm phần tử img có id là "bonk"
bonk_img = driver.find_element(By.ID, "bonk")

# Click liên tục vào img "bonk"
while True:
    bonk_img.click()
    print("Clicked on the bonk image")
    time.sleep(0.1)
