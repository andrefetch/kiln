import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_propsToHtmlNoStr(self):

        node = HTMLNode(
            None,
            None,
            None,
            None
        )

        self.assertEqual(
            node.props_to_html(),
            ""
        )

    def test_propsToHtmlProps(self):

        node = HTMLNode(
            props={
                "href": "https://boot.dev", "target": "_blank"
            }
        )

        self.assertEqual(
            node.props_to_html(),
            ' href="https://boot.dev" target="_blank"'
        )

    def test_notEq(self):

        child_node = HTMLNode(tag="span", value="hello")

        parent_node = HTMLNode(
            tag="p",
            value="Front-end is awesome!",
            children=[child_node],
            props={
                "href": "https://google.com", "target": "_blank"
            }
        )

        parent_node2 = HTMLNode(
            tag="p",
            value="Front-end blows!",
            children=[child_node],
            props={
                "href": "https://boot.dev", "target": "_blank"
            }
        )

        self.assertNotEqual(parent_node, parent_node2)

    def test_leaf_to_html_p(self):

        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    def test_leaf_to_html_b(self):

        node = LeafNode("b", "This is BOLD Text!")
        self.assertEqual(node.to_html(), "<b>This is BOLD Text!</b>")

if __name__ == "__main__":

    unittest.main()
