from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the target URL from the environment variables
url = os.getenv("TARGET_URL")
chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")

# Check if the URL is loaded successfully
if not url:
    raise ValueError("TARGET_URL is not set in the .env file")

print(f"Navigating to URL: {url}")

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the website
    driver.get(url)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )

    # Extract data
    data = element.text
    print(f"Extracted Data: {data}")

finally:
    # Ensure the WebDriver is closed even if an error occurs
    driver.quit()
