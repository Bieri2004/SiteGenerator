import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_two_attrs(self):
        node = HTMLNode(
            tag="a",
            value="Link",
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        result = node.props_to_html()
        self.assertIn('href="https://www.google.com"', result)
        self.assertIn('target="_blank"', result)
        self.assertTrue(result.startswith(" "))

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", value="Hello", props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_repr_contains_fields(self):
        node = HTMLNode(tag="p", value="Hi", children=[], props={"class": "text"})
        rep = repr(node)
        self.assertIn("tag=p", rep)
        self.assertIn("value=Hi", rep)
        self.assertIn("props={'class': 'text'}", rep)


if __name__ == "__main__":
    unittest.main()
