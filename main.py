from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pymongo import MongoClient

# from webdriver_manager.chrome import ChromeDriverManager

from dotenv import load_dotenv
import os

from scraper import scraper

# Load environment variables from .env file
load_dotenv()

origin_url = os.getenv("TARGET_URL")

db_url = os.getenv("DB_URL")
db_name = os.getenv("DB_NAME")
db_collection = os.getenv("DB_COLLECTION")

client = MongoClient(db_url)
db = client[db_name]
db_collection = db[db_collection]

chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")

# Check if the URL is loaded successfully
if not origin_url:
    raise ValueError("TARGET_URL is not set in the .env file")

print(f"Navigating to URL: {origin_url}")

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Call the scraper
url_for_button = f"{origin_url}/buttons"

tags = ["neumorphism", "3d", "gradient"]
styles = ["tailwind", "css"]

for tag in tags:
    url_for_tag = f"{url_for_button}?tags={tag}"
    for style in styles:
        url_for_style = f"{url_for_tag}?t={style}"
        page = 0
        while True:
            next_page_url = f"{url_for_tag}&page={page}"
            is_not_final_page = scraper(db_collection, driver, next_page_url)
            if( is_not_final_page == False ):
                break
            page += 1

driver.quit()
client.close()