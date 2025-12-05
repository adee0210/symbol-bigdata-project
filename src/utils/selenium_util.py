import json
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumUtil:
    def __init__(self):
        common_option = [
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--disable-blink-features=AutomationControlled",
            "--no-first-run",
            "--disable-default-apps",
            "--disable-extensions",
            # "--headless",
        ]
        chrome_option = Options()
        for option in common_option:
            chrome_option.add_argument(option)

        chrome_service = Service(ChromeDriverManager().install())
        self.chrome_driver = webdriver.Chrome(
            options=chrome_option, service=chrome_service
        )

    def get_data_by_tag_name(self, url, tag_name):
        # Mở tab mới cho mỗi URL
        self.chrome_driver.execute_script("window.open('');")
        self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[-1])

        self.chrome_driver.get(url=url)

        WebDriverWait(self.chrome_driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, tag_name))
        )
        tag_name_data = json.loads(
            self.chrome_driver.find_element(by=By.TAG_NAME, value=tag_name).text
        )

        # Đóng tab hiện tại và chuyển về tab chính
        self.chrome_driver.close()
        self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[0])

        return tag_name_data

    def quit_selenium_util(self):
        self.chrome_driver.quit()
