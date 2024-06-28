import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
driver_path = r"C:\Users\DELL\Desktop\New folder\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.maximize_window()
username = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
username.click()
username.send_keys("Admin")
time.sleep(1)
password = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
password.click()
password.send_keys("admin123")
time.sleep(1)
login = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
login.click()
time.sleep(5)
title = driver.title
print(title)
default_title = "OrangeHRM"
if title in default_title:
        print("Title Matches Correctly")
else:
        print("Incorrect Title")
time.sleep(5)
admin1 = driver.find_element(By.LINK_TEXT, "Admin")
admin1.click()
time.sleep(5)
admin_menu = driver.find_elements(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li")
expected_admin_menu= ["User Management","Job","Organization","Qualifications","Nationalities","Corporate Banking","Configuration"]
for i in admin_menu:
    if i.text in expected_admin_menu:
        print("Items Matches correctly")
    else:
        print("missing Item")
driver.quit()