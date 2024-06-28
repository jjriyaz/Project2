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
time.sleep(2)
driver.maximize_window()
forgot_password = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p")
forgot_password.click()
time.sleep(2)

username = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/form/div[1]/div/div[2]/input")
username.click()
username.send_keys("Admin")
time.sleep(2)

reset = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/form/div[2]/button[2]")
reset.click()