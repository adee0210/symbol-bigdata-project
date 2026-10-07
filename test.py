import time

from selenium import webdriver

url = "https://ts.fss.com.vn/core/kimai.php"

webdriver = webdriver.Chrome()
webdriver.get(url)
time.sleep(5)  # Wait for the page to load

# xpath //*[@id="kimaiusername"]
username_field = webdriver.find_element("xpath", '//*[@id="kimaiusername"]')

# xpath pass //*[@id="kimaipassword"]
password_field = webdriver.find_element("xpath", '//*[@id="kimaipassword"]')

# enter value user name_field.send_keys("admin")
username_field.send_keys("duc.leanh")
password_field.send_keys("Anhduc$$@0210")

# enter password to login
password_field.submit()
time.sleep(5)  # Wait for the page to load

# click xpath //*[@id="timeSheet_head"]/div/a
timeSheet_head = webdriver.find_element("xpath", '//*[@id="timeSheet_head"]/div/a')
timeSheet_head.click()

time.sleep(5)
# click xpath //*[@id="add_edit_timeSheetEntry_activityID"]/option[10]
activity_option = webdriver.find_element(
    "xpath", '//*[@id="add_edit_timeSheetEntry_activityID"]/option[10]'
)
activity_option.click()

time.sleep(5)  # Wait for the page to load

# send keys to xpath //*[@id="start_day"]
start_day_field = webdriver.find_element("xpath", '//*[@id="start_day"]')
start_day_field.send_keys("08.10.2026")

time.sleep(5)

# xpath //*[@id="end_day"]
end_day_field = webdriver.find_element("xpath", '//*[@id="end_day"]')
end_day_field.send_keys("08.10.2026")

time.sleep(5)
