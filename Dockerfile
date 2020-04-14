FROM python:3.7

RUN pip install mkdocs
COPY . /mkdocs_dir
WORKDIR /mkdocs_dir
EXPOSE 8000
ENTRYPOINT [ "make" ]
CMD [ "serve"]