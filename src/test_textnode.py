import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_equal_text(self):
        node1 = TextNode("Text A", TextType.NORMAL)
        node2 = TextNode("Text B", TextType.NORMAL)
        self.assertNotEqual(node1, node2)

    def test_not_equal_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_equal_url(self):
        node1 = TextNode("Link", TextType.LINK, "https://a.com")
        node2 = TextNode("Link", TextType.LINK, "https://b.com")
        self.assertNotEqual(node1, node2)

    def test_default_url_none(self):
        node1 = TextNode("Text", TextType.NORMAL)
        node2 = TextNode("Text", TextType.NORMAL, None)
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = TextNode("Hello", TextType.IMAGE, "https://img.com")
        self.assertEqual(repr(node), "TextNode(Hello, image, https://img.com)")

if __name__ == "__main__":
    unittest.main()
