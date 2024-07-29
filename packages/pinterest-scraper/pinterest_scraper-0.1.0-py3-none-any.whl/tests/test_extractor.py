import unittest
from pinterest_scraper import CommentExtractor, PinterestExtractorError

class TestCommentExtractor(unittest.TestCase):
    def test_extract_usernames(self):
        html_content = """
        <div data-test-id="commentThread-comment">
            <a href="/user1/">User 1</a>
        </div>
        <div data-test-id="commentThread-comment">
            <a href="/user2/">User 2</a>
        </div>
        """
        try:
            usernames = CommentExtractor.extract_usernames(html_content)
            self.assertEqual(usernames, ["user1", "user2"])
        except PinterestExtractorError as e:
            self.fail(f"PinterestExtractorError: {e}")

if __name__ == "__main__":
    unittest.main()
