# below targets are self explanatory and run mkdocs
default:
	mkdocs

# Build static files and compress in to .tar.gz file in the shared directory
produce:
	mkdocs build && tar -czf /shared_dir/site.tar.gz site && rm -rf site

# This target is to serve directly from markdown files and have a benifit of livereload omn change
serve_mkd:
	mkdocs serve -a 0.0.0.0:8000

# Extract compressed .tar.gz file and run python's http server.
serve:
	tar -zxf /shared_dir/site.tar.gz && cd site && python -m http.server

produce-serve: produce serve

# This target is just to fit the requirements, which will run mkdockerize.sh
# which inturn call above produce-serve target
run:
	chmod +x /mkdockerize.sh && /mkdockerize.sh
