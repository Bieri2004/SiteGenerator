import unittest
from blocks import BlockType, block_to_block_type


class TestBlockTypes(unittest.TestCase):
    def test_heading(self):
        block = "# Heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code_block(self):
        block = "```\ncode here\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = "> quote line 1\n> quote line 2"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list_block(self):
        block = "- item 1\n- item 2"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list_block(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        block = "Just a normal paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()

