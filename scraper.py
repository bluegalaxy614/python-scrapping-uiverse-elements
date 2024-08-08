
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def scraper(driver, url):

    driver.get(url)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "article"))
    )
    all_articles = driver.find_elements(By.TAG_NAME, "article")
    
    article_data = []
    
    for article in all_articles:
        article_text = article.text
        article_data.append(article_text)
    if(article_data == []):
        return False
    return True

