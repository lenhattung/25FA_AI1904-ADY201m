from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

# Khởi tạo WebDriver
driver = webdriver.Chrome()  # Hoặc webdriver.Firefox() nếu bạn sử dụng Firefox

# Mở trang Wikipedia
url = 'https://en.wikipedia.org/wiki/List_of_painters_by_name'
driver.get(url)

# Đợi một chút để trang tải
time.sleep(2)

# Lấy tất cả các thẻ <a> với title chứa "List of painters"
tags = driver.find_elements(By.XPATH, "//a[contains(@title, 'List of painters')]")

# Tạo danh sách các liên kết
links = ['http://en.wikipedia.org' + tag.get_attribute('href') for tag in tags]

# In ra các liên kết
for link in links:
    print(link)

# Đóng WebDriver
driver.quit()