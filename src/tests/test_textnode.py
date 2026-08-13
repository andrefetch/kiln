import unittest
from src.textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):

    def test_eq(self):

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node, node2)

    def test_notEq(self):

        node = TextNode("This one is a different text node", TextType.CODE)
        node2 = TextNode("This is not the same node", TextType.TEXT)

        self.assertNotEqual(node, node2)

    def test_textProperty(self):

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node.text_type, node2.text_type)

    def test_urlIsNone(self):

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertIsNone(node.url)
        self.assertIsNone(node2.url)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":

    unittest.main()
