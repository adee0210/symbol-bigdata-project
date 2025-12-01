from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
common_options = [
    "--no-sandbox",
    "--disable-dev-shm-usage",  # Sử dụng disk thay vì shared memory, tránh lỗi khi /dev/shm đầy
    "--disable-gpu",  # Vô hiệu hóa GPU acceleration, hữu ích trong headless hoặc môi trường không GPU
    "--disable-blink-features=AutomationControlled",  # Vô hiệu hóa tính năng tự động hóa để tránh bị phát hiện là bot
    "--no-first-run",  # Bỏ qua các bước setup lần đầu khi khởi động trình duyệt
    "--disable-default-apps",  # Vô hiệu hóa các ứng dụng mặc định của trình duyệt
    "--disable-extensions",  # Vô hiệu hóa extensions để chạy nhanh hơn và tránh xung đột
    "--headless=new",  # Chạy trình duyệt ở chế độ headless (không giao diện), phiên bản mới
]

service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(
    "https://tvc4.investing.com/4379fbb3b2cf9327a768dbfde5d69d1d/1761556750/52/52/110/history?symbol=VCB&resolution=1&from=1609459200&to=1672531199"
)
data = driver.find_element("tag name", "body")
print(data.text)


driver.quit()
