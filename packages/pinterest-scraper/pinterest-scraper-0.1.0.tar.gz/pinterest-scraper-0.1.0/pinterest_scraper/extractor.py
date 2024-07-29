from bs4 import BeautifulSoup
from .exceptions import PinterestExtractorError

class CommentExtractor:
    @staticmethod
    def extract_usernames(html_content):
        try:
            soup = BeautifulSoup(html_content, "html.parser")
            comment_divs = soup.find_all("div", {"data-test-id": "commentThread-comment"})

            usernames = []
            for div in comment_divs:
                a_tag = div.find("a", href=True)
                if a_tag:
                    username = a_tag['href'].strip('/')
                    usernames.append(username)
            return usernames
        except Exception as e:
            raise PinterestExtractorError(f"Failed to extract usernames: {e}")
