from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from .exceptions import PinterestScraperError

class PinterestScraper:
    def __init__(self, headless=True):
        options = Options()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
        self.driver = webdriver.Chrome(options=options)

    def get_page_source(self, url, wait_time=20, scroll_pause_time=2):
        try:
            self.driver.get(url)
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            while True:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(scroll_pause_time)
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test-id='commentThread-comment']"))
            )
            return self.driver.page_source
        except Exception as e:
            raise PinterestScraperError(f"Failed to get page source: {e}")
        finally:
            self.driver.quit()
