from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


# --- Topic 1: Service Initialization (Automatic Driver Management) ---
# This line automatically downloads the correct ChromeDriver version
# that matches your installed Google Chrome browser.
print("Initializing Chrome Service and downloading driver...")
service = Service(ChromeDriverManager().install())

# --- Topic 2: Driver Initialization ---
# The driver is created using the automatically managed service object.
driver = webdriver.Chrome(service=service)


driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button.oxd-button--main.orangehrm-login-button").click()

act_title = driver.title
expected_title = "OrangeHRM"

if act_title == expected_title :
    print("Log in Test Passed")
else:
    print("log in test failed")
time.sleep(10)

driver.quit()






