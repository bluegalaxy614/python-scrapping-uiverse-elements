from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import time

def store_data_to_db(db_collection, document):
    """Stores the document in the MongoDB collection."""
    try:
        db_collection.insert_one(document)
    except Exception as e:
        print(f"Error storing document to MongoDB: {e}")

def store_data_by_link(db_collection, driver, link, category, tag, style):
    """Extracts data from the provided link and stores it in the MongoDB collection."""
    try:
        driver.get(link)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "main"))
        )

        css_code, html_code, views_number, tags, report_date = None, None, 0, [], ""

        try:
            css_code_element = driver.find_element(By.TAG_NAME, "textarea")
            css_code = css_code_element.text if css_code_element else None
        except Exception as e:
            print(f"Error finding CSS code: {e}")
            
        if(css_code == None):
            return

        if tag == "css":
            try:
                html_button = driver.find_element(By.CSS_SELECTOR, "button.px-4.py-1.pl-3.max-w-[170px] w-full.cursor-pointer.font-sans.text-base.font-semibold.text-gray-200.flex.gap-2.items-center.transition-colors.rounded-b-none.border-none.rounded-md.label.hover:bg-[#1e1e1e].bg-dark-700")
                if html_button:
                    html_button.click()
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME, "main"))
                    )
                    html_code_element = driver.find_element(By.TAG_NAME, "textarea")
                    html_code = html_code_element.text if html_code_element else None
            except Exception as e:
                print(f"Error retrieving HTML code: {e}")

        try:
            views_element = driver.find_element(By.CSS_SELECTOR, "div.flex.items-center.pl-3")
            views_text = views_element.text if views_element else "0 views"
            views_number = int(views_text.split()[0])
        except Exception as e:
            print(f"Error retrieving views: {e}")

        try:
            tags_element = driver.find_element(By.TAG_NAME, "aside")
            tags = [tag_element.text for tag_element in tags_element.find_elements(By.TAG_NAME, "a")] if tags_element else []
        except Exception as e:
            print(f"Error retrieving tags: {e}")

        try:
            report_date_element = driver.find_element(By.CSS_SELECTOR, "div.flex.items-center.gap-3.font-normal.text-gray-400")
            report_date = report_date_element.text if report_date_element else ""
        except Exception as e:
            print(f"Error retrieving report date: {e}")

        document = {
            "category": category,
            "tag": tag,
            "style": style,
            "link": link,
            "html": html_code,
            "css": css_code,
            "views": views_number,
            "tags": tags,
            "report_date": report_date
        }

        print(f"Document to be stored: {document}")
        store_data_to_db(db_collection, document)
    except Exception as e:
        print(f"Error processing link {link}: {e}")

def scraper(db_collection, driver, origin_url, category, tag, style, page):
    """Scrapes data from a specific page and processes the links."""
    url = f"{origin_url}/{category}?t={style}&tags={tag}&page={page}"
    driver.get(url)

    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "section"))
        )

        all_articles = driver.find_elements(By.TAG_NAME, "article")

        if not all_articles:
            return False

        links = []
        for article in all_articles:
            article_links = [link.get_attribute("href") for link in article.find_elements(By.TAG_NAME, "a") if link.get_attribute("href")]
            links.extend(article_links)

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [
                executor.submit(store_data_by_link, db_collection, driver, link, category, tag, style)
                for link in links
            ]

            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"Error during threaded execution: {e}")

        return True

    except Exception as e:
        print(f"Error scraping page {page} for {category} - {tag} - {style}: {e}")
        return False

def main():
    """Main function to run the scraper."""
    load_dotenv()

    origin_url = os.getenv("TARGET_URL")
    db_url = os.getenv("DB_URL")
    db_name = os.getenv("DB_NAME")
    db_collection_name = os.getenv("DB_COLLECTION")
    chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")

    if not origin_url or not db_url or not db_name or not db_collection_name or not chrome_driver_path:
        raise ValueError("One or more required environment variables are not set in the .env file")

    client = MongoClient(db_url)
    db = client[db_name]
    db_collection = db[db_collection_name]

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)

    categories = ["buttons", "checkboxes", "switches", "cards", "loaders", "inputs", "radio-buttons", "forms", "patterns", "tooltips"]
    tags = ["neumorphism", "3d", "gradient"]
    styles = ["tailwind", "css"]

    try:
        for category in categories:
            for tag in tags:
                for style in styles:
                    page = 0
                    while True:
                        is_not_final_page = scraper(db_collection, driver, origin_url, category, tag, style, page)
                        if not is_not_final_page:
                            break
                        time.sleep(1)  # Be polite to the server and avoid potential rate limits
                        page += 1
    finally:
        driver.quit()
        client.close()

if __name__ == "__main__":
    main()
