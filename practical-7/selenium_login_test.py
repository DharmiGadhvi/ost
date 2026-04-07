from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Start browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

# Wait
wait = WebDriverWait(driver, 10)

# Enter username
username = wait.until(
    EC.presence_of_element_located((By.ID, "username"))
)
username.send_keys("tomsmith")

# Enter password
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Click login
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

# Verify login
message = wait.until(
    EC.presence_of_element_located((By.ID, "flash"))
)
print("Login Message:", message.text)

# Logout
driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius").click()

# Close browser
time.sleep(3)
driver.quit()