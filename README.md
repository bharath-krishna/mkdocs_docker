![Docker Image CI](https://github.com/bharath-krishna/mkdocs_docker/workflows/Docker%20Image%20CI/badge.svg?branch=master)

# MkDocs

MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building
project documentation. Documentation source files are written in Markdown, and configured with a single
YAML configuration file. Start by reading the introduction below, then check the User Guide for more info.

## How to use

First from the root dir build the docker image as below
> docker build -t <image_name> .

### To produce a .tar.gz file of the static files

> docker run -it --rm -v <path_to_docs>:/shared_dir -p 8000:8000 mkdocs_image produce

### To serve the docs from the produced static files, run as below

> docker run -it --rm -v <dir_of_tar.gz_file>:/shared_dir -p 8000:8000 mkdocs_image serve

### To serve from markdown files instead of producing to a .tar.gz then run as below

> docker run -it --rm -v <path_to_docs>:/shared_dir -p 8000:8000 mkdocs_image serve_mkd

## Example

checkout code from <https://github.com/bharath-krishna/mkdocs_docker> to a dir 
/triad_challenge

then you can produce the compressed file from that docs as 

> docker run -it --rm -v /triad_challenge/:/shared_dir -p 8000:8000 mkdocs_image produce

a site.tar.gz file will be placed in the /triad_challenge dir

> Note: `/shared_dir` is a standard name, do not change it.
