import json
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SeleniumUtil:
    def __init__(self, url):

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

        chrome_service = Service("/usr/bin/chromedriver")
        self.chrome_driver = webdriver.Chrome(
            options=chrome_option, service=chrome_service
        )
        self.url = url

    def get_data_by_tag_name(self, tag_name):
        self.chrome_driver.get(url=self.url)

        WebDriverWait(self.chrome_driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, tag_name))
        )
        tag_name_data = json.loads(
            self.chrome_driver.find_element(by=By.TAG_NAME, value=tag_name).text
        )
        return tag_name_data
