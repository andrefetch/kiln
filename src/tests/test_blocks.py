import unittest

from src.markdown.block_markdown import BlockType, block_to_block_type, markdown_to_blocks


class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):

        block = "# This is a heading"

        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_every_heading_level(self):

        for hashes in ["#", "##", "###", "####", "#####", "######"]:
            block = f"{hashes} A heading"

            self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_without_space_is_paragraph(self):

        block = "#Not a heading"

        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_seven_hashes_is_paragraph(self):

        block = "####### Too many hashes"

        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code(self):

        block = "```\nprint('hello')\n```"

        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote(self):

        block = "> This is a quote\n> that spans lines"

        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_with_a_broken_line_is_paragraph(self):

        block = "> This is a quote\nthis line forgot the marker"

        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list(self):

        block = "- This is a list\n- with items\n- and more items"

        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_with_a_broken_line_is_paragraph(self):

        block = "- This is a list\n-missing the space"

        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list(self):

        block = "1. First item\n2. Second item\n3. Third item"

        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_out_of_order_is_paragraph(self):

        block = "1. First item\n3. Skipped a number"

        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_not_starting_at_one_is_paragraph(self):

        block = "2. Starts at two\n3. Then three"

        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph(self):

        block = "This is a normal paragraph with **bold** and _italic_ text"

        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_multiline_paragraph(self):

        block = "This is a paragraph\nthat keeps going on a new line"

        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_blocks_from_markdown(self):

        md = """
# Kiln

This is a paragraph with _italic_ text

- a list
- with items

1. first
2. second

> a quote
> with two lines
"""

        blocks = markdown_to_blocks(md)
        block_types = []

        for block in blocks:
            block_types.append(block_to_block_type(block))

        expected_result = [
            BlockType.HEADING,
            BlockType.PARAGRAPH,
            BlockType.UNORDERED_LIST,
            BlockType.ORDERED_LIST,
            BlockType.QUOTE,
        ]

        self.assertEqual(block_types, expected_result)


if __name__ == "__main__":

    unittest.main()
