from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

from dotenv import load_dotenv
import os

from scraper import scraper

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

# Call the scraper
data = scraper(driver, url)
print(f"Extracted Data: {data}")
