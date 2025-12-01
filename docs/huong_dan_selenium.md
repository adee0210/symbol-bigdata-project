# Hướng dẫn sử dụng Selenium với Python

## 1. Giới thiệu
Selenium là thư viện tự động hóa trình duyệt web, hỗ trợ kiểm thử, crawl dữ liệu, thao tác web tự động. Selenium có thể làm việc với nhiều trình duyệt như Chrome, Chromium, Firefox, Edge...

## 2. Cài đặt
```sh
pip install selenium
```

## 3. Chuẩn bị driver
- Chrome/Chromium: cần chromedriver
- Firefox: cần geckodriver
- Edge: cần msedgedriver

Đảm bảo driver phù hợp với phiên bản trình duyệt.

## 4. Khởi tạo trình duyệt
### Tùy chọn chung cho các trình duyệt
```python
import uuid
import tempfile

# Các tùy chọn chung để tối ưu hóa và tránh phát hiện
common_options = [
    "--no-sandbox",  # Vô hiệu hóa sandbox để tránh lỗi trong container hoặc môi trường hạn chế quyền
    "--disable-dev-shm-usage",  # Sử dụng disk thay vì shared memory, tránh lỗi khi /dev/shm đầy
    "--disable-gpu",  # Vô hiệu hóa GPU acceleration, hữu ích trong headless hoặc môi trường không GPU
    "--disable-blink-features=AutomationControlled",  # Vô hiệu hóa tính năng tự động hóa để tránh bị phát hiện là bot
    "--no-first-run",  # Bỏ qua các bước setup lần đầu khi khởi động trình duyệt
    "--disable-default-apps",  # Vô hiệu hóa các ứng dụng mặc định của trình duyệt
    "--disable-extensions",  # Vô hiệu hóa extensions để chạy nhanh hơn và tránh xung đột
    "--headless=new",  # Chạy trình duyệt ở chế độ headless (không giao diện), phiên bản mới
    f"--user-data-dir={tempfile.mkdtemp()}"  # Sử dụng thư mục user data tạm thời unique để tránh xung đột session
]
```

### Chrome/Chromium
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.binary_location = "/snap/bin/chromium"  # Chỉ cần nếu dùng trình duyệt không phải mặc định
for option in common_options:
    chrome_options.add_argument(option)

service = Service("/usr/bin/chromedriver")  # Đường dẫn chromedriver

driver = webdriver.Chrome(service=service, options=chrome_options)
```

### Firefox
```python
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
for option in common_options:
    firefox_options.add_argument(option)

service = Service("/usr/bin/geckodriver")

driver = webdriver.Firefox(service=service, options=firefox_options)
```

## 5. Các thao tác cơ bản
### Mở trang web
```python
driver.get("https://www.google.com")
```

### Lấy tiêu đề trang
```python
print(driver.title)
```

### Tìm phần tử
```python
# Theo id
el = driver.find_element("id", "element_id")
# Theo class
el = driver.find_element("class name", "class_name")
# Theo xpath
el = driver.find_element("xpath", "//div[@class='abc']")
```

### Tương tác với phần tử
```python
el.click()           # Click chuột
el.send_keys("text") # Nhập dữ liệu
```

### Lấy nội dung HTML
```python
html = driver.page_source
```

### Đọc nội dung text của một thẻ
```python
el = driver.find_element("id", "element_id")
print(el.text)  # In ra nội dung text của thẻ
```

### Lấy dữ liệu theo thuộc tính
```python
el = driver.find_element("id", "element_id")
href = el.get_attribute("href")  # Lấy thuộc tính href
src = el.get_attribute("src")    # Lấy thuộc tính src
value = el.get_attribute("value")  # Lấy giá trị của input
class_name = el.get_attribute("class")  # Lấy class
```

### Lấy nhiều phần tử cùng lúc
```python
# Lấy tất cả thẻ a
links = driver.find_elements("tag name", "a")
for link in links:
    print(link.text, link.get_attribute("href"))

# Lấy tất cả phần tử có class 'item'
items = driver.find_elements("class name", "item")
for item in items:
    print(item.text)
```

### In dữ liệu ra file hoặc console
```python
import json

# In ra console
print("Title:", driver.title)
print("URL:", driver.current_url)

# Lưu dữ liệu vào file
data = {"title": driver.title, "url": driver.current_url}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# In HTML của trang
with open("page.html", "w") as f:
    f.write(driver.page_source)
```
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "element_id"))
)
```

### Đóng trình duyệt
```python
driver.quit()
```

## 6. Một số mẹo nâng cao
- Sử dụng headless để chạy không giao diện, tiết kiệm tài nguyên.
- Dùng WebDriverWait để chờ phần tử xuất hiện, tránh lỗi khi trang chưa load xong.
- Có thể thao tác với cookies, screenshot, scroll, v.v.

### Tránh tạo quá nhiều trình duyệt khi crawl nhiều nguồn
Để tiết kiệm tài nguyên và tránh lỗi, hãy dùng một instance duy nhất và navigate giữa các trang:

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo driver một lần
driver = webdriver.Chrome(service=service, options=chrome_options)

# Danh sách URLs cần crawl
urls = ["https://site1.com", "https://site2.com", "https://site3.com"]

for url in urls:
    driver.get(url)
    # Chờ trang load xong
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    # Lấy dữ liệu
    data = driver.find_element("tag name", "body").text
    print(f"Data from {url}: {data[:100]}...")  # In 100 ký tự đầu
    
    # Có thể lưu data vào file/database ở đây

# Đóng driver sau khi xong
driver.quit()
```

**Lưu ý:**
- Nếu cần crawl song song, dùng threading hoặc multiprocessing với các driver riêng.
- Đóng tab cũ nếu mở tab mới: `driver.close()` rồi `driver.switch_to.window(driver.window_handles[0])`
- Theo dõi memory usage để tránh crash khi crawl nhiều.

## 7. Tài liệu tham khảo
- Trang chủ: https://www.selenium.dev/
- API Python: https://selenium-python.readthedocs.io/

---
**Lưu ý:**
- Đảm bảo driver và trình duyệt cùng phiên bản.
- Đường dẫn driver/trình duyệt có thể thay đổi tùy hệ thống.
- Selenium phù hợp cho tự động hóa web, kiểm thử, crawl dữ liệu, v.v.

