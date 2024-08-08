
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def store_data_to_db(db_collection, document):
    db_collection.insert_one(document)
    
def store_data_by_link(db_collection, driver, link, category, tag, style):
    driver.get(link)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "main"))
    )
    
    str_for_html = driver.find_elements(By.TAG_NAME, "textarea")[0].text
    str_for_css = driver.find_elements(By.TAG_NAME, "style")[0].text
    
    element_for_views = driver.find_elements(By.CSS_SELECTOR, "div.flex.items-center.pl-3")
    views_text = element_for_views[0].text
    number_views = int(views_text.split()[0])
    
    element_for_tags = driver.find_elements(By.TAG_NAME, "aside")
    
    tag_name = element_for_tags.find_elements(By.TAG_NAME, "h2")[0].text
    elements_for_tag = element_for_tags.find_elements(By.TAG_NAME, "a")
    
    tags = []
    for tag_element in elements_for_tag:
        tags.append(tag_element.text)
        
    report_date = element_for_tags.find_elements(By.CSS_SELECTOR, "div.flex.items-center.gap-3.font-normal.text-gray-400")[0].text
    
    document = {
        "link": link,
        "html": str_for_html,
        "css": str_for_css,
        "views": number_views,
        "category": category,
        "tag": tag,
        "tag_name": tag_name,
        "style": style,
        "tags": tags,
        "report_date": report_date
    }
    
    print(document)
    
    store_data_to_db(db_collection, document)
    
def scraper(db_collection, driver, origin_url, category, tag, style, page):
    url = f"{origin_url}/{category}?t={style}&tags={tag}&page={page}"
    driver.get(url)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "section"))
    )
    
    all_articles = driver.find_elements(By.TAG_NAME, "article")
    
    for article in all_articles:
        links = article.find_elements(By.TAG_NAME, "a")
        article_links = [link.get_attribute("href") for link in links]
        for link in article_links:
            print(link)
            store_data_by_link(db_collection, driver, link, category, tag, style)
        
    if(all_articles == []):
        return False
    return True