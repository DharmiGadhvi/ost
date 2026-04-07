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

driver.get("https://www.youtube.com")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Find search box
search_box = wait.until(
    EC.presence_of_element_located((By.NAME, "search_query"))
)
search_box.send_keys("Open Source Technology")

# Click search button
search_button = wait.until(
    EC.element_to_be_clickable((By.ID, "search-icon-legacy"))
)
search_button.click()

time.sleep(5)

print("Search executed successfully")

driver.quit()