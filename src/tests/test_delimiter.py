import unittest

from src.markdown.inline_markdown import split_nodes_delimiter
from src.nodes.textnode import TextType, TextNode


class TestSplitDelimiter(unittest.TestCase):

    def test_basic_split(self):

        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, expected_result)

    def test_unclosed_delimiter(self):

        with self.assertRaises(Exception):
            node = TextNode("Unclosed `delimiter here", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
