
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def scraper(driver, url):
    try:
    
        driver.get(url)
        
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        # Extract data
        data = element.text
        return data
    finally:
        driver.quit()

