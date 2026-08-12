import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):

    def test_eq(self):

        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)

        self.assertEqual(node, node2)

    def test_notEq(self):

        node = TextNode("This one is a different text node", TextType.CODE_TEXT)
        node2 = TextNode("This is not the same node", TextType.PLAIN_TEXT)

        self.assertNotEqual(node, node2)

    def test_textProperty(self):

        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)

        self.assertEqual(node.text_type, node2.text_type)

    def test_urlIsNone(self):

        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)

        self.assertIsNone(node.url)
        self.assertIsNone(node2.url)

if __name__ == "__main__":

    unittest.main()
