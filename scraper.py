
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def scraper(driver, url):

    driver.get(url)
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    # Extract data
    data = element.text
    return data

