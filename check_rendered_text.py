#!/usr/bin/env python3
"""Compare the rendered text of two HTML files, or two whole trees.

The gate for HTML minification. Minification may change every byte of markup;
it may not change one character of what a reader sees.

Inline tags are removed with no replacement, because a browser inserts no
whitespace for </strong> or </a>. Every other tag becomes a space, because a
browser does separate block boundaries. Both halves of that rule matter:
replacing all tags with a space hides words joined across an inline boundary,
which is the defect being hunted, and removing all tags reports a failure every
time a newline between two paragraphs disappears.

Parsing uses html.parser from the standard library rather than a tag regex.
A regex of the form <[^>]*> truncates on a > inside a quoted attribute and
leaks the remainder of the attribute into the text it claims to have stripped.

Usage:
    python3 check_rendered_text.py before.html after.html
    python3 check_rendered_text.py before_tree/ after_tree/
"""

import argparse
import os
import re
import sys
from html.parser import HTMLParser

# Phrasing content per the HTML specification, minus <br>, which represents a
# line break and therefore does separate words. Anything not listed here is
# treated as a block boundary.
INLINE_TAGS = frozenset({
    "a", "abbr", "b", "bdi", "bdo", "button", "cite", "code", "data", "dfn",
    "em", "i", "img", "input", "kbd", "label", "mark", "meter", "output",
    "picture", "progress", "q", "rp", "rt", "ruby", "s", "samp", "select",
    "slot", "small", "span", "strong", "sub", "sup", "svg", "textarea",
    "time", "u", "var", "wbr",
})

SKIP_CONTENT = frozenset({"script", "style", "template"})
WHITESPACE = re.compile(r"\s+")


class TextExtractor(HTMLParser):
    """Collect visible text, modelling inline and block tags differently."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self._skip_depth = 0

    def _boundary(self, tag):
        if tag not in INLINE_TAGS:
            self.parts.append(" ")

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_CONTENT:
            self._skip_depth += 1
        self._boundary(tag)

    def handle_startendtag(self, tag, attrs):
        self._boundary(tag)

    def handle_endtag(self, tag):
        if tag in SKIP_CONTENT and self._skip_depth:
            self._skip_depth -= 1
        self._boundary(tag)

    def handle_data(self, data):
        if not self._skip_depth:
            self.parts.append(data)

    def text(self):
        return WHITESPACE.sub(" ", "".join(self.parts)).strip()


def rendered_text(path):
    """Return the visible text of an HTML file, with whitespace normalized."""
    with open(path, encoding="utf-8", errors="replace") as handle:
        parser = TextExtractor()
        parser.feed(handle.read())
        parser.close()
        return parser.text()


def _first_difference(before, after):
    for index in range(min(len(before), len(after))):
        if before[index] != after[index]:
            start = max(0, index - 60)
            return (f"  first difference at char {index}\n"
                    f"  before: ...{before[start:index + 60]}...\n"
                    f"  after:  ...{after[start:index + 60]}...")
    return f"  one side is a prefix of the other, diverging at char {min(len(before), len(after))}"


def _html_paths(root):
    found = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if not os.path.islink(os.path.join(dirpath, d)))
        for filename in sorted(filenames):
            if filename.endswith((".html", ".htm")):
                path = os.path.join(dirpath, filename)
                found[os.path.relpath(path, root)] = path
    return found


def compare_trees(before_root, after_root):
    """Compare every HTML page in two trees. Returns a list of problems."""
    before = _html_paths(before_root)
    after = _html_paths(after_root)
    problems = []

    for relative in sorted(set(before) - set(after)):
        problems.append(f"missing in after: {relative}")
    for relative in sorted(set(after) - set(before)):
        problems.append(f"unexpected in after: {relative}")

    for relative in sorted(set(before) & set(after)):
        b = rendered_text(before[relative])
        a = rendered_text(after[relative])
        if b != a:
            problems.append(f"text changed: {relative}\n{_first_difference(b, a)}")

    return problems, len(set(before) & set(after))


def main():
    parser = argparse.ArgumentParser(description="Compare rendered text of HTML files or trees")
    parser.add_argument("before")
    parser.add_argument("after")
    args = parser.parse_args()

    if os.path.isdir(args.before) != os.path.isdir(args.after):
        parser.error("pass either two files or two directories, not one of each")

    if os.path.isdir(args.before):
        problems, compared = compare_trees(args.before, args.after)
        if problems:
            print(f"DIFFERENT: {len(problems)} problem(s) across {compared} compared page(s)")
            for problem in problems[:20]:
                print(f"- {problem}")
            if len(problems) > 20:
                print(f"... and {len(problems) - 20} more")
            sys.exit(1)
        print(f"OK: rendered text identical across {compared} page(s)")
        return

    before = rendered_text(args.before)
    after = rendered_text(args.after)
    if before == after:
        print(f"OK: rendered text identical ({len(before)} chars)")
        return
    print("DIFFERENT: rendered text changed")
    print(f"  before: {len(before)} chars")
    print(f"  after:  {len(after)} chars")
    print(_first_difference(before, after))
    sys.exit(1)


if __name__ == "__main__":
    main()
