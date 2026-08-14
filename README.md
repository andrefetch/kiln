# Kiln, A Static Site Generator

A small static site generator in Python. You write pages in Markdown, run it, and get plain HTML you can drop on GitHub Pages.

Building it to understand how Hugo and Jekyll actually work instead of just using them.

## Where it's at

Inline Markdown parsing is done. A line like:

```
This is **bold** and _italic_ with `code`, a [link](https://example.com) and an ![image](cat.png)
```

gets split into typed nodes that each know how to render themselves as HTML. Bold, italic and code render fully; links and images parse correctly but drop their attributes on the way out (see step 0 below). Underneath sits a small HTML tree (`LeafNode` / `ParentNode`) that renders itself with `to_html()`. 

## Rendering is recursive

Something like `[link](https://example.com)` is really two things — the text you see and the URL behind it. The URL gets stored on the node and comes back out as an attribute (`href`, or `src` and `alt` for images) when it renders.

The rendering itself is recursive. A parent node just asks each of its children to render themselves:

```python
for child in self.children:
    result += child.to_html()
```

If a child is another parent, it does the same thing to its own children. Leaf nodes have no children, so they return their string and it stops there. One call at the top renders the whole tree, however deep it goes.

## What's next

Everything works one line at a time. Next is blocks — document structure instead of inline styling.

0. Fix props getting dropped. `LeafNode.__init__` passes `props=None` up to `HTMLNode`, and `ParentNode.to_html` never calls `props_to_html()`, so links and images currently render as bare `<a>` and `<img>`. Void elements need self-closing too.
1. Split a document into blocks on blank lines
2. Detect the type: heading, code, quote, `-` list, `1.` list, paragraph
3. Map each to HTML (`<h1>`, `<ul>`/`<li>`, `<blockquote>`), running the inline parser on the contents
4. Wrap the result in a page template with a title from the first `#`
5. Walk `content/` recursively, copy `static/` over, write everything to `public/`
6. Push it to GitHub Pages so the repo hosts its own site
