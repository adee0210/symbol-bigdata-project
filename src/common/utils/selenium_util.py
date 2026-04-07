import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumUtil:

    def __init__(self):
        chromium_option = Options()
        chromium_option.add_argument("--no-sandbox")
        chromium_option.add_argument("--disable-dev-shm-usage")
        chromium_option.add_argument("--disable-gpu")
        chromium_option.add_argument("--disable-blink-features=AutomationControlled")
        chromium_option.add_argument("--no-first-run")
        chromium_option.add_argument("--disable-default-apps")
        chromium_option.add_argument("--disable-extensions")
        # chromium_option.add_argument("--headless=new")
        self.chrome_driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chromium_option,
        )

    def extract_element_from_url_to_json(self, url, by_element, element_name):
        try:
            self.chrome_driver.get(url=url)
            WebDriverWait(self.chrome_driver, 10).until(
                lambda d: len(
                    d.find_element(by=by_element, value=element_name).text.strip()
                )
                > 0
            )
            data = self.chrome_driver.find_element(
                by=by_element, value=element_name
            ).text
            data = json.loads(data)
            print(data["t"][0])

        finally:
            self.chrome_driver.quit()
