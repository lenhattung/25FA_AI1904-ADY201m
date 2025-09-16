from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import pandas as pd
import time

# Tạo DataFrame rỗng
d = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})

# Khởi tạo WebDriver
driver = webdriver.Chrome()  # Hoặc webdriver.Firefox() nếu bạn sử dụng Firefox

# Mở trang Wikipedia của Edvard Munch
url = 'http://en.wikipedia.org/wiki/Edvard_Munch'
driver.get(url)

# Đợi một chút để trang tải
time.sleep(2)

# Lấy tên họa sĩ
try:
    name = driver.find_element(By.TAG_NAME, 'h1').text
except:
    name = ''

# Lấy thông tin sinh
try:
    birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
    birth = birth_element.text
    birth = re.findall(r'[0-9]+\s+[A-Za-z]+\s+[0-9]+', birth)[0]
except:
    birth = ''

# Lấy thông tin mất
try:
    death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
    death = death_element.text
    death = re.findall(r'[0-9]+\s+[A-Za-z]+\s+[0-9]+', death)[0]
except:
    death = ''

# Lấy thông tin quốc tịch
try:
    nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
    nationality = nationality_element.text
except:
    nationality = ''

# Tạo từ điển với thông tin của họa sĩ
painter = {'name': name, 'birth': birth, 'death': death, 'nationality': nationality}

# Chuyển đổi từ điển thành DataFrame
painter_df = pd.DataFrame([painter])

# Thêm thông tin vào DataFrame chính
d = pd.concat([d, painter_df], ignore_index=True)

# In ra DataFrame
print(d)

# Đóng WebDriver
driver.quit()