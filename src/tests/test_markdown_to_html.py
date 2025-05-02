from src.markdown_to_html import markdown_to_html_node

def test_markdown_to_html_node_paragraphs() -> None:
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
    node = markdown_to_html_node(md)
    test = node.to_html()
    result = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
    assert test == result
    
def test_markdown_to_html_node_codeblock() -> None:
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    test = node.to_html()
    result = "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
    assert test == result
    

def test_mixed_content() -> None:
    md = """# Heading 1

This is a paragraph with **bold** and _italic_ text.

## Heading 2

* List item 1
* List item 2 with `code`

> This is a blockquote with **formatting**

```
def sample_code():
    return "No formatting here"
```
"""

    node = markdown_to_html_node(md)
    test = node.to_html()
    result = "<div><h1>Heading 1</h1><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p><h2>Heading 2</h2><ul><li>List item 1</li><li>List item 2 with <code>code</code></li></ul><blockquote>This is a blockquote with <b>formatting</b></blockquote><pre><code>def sample_code():\n    return \"No _formatting_ here\"\n</code></pre></div>"
    assert test == result

def test_ordered_list() -> None:
    md = """
1. First item
2. Second item with **bold**
3. Third item with `code` and _italic_
"""
    node = markdown_to_html_node(md)
    test = node.to_html()
    result = "<div><ol><li>First item</li><li>Second item with <b>bold</b></li><li>Third item with <code>code</code> and <i>italic</i></li></ol></div>"
    assert test == result
