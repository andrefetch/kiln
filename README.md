<p align="center">
  <img src="assets/new_kiln.png" alt="Kiln" width="600">
</p>

# Kiln, A Static Site Generator

A small, lightweight static site generator in Python. You write pages in Markdown, run it, and get plain HTML you can drop on GitHub Pages.

Building it to understand how Hugo and Jekyll actually work instead of just using them.

## Where it's at

Inline Markdown parsing is done. A line like:

```
This is **bold** and _italic_ with `code`, a [link](https://example.com) and an ![image](cat.png)
```

gets split into typed nodes that each know how to render themselves as HTML. Bold, italic and code render fully; links and images parse correctly but drop their attributes on the way out (see step 0 below). Underneath sits a small HTML tree (`LeafNode` / `ParentNode`) that renders itself with `to_html()`. 

## Rendering is recursive

The rendering itself is recursive. A parent node just asks each of its children to render themselves:

```python
for child in self.children:
    result += child.to_html()
```

If a child is another parent, it does the same thing to its own children. Leaf nodes have no children, so they return their string and it stops there. One call at the top renders the whole tree, however deep it goes.

### Next Up
Currently still following the project on [boot.dev!](https://www.boot.dev/courses/build-static-site-generator-python). Mainly what is needed next is to render `-` into list HTML attributes and numbered items into ordered lists.
Then lastly, display it into actual HTML and deploy the website, and make it customizable for others to use.
