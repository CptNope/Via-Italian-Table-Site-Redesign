#!/usr/bin/env python3
"""Make artifact-ready copies of a site page (the host adds its own document shell)."""
import pathlib, re, sys
src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
s = src.read_text()
s = re.sub(r'^<!doctype html>\s*<html[^>]*>\s*<head>\s*<meta charset="utf-8">\s*<meta name="viewport"[^>]*>\s*', '', s)
s = s.replace('<title>', '<meta name="claude:viewport-fit-sides" content="cover">\n<title>', 1)
s = s.replace('</head>\n<body>\n', '', 1)
s = re.sub(r'</body>\s*</html>\s*$', '', s)
out.write_text(s)
