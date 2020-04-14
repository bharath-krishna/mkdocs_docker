default:
	mkdocs

produce:
	mkdocs build && tar -czf site.tar.gz site && rm -rf site

serve_mkd:
	mkdocs serve -a 0.0.0.0:8000

serve:
	tar -zxf site.tar.gz && cd site && python -m http.server