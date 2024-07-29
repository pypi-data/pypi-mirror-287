import unittest
from pinterest_scraper import PinterestScraper, PinterestScraperError

class TestPinterestScraper(unittest.TestCase):
    def test_get_page_source(self):
        scraper = PinterestScraper(headless=True)
        url = "https://www.pinterest.com/pin/703756187242133/"
        try:
            html_content = scraper.get_page_source(url)
            self.assertIn("<html", html_content)
        except PinterestScraperError as e:
            self.fail(f"PinterestScraperError: {e}")

if __name__ == "__main__":
    unittest.main()
