
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from mongo import store_data_to_db

def store_data_by_link(db_collection, driver, link):
    driver.get(link)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "main"))
    )
    
    # store_data_to_db(db_collection, document)
def scraper(db_collection, driver, url):

    driver.get(url)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "section"))
    )
    
    all_articles = driver.find_elements(By.TAG_NAME, "article")
    
    for article in all_articles:
        links = article.find_elements(By.TAG_NAME, "a")
        article_links = [link.get_attribute("href") for link in links]
        for link in article_links:
            store_data_by_link(db_collection, driver, link)
        
    if(all_articles == []):
        return False
    return True