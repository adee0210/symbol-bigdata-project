from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Test by opening a page
driver.get("https://www.google.com")

# Close the browser
driver.quit()
