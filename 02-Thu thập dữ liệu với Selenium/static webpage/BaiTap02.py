from selenium import webdriver
from selenium.webdriver.common.by import By
import time

painter_links = []

# Khởi tạo WebDriver
driver = webdriver.Chrome()  # Hoặc webdriver.Firefox() nếu bạn sử dụng Firefox

# Mở trang Wikipedia
url = 'http://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22M%22'
driver.get(url)

# Đợi một chút để trang tải
time.sleep(2)

# Tìm tất cả các thẻ <ul> và chọn thẻ thứ hai
ul_tags = driver.find_elements(By.TAG_NAME, 'ul')
li_tags = ul_tags[1].find_elements(By.TAG_NAME, 'li')  # Lấy thẻ <li> từ thẻ <ul> thứ hai

# Tạo danh sách các liên kết
links = ['http://en.wikipedia.org' + tag.find_element(By.TAG_NAME, 'a').get_attribute('href') for tag in li_tags]

# Thêm liên kết vào danh sách painter_links
painter_links.extend(links)

# In ra các liên kết
for link in painter_links:
    print(link)

# Đóng WebDriver
driver.quit()
