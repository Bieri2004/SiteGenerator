import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches,
        )

    def test_extract_multiple_images(self):
        text = (
            "![one](https://example.com/1.png) and "
            "![two](https://example.com/2.png)"
        )
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("one", "https://example.com/1.png"),
                ("two", "https://example.com/2.png"),
            ],
            matches,
        )

    def test_extract_markdown_links(self):
        text = (
            "This is text with a link [to boot dev](https://www.boot.dev) "
            "and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )

    def test_images_not_matched_as_links(self):
        text = "![image](https://example.com/img.png)"
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()
