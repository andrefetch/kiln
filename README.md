<p align="center">
  <img src="assets/new_kiln.png" alt="Kiln" width="600">
</p>

# Kiln, A Static Site Generator

A small, lightweight static site generator in Python. You write pages in Markdown, run it, and get plain HTML you can drop on GitHub Pages!

Built to understand how Hugo and Jekyll actually work instead of just using them. No dependencies, standard library only.

Live demo: **[andrefetch.github.io/kiln](https://andrefetch.github.io/kiln/)**

## Usage

```bash
./main.sh    # build into docs/ and serve it on localhost:8888
./build.sh   # build for GitHub Pages (basepath /kiln/)
./test.sh    # run the unit tests
```

Drop Markdown into `content/`, static files into `static/`, and everything lands in `docs/` mirroring the same structure. `content/blog/tom/index.md` becomes `docs/blog/tom/index.html`. Every page is wrapped in `template.html`, where `{{ Title }}` is filled from the page's `# heading` and `{{ Content }}` from the rendered body.

The basepath argument rewrites every root-relative `href="/` and `src="/` so the site works from a subdirectory like `user.github.io/kiln/` instead of only from a domain root.

## Layout

```
content/        markdown pages         src/nodes/      HTMLNode / LeafNode / ParentNode
static/         css and images         src/markdown/   inline + block parsing
docs/           generated output       src/tests/      36 unit tests
template.html   page shell             src/main.py     build pipeline
```

## How it works

Markdown goes through four passes:

1. **Blocks**: the document is split on blank lines and each block gets typed as a heading, code, quote, unordered list, ordered list, or a paragraph if nothing else matches.
2. **Inline**: text inside a block is split on delimiters into typed `TextNode`s for `**bold**`, `_italic_`, `` `code` ``, `[links](url)` and `![images](url)`.
3. **Tree**: each node converts into an HTML node. `LeafNode` holds a tag and a value, `ParentNode` holds children, and props become attributes so links keep their `href` and images their `src` and `alt`.
4. **Render**: `to_html()` is called once at the top and the whole tree comes out as a string.

## Rendering is recursive

The rendering itself is recursive. A parent node just asks each of its children to render themselves.

```python
for child in self.children:
    result += child.to_html()
```

If a child is another parent, it does the same thing to its own children. Leaf nodes have no children, so they return their string and it stops there. One call at the top renders the whole tree, however deep it goes.

Page generation works the same way: `generate_page()` walks `content/` and recurses into every subdirectory, and `copy_dir()` mirrors `static/` the same way.

## Deploying

`build.sh` writes into `docs/`, which GitHub Pages can serve directly. Point Pages at the `docs/` folder on `main`, commit the build, and push. Change the basepath in `build.sh` to match your own repository name.

## Status

The [boot.dev project](https://www.boot.dev/courses/build-static-site-generator-python) is complete: full inline and block parsing, recursive page generation, static asset copying, and a deployed site.

