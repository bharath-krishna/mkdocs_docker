FROM python:3.7

RUN pip install mkdocs
COPY . .
ENTRYPOINT ["mkdocs"]
CMD [ "serve" ]