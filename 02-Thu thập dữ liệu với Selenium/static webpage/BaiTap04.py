from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

# Khởi tạo WebDriver
driver = webdriver.Chrome()  # Hoặc webdriver.Firefox() nếu bạn sử dụng Firefox

# Mở trang Wikipedia
url = 'https://en.wikipedia.org/wiki/Lists_of_musicians#R'
driver.get(url)

# Đợi một chút để trang tải
time.sleep(2)

# Tìm phần tử chứa danh sách nhạc sĩ bắt đầu bằng chữ "R"
bs_R = driver.find_element(By.ID, 'R')

# Tìm tất cả các thẻ <ul> liền kề sau phần tử 'R'
bs_div = bs_R.find_element(By.XPATH, 'following-sibling::h2[1]/following-sibling::ul[1]')

# Tìm tất cả các thẻ <a> có title bắt đầu bằng "List of R"
tags = bs_div.find_elements(By.TAG_NAME, 'a')
links = ['http://en.wikipedia.org' + tag.get_attribute('href') for tag in tags if re.match(r'List of [Rr].*', tag.get_attribute('title'))]

# In ra các liên kết
for link in links:
    print(link)

# Đóng WebDriver
driver.quit()
