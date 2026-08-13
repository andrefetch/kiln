# Static Site Generator

A small static site generator in Python. You write pages in Markdown, run it, and get plain HTML you can drop on GitHub Pages.

Building it to understand how Hugo and Jekyll actually work instead of just using them.

## Where it's at

Inline Markdown parsing is done. A line like:

```
This is **bold** and _italic_ with `code`, a [link](https://example.com) and an ![image](cat.png)
```

gets split into typed nodes that each know how to render themselves as HTML. Bold, italic, code, links and images all work, plus a small HTML tree (`LeafNode` / `ParentNode`) that renders itself with `to_html()`. 

## What's next

Everything works one line at a time. Next is blocks — document structure instead of inline styling.

1. Split a document into blocks on blank lines
2. Detect the type: heading, code, quote, `-` list, `1.` list, paragraph
3. Map each to HTML (`<h1>`, `<ul>`/`<li>`, `<blockquote>`), running the inline parser on the contents
4. Wrap the result in a page template with a title from the first `#`
5. Walk `content/` recursively, copy `static/` over, write everything to `public/`
6. Push it to GitHub Pages so the repo hosts its own site
