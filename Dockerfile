FROM python:3.7

# Install mkdocs python module
RUN pip install mkdocs

# Copy project contents to container
COPY . /
WORKDIR /shared_dir

# MkDocs by default listens port 8000
EXPOSE 8000

# Run default target in makefile when there are no commands passed
ENTRYPOINT [ "make", "-s", "-f", "/Makefile" ]
CMD [ "default"]