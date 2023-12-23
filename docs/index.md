# Sphinx admonition MWE

```{toctree}
: maxdepth: 2
: titlesonly: true

self
other_page
referencing_page
```

```{include} admonition.md
: start-after: <!-- admonition-1-start -->
: end-before: <!-- admonition-1-end -->
```

[Link to top admonition](#test-warning)
[Link to other admonition](other_page.md#test-warning)
