FROM python:3.7

RUN pip install mkdocs
COPY . /
WORKDIR /shared_dir
EXPOSE 8000
ENTRYPOINT [ "make", "-f", "/Makefile" ]
CMD [ "default"]