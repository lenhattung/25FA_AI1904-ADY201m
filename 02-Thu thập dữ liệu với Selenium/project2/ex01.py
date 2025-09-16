from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Đường dẫn đến file thực thi geckodriver
gecko_path = r"D:/OneDrive/Documents/GitHub/osds/02-Scraping Data/project2/geckodriver.exe"

# Khởi tởi đối tượng dịch vụ với đường geckodriver
ser = Service(gecko_path)

# Tạo tùy chọn
options = webdriver.firefox.options.Options();
options.binary_location ="C:/Program Files/Mozilla Firefox/firefox.exe"
# Thiết lập firefox chỉ hiện thị giao diện
options.headless = False

# Khởi tạo driver
driver = webdriver.Firefox(options = options, service=ser)

# Tạo url
url = 'http://pythonscraping.com/pages/javascript/ajaxDemo.html'

# Truy cập
driver.get(url)

# In ra nội dung của trang web
print("Before: ================================\n")
print(driver.page_source)


# Tạm dừng khoảng 3 giây
time.sleep(3)

# In lai
print("\n\n\n\nAfter: ================================\n")
print(driver.page_source)


# Đóng browser
driver.quit()
