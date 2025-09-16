from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
import time
import pandas as pd

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
url = 'https://nhathuoclongchau.com.vn/thuc-pham-chuc-nang/vitamin-khoang-chat'

# Truy cập
driver.get(url)

# Tạm dừng khoảng 2 giây
time.sleep(1)

# Tìm phần tử body của trang để gửi phím mũi tên xuống
body = driver.find_element(By.TAG_NAME, "body")
time.sleep(3)

for k in range (10):
    try:
        # Lấy tất cả các button trên trang
       buttons = driver.find_elements(By.TAG_NAME, "button")

       # Duyệt qua từng button
       for button in buttons:
           # Kiểm tra nếu nội dung của button chứa "Xem thêm" và "sản phẩm"
           if "Xem thêm" in button.text and "sản phẩm" in button.text:
               # Di chuyển tới button và click
               button.click()
               break  # Thoát khỏi vòng lặp nếu đã click thành công
    
    except Exception as e:
        print(f"Lỗi: {e}")

# Nhấn phím mũi tên xuống nhiều lần để cuộn xuống từ từ
for i in range(50):  # Lặp 30 lần, mỗi lần cuộn xuống một ít
    body.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.01)  # Tạm dừng 0.2 giây giữa mỗi lần cuộn để trang tải nội dung

# Tạm dừng thêm vài giây để trang tải hết nội dung ở cuối trang
time.sleep(1)

# Tao cac list
stt = []
ten_san_pham = []
gia_ban = []
hinh_anh = []

# Tìm tất cả các button có nội dung là "Chọn mua"
buttons = driver.find_elements(By.XPATH, "//button[text()='Chọn mua']")

print(len(buttons))

# lay tung san pham
for i, bt in enumerate(buttons, 1):
    # Quay ngược 3 lần để tìm div cha
    parent_div = bt
    for _ in range(3):
        parent_div = parent_div.find_element(By.XPATH,"./..")  # Quay ngược 1 lần
    
    sp =parent_div
    
    # Lat ten sp
    try:
        tsp = sp.find_element(By.TAG_NAME, 'h3').text
    except:
        tsp=''
    
    # Lat gia sp
    try:
        gsp = sp.find_element(By.CLASS_NAME, 'text-blue-5').text
    except:
        gsp=''
    
    # Lat hinh anh
    try:
        ha = sp.find_element(By.TAG_NAME, 'img').get_attribute('src')
    except:
        ha=''

    # Chi them vao ds neu co ten sp
    if(len(tsp)>0):
        stt.append(i)
        ten_san_pham.append(tsp)
        gia_ban.append(gsp)
        hinh_anh.append(ha)

# Tạo df
df=pd.DataFrame({
    "STT" : stt,
    "Tên sản phẩm": ten_san_pham,
    "Giá bán":gia_ban,
    "Hình ảnh":hinh_anh
    
})

df.to_excel('danh_sach_sp_3.xlsx', index=False)