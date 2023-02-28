# Overview

## What Is MkDocs?

MkDocs is a **fast**, **simple** and **downright gorgeous** static site generator that's geared towards building project documentation.
More info: https://www.mkdocs.org/


## Prerequisites - Install pip on Windows
Follow the instructions in this article
https://www.dataquest.io/blog/install-pip-windows/ 

## Setup on-premises

```
pip install mkdocs
```

```
pip install mkdocs
           pip install mkdocs-awesome-pages-plugin mkdocs-git-revision-date-localized-plugin mkdocs-material==8.5.1 mkdocs-minify-plugin mkdocs-redirects pymdown-extensions jinja2 mkdocs-git-revision-date-localized-plugin mkdocs-include-markdown-plugin
```

## Serve (run) - User docs
1. Run:
```
cd user_docs
mkdocs serve
```

1. Open http://127.0.0.1:8000
## Serve (run) - Dev docs
1. Run:
```
cd dev_docs
mkdocs serve
```

1. Open http://127.0.0.1:8000
